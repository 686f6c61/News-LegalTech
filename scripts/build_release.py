#!/usr/bin/env python3
"""Empaqueta la release diaria de datos abiertos.

Lee ``events/YYYY-MM-DD/`` (y el digest ya escrito, si existe) y emite
``releases/<version>/graph.jsonld`` mas ``RELEASE.md``. No inventa eventos
ni hace el scan editorial: si la carpeta del dia no tiene piezas, no hay release.

Versionado
----------
La version de las releases futuras es la fecha editorial Europe/Madrid en
``DD.MM.YY`` (dia, mes y año de dos digitos). Asi 2026-10-02 es ``02.10.26``
y 2026-10-01 seria ``01.10.26``. El siglo asumido al leer una carpeta nueva
es 2000-2099. El titulo publico es ``Radar LegalTech · DD.MM.YY``.
``/releases/latest`` apunta al ultimo tag publicado.

Lo ya publicado en ``YY.MM.DD`` no se migra ni se reescribe:
``26.09.29``, ``26.09.30`` y ``26.10.01``.

Un dia sin carpeta ``events/YYYY-MM-DD/`` no genera release y no renumera
otros dias: la version sigue siendo la fecha. Antes de escribir, la carpeta
``releases/DD.MM.YY/`` y el tag git del mismo nombre se contrastan con la
fecha declarada en ``RELEASE.md`` para no pisar otra fecha. Una carpeta
historica ``YY.MM.DD`` cuya fecha coincide con el dia no se convierte al
formato nuevo.

Namespace (grafos que escribe este script)
------------------------------------------
- Vocabulario ``sota:`` -> ``https://legalnews.686f6c61.dev/ns#``
- ``@id`` de release, evento y entidad bajo
  ``https://github.com/686f6c61/News-LegalTech/...``
- Descarga del artefacto:
  ``https://github.com/686f6c61/News-LegalTech/releases/download/<version>/graph.jsonld``

``releases/26.09.29/graph.jsonld`` conserva ``https://legaltech-sota.local/``
(salvo las referencias de version, ya en ``26.09.29``) y este script no lo
reescribe.

Uso
---
  python scripts/build_release.py --date 2026-10-02
  python scripts/build_release.py --pending
  python scripts/build_release.py --list-pending
  python scripts/build_release.py --check-published
  python scripts/build_release.py --date 2026-10-02 --dry-run
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

try:
    import yaml
except ImportError:  # pragma: no cover - el workflow instala PyYAML
    yaml = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parents[1]
MADRID = ZoneInfo("Europe/Madrid")

REPO_HTML = "https://github.com/686f6c61/News-LegalTech"
SOTA_NS = "https://legalnews.686f6c61.dev/ns#"
LEGACY_NS = "https://legaltech-sota.local/"
PUBLIC_TITLE = "Radar LegalTech"

_DD = r"0[1-9]|[12]\d|3[01]"
_MM = r"0[1-9]|1[0-2]"
_YY = r"\d{2}"
# Politica vigente: dia.mes.año corto.
CALENDAR_VERSION_RE = re.compile(rf"^v?(?P<dd>{_DD})\.(?P<mm>{_MM})\.(?P<yy>{_YY})$")
# Historico publicado (26.09.29, 26.09.30, 26.10.01). No se asigna a dias nuevos.
LEGACY_CALENDAR_VERSION_RE = re.compile(rf"^v?(?P<yy>{_YY})\.(?P<mm>{_MM})\.(?P<dd>{_DD})$")
LEGACY_RELEASE_RE = re.compile(r"^v?1\.\d+\.0$")
DATE_IN_NOTES_RE = re.compile(r"\*\*Fecha:\*\*\s*(\d{4}-\d{2}-\d{2})")
RELEASE_LINE_RE = re.compile(r"(?m)^release:\s*(.+?)\s*$")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)

PLACEHOLDER_RELEASES = {
    "",
    "full-radar-local",
    "unreleased",
    "pending",
    "tbd",
    "draft",
}


class ReleaseError(Exception):
    def __init__(self, message: str, code: int = 1) -> None:
        super().__init__(message)
        self.code = code


@dataclass
class BuildResult:
    day: date
    version: str
    skipped: bool = False
    changed: bool = False
    historical: bool = False
    event_count: int = 0
    graph_path: Path | None = None
    notes_path: Path | None = None
    message: str = ""
    stamped: list[str] = field(default_factory=list)


def madrid_today() -> date:
    return datetime.now(MADRID).date()


def parse_day(value: str) -> date:
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError as exc:
        raise ReleaseError(f"Fecha invalida (se espera YYYY-MM-DD): {value}") from exc


def version_for_date(day: date) -> str:
    """Fecha editorial Europe/Madrid como ``DD.MM.YY``."""
    return f"{day.day:02d}.{day.month:02d}.{day.year % 100:02d}"


def legacy_version_for_date(day: date) -> str:
    """Formato historico ``YY.MM.DD``. No se asigna a releases nuevas."""
    return f"{day.year % 100:02d}.{day.month:02d}.{day.day:02d}"


def _date_from_version_match(match: re.Match[str]) -> date | None:
    try:
        return date(
            2000 + int(match.group("yy")),
            int(match.group("mm")),
            int(match.group("dd")),
        )
    except ValueError:
        return None


def parse_calendar_version(name: str) -> date | None:
    """Lee ``DD.MM.YY`` (o ``vDD.MM.YY``) como fecha del siglo 2000-2099."""
    match = CALENDAR_VERSION_RE.match(name.strip())
    if not match:
        return None
    return _date_from_version_match(match)


def parse_legacy_calendar_version(name: str) -> date | None:
    """Lee ``YY.MM.DD`` historico (o ``vYY.MM.DD``) como fecha del siglo 2000-2099."""
    match = LEGACY_CALENDAR_VERSION_RE.match(name.strip())
    if not match:
        return None
    return _date_from_version_match(match)


def _is_calendar_release_name(name: str) -> bool:
    return (
        parse_calendar_version(name) is not None
        or parse_legacy_calendar_version(name) is not None
    )


def notes_date(notes_path: Path) -> date | None:
    if not notes_path.is_file():
        return None
    match = DATE_IN_NOTES_RE.search(notes_path.read_text(encoding="utf-8"))
    if not match:
        return None
    return parse_day(match.group(1))


def is_historical_graph(graph_path: Path) -> bool:
    if not graph_path.is_file():
        return False
    return LEGACY_NS in graph_path.read_text(encoding="utf-8")


def git_tags(root: Path) -> list[str]:
    """Tags del repo, si ``root`` es un checkout git. Si no, lista vacia."""
    if not (root / ".git").exists():
        return []
    try:
        proc = subprocess.run(
            ["git", "-C", str(root), "tag", "-l"],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return []
    if proc.returncode != 0:
        return []
    return [line.strip() for line in proc.stdout.splitlines() if line.strip()]


def _tag_matches_version(tag: str, version: str) -> bool:
    if tag == version:
        return True
    return tag == f"v{version}" and CALENDAR_VERSION_RE.match(tag) is not None


def legacy_release_version(root: Path, day: date) -> str | None:
    """Carpeta ``YY.MM.DD`` ya publicada para ``day``, o None.

    Si el nombre historico coincide con ``DD.MM.YY`` (el dia es el año corto),
    no hay una carpeta distinta que preservar.
    """
    legacy = legacy_version_for_date(day)
    if legacy == version_for_date(day):
        return None
    folder = root / "releases" / legacy
    graph = folder / "graph.jsonld"
    if not graph.is_file():
        return None
    if notes_date(folder / "RELEASE.md") != day:
        return None
    return legacy


def resolve_version(root: Path, day: date) -> str:
    """``DD.MM.YY`` de la fecha, contrastada con carpeta y tag de ese nombre.

    No reescribe una release historica ``YY.MM.DD``: el llamador debe
    consultarla con ``legacy_release_version`` y dejarla intacta.
    """
    version = version_for_date(day)
    notes = root / "releases" / version / "RELEASE.md"
    recorded = notes_date(notes)
    if recorded is not None and recorded != day:
        raise ReleaseError(
            f"{version} ya esta asignada a {recorded.isoformat()} "
            f"({notes}). {day.isoformat()} no puede reutilizarla.",
            code=2,
        )
    if recorded != day:
        for tag in git_tags(root):
            if _tag_matches_version(tag, version):
                raise ReleaseError(
                    f"El tag {tag} ya usa {version}. "
                    f"{day.isoformat()} no puede reutilizarlo.",
                    code=2,
                )
    return version


def _require_yaml() -> None:
    if yaml is None:
        raise ReleaseError(
            "Falta PyYAML. Instala con: pip install -r scripts/requirements.txt"
        )


def index_event_ids(day_dir: Path) -> list[str] | None:
    index = day_dir / "index.yaml"
    if not index.is_file():
        return None
    _require_yaml()
    data = yaml.safe_load(index.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        return None
    if isinstance(data.get("event_ids"), list):
        return [str(item) for item in data["event_ids"]]
    events = data.get("events")
    if isinstance(events, list):
        ids: list[str] = []
        for item in events:
            if isinstance(item, dict) and item.get("id"):
                ids.append(str(item["id"]))
            elif isinstance(item, str):
                ids.append(item)
        return ids
    return None


def event_paths(day_dir: Path) -> dict[str, Path]:
    found: dict[str, Path] = {}
    if not day_dir.is_dir():
        return found
    for path in sorted(day_dir.glob("evt-*.yaml")):
        found[path.stem] = path
    for path in sorted(day_dir.glob("evt-*.json")):
        found[path.stem] = path
    return found


def ordered_event_ids(day_dir: Path) -> list[str]:
    on_disk = event_paths(day_dir)
    if not on_disk:
        return []
    indexed = index_event_ids(day_dir)
    if not indexed:
        return sorted(on_disk)
    missing = [event_id for event_id in indexed if event_id not in on_disk]
    if missing:
        raise ReleaseError(
            f"{day_dir.name}: index.yaml cita eventos sin fichero: {', '.join(missing)}"
        )
    extras = sorted(set(on_disk) - set(indexed))
    if extras:
        print(
            f"aviso: {day_dir.name} tiene eventos fuera de index.yaml: {', '.join(extras)}",
            file=sys.stderr,
        )
    return list(indexed) + extras


def load_event(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix == ".json":
        data = json.loads(text)
    else:
        _require_yaml()
        data = yaml.safe_load(text)
    if not isinstance(data, dict):
        raise ReleaseError(f"{path} no es un objeto de evento")
    return data


def load_day_events(root: Path, day: date) -> list[dict]:
    day_dir = root / "events" / day.isoformat()
    paths = event_paths(day_dir)
    events: list[dict] = []
    for event_id in ordered_event_ids(day_dir):
        event = load_event(paths[event_id])
        if event.get("id") and event["id"] != event_id:
            raise ReleaseError(
                f"{paths[event_id].name}: id {event.get('id')!r} no coincide con el fichero"
            )
        event.setdefault("id", event_id)
        _require_event_fields(event, paths[event_id])
        events.append(event)
    return events


def _require_event_fields(event: dict, path: Path) -> None:
    required = ("id", "date", "type", "sota_score", "ai_legaltech", "title", "summary_p1", "summary_p2", "sources")
    missing = [key for key in required if event.get(key) in (None, "", [])]
    if missing:
        raise ReleaseError(f"{path.name}: faltan campos {', '.join(missing)}")
    if not isinstance(event["sources"], list):
        raise ReleaseError(f"{path.name}: sources debe ser una lista")


def known_event_types(root: Path) -> set[str]:
    schema_path = root / "schemas" / "event.schema.json"
    if not schema_path.is_file():
        return set()
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    try:
        return set(schema["properties"]["type"]["enum"])
    except (KeyError, TypeError):
        return set()


def resource_id(kind: str, ident: str) -> str:
    return f"{REPO_HTML}/{kind}/{ident}"


def download_url(version: str) -> str:
    return f"{REPO_HTML}/releases/download/{version}/graph.jsonld"


def _citation(source: dict) -> dict:
    cited = source.get("cited_title") or source.get("url") or source.get("source_id") or ""
    node: dict = {
        "@type": "schema:CreativeWork",
        "schema:url": source.get("url", ""),
        "schema:name": cited,
    }
    if source.get("source_id"):
        node["sota:sourceId"] = source["source_id"]
    return node


def event_node(event: dict) -> dict:
    summary_p1 = str(event["summary_p1"]).strip()
    summary_p2 = str(event["summary_p2"]).strip()
    node: dict = {
        "@id": resource_id("events", event["id"]),
        "@type": "schema:Article",
        "schema:identifier": event["id"],
        "schema:headline": event["title"],
        "schema:datePublished": event["date"],
        "schema:inLanguage": event.get("lang") or "es",
        "schema:abstract": summary_p1,
        "schema:articleBody": f"{summary_p1}\n\n{summary_p2}",
        "sota:type": event["type"],
        "sota:sotaScore": event["sota_score"],
        "sota:aiLegaltech": bool(event["ai_legaltech"]),
    }
    if event.get("why_sota"):
        node["sota:whySota"] = event["why_sota"]
    if event.get("why_now"):
        node["sota:whyNow"] = event["why_now"]
    if event.get("geo"):
        node["sota:geo"] = list(event["geo"])
    if event.get("topics"):
        node["sota:topics"] = list(event["topics"])
    node["sota:summaryP1"] = summary_p1
    node["sota:summaryP2"] = summary_p2
    node["schema:citation"] = [_citation(source) for source in event["sources"] if isinstance(source, dict)]
    entities = [str(item) for item in event.get("entities") or [] if item]
    if entities:
        node["schema:about"] = [{"@id": resource_id("entities", entity_id)} for entity_id in entities]
    return node


def entity_node(entity_id: str) -> dict:
    return {
        "@id": resource_id("entities", entity_id),
        "@type": "schema:Thing",
        "schema:identifier": entity_id,
    }


def assemble_graph(day: date, version: str, events: list[dict]) -> dict:
    event_nodes = [event_node(event) for event in events]
    entity_ids: list[str] = []
    seen: set[str] = set()
    for event in events:
        for entity_id in event.get("entities") or []:
            if entity_id and entity_id not in seen:
                seen.add(entity_id)
                entity_ids.append(str(entity_id))
    entity_ids.sort()
    if day == date(2026, 9, 29):
        description = (
            f"Primera release diaria del grafo Observatorio LegalTech SOTA "
            f"(día {day.isoformat()})."
        )
    else:
        description = (
            f"Release diaria del grafo Observatorio LegalTech SOTA "
            f"(día operativo {day.isoformat()}, {len(events)} eventos)."
        )
    dataset = {
        "@id": resource_id("releases", version),
        "@type": ["schema:Dataset", "schema:CreativeWork"],
        "schema:name": f"{PUBLIC_TITLE} · {version}",
        "schema:version": version,
        "schema:datePublished": day.isoformat(),
        "schema:description": description,
        "schema:inLanguage": "es",
        "schema:url": download_url(version),
        "schema:hasPart": [{"@id": node["@id"]} for node in event_nodes],
    }
    return {
        "@context": {
            "schema": "https://schema.org/",
            "sota": SOTA_NS,
            "xsd": "http://www.w3.org/2001/XMLSchema#",
        },
        "@graph": [dataset, *event_nodes, *[entity_node(entity_id) for entity_id in entity_ids]],
    }


def dump_jsonld(document: dict) -> str:
    return json.dumps(document, ensure_ascii=False, indent=2) + "\n"


def _digest_paths(root: Path, day: date) -> list[Path]:
    iso = day.isoformat()
    candidates = [
        root / "content" / "digests" / "daily" / f"{day.year}" / f"{iso}.md",
        root / "digests" / "daily" / f"{iso}.md",
    ]
    return [path for path in candidates if path.is_file()]


def render_release_notes(day: date, version: str, events: list[dict], root: Path) -> str:
    ai = sum(1 for event in events if event.get("ai_legaltech"))
    digest_lines = []
    canonical = root / "content" / "digests" / "daily" / f"{day.year}" / f"{day.isoformat()}.md"
    if canonical.is_file():
        digest_lines.append(f"| Digest diario | `{canonical.relative_to(root).as_posix()}` |")
    else:
        digest_lines.append("| Digest diario | (sin digest en content/) |")
    rows = "\n".join(
        [
            f"| Grafo JSON-LD del día | `releases/{version}/graph.jsonld` |",
            *digest_lines,
            f"| Eventos | `events/{day.isoformat()}/` |",
            "| Schemas | `schemas/` |",
        ]
    )
    event_lines = []
    for index, event in enumerate(events, start=1):
        title = str(event["title"]).replace("|", "/")
        event_lines.append(
            f"{index}. `{event['id']}` (sota {event['sota_score']}, {event['type']}): {title}"
        )
    events_block = "\n".join(event_lines) if event_lines else "(sin eventos)"
    meaning = f"release del día {day.isoformat()} (Europe/Madrid)."
    return f"""# {PUBLIC_TITLE} · {version}

**Fecha:** {day.isoformat()} (Europe/Madrid)  
**Versión:** `{version}`  
**Significado:** {meaning} La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
{rows}

## Eventos incluidos

{events_block}

**Foco AI LegalTech:** {ai}/{len(events)} eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `{SOTA_NS}` |
| `@id` de la release | `{resource_id("releases", version)}` |
| `@id` de evento | `{REPO_HTML}/events/<evt-id>` |
| `@id` de entidad | `{REPO_HTML}/entities/<ent-id>` |
| Descarga | `{download_url(version)}` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `{LEGACY_NS}` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `{version}`.
- El título público es `{PUBLIC_TITLE} · {version}`.
- El script contrasta la carpeta y el tag `{version}` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: {REPO_HTML}
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.
"""


def _strip_scalar(value: str) -> str:
    return value.strip().strip("'\"").strip()


def _replace_release_stamp(current: str, version: str, force: bool, path: Path) -> bool:
    """Decide si `release:` pasa a la versión de calendario del día."""
    if current == version:
        return False
    if force or current.lower() in PLACEHOLDER_RELEASES or LEGACY_RELEASE_RE.match(current):
        return True
    print(
        f"aviso: {path.as_posix()} ya tiene release: {current}; no se reescribe",
        file=sys.stderr,
    )
    return False


def stamp_frontmatter_release(path: Path, version: str, force: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return False
    match = FRONTMATTER_RE.match(text)
    if not match:
        return False
    frontmatter = match.group(1)
    found = RELEASE_LINE_RE.search(frontmatter)
    replacement = f'release: "{version}"'
    if found:
        current = _strip_scalar(found.group(1))
        if not _replace_release_stamp(current, version, force, path):
            return False
        frontmatter = RELEASE_LINE_RE.sub(replacement, frontmatter, count=1)
    else:
        frontmatter = frontmatter.rstrip() + "\n" + replacement
    new_text = "---\n" + frontmatter + "\n---\n" + text[match.end() :]
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def stamp_index_release(path: Path, version: str, force: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    found = RELEASE_LINE_RE.search(text)
    line = f"release: {version}"
    if found:
        current = _strip_scalar(found.group(1))
        if not _replace_release_stamp(current, version, force, path):
            return False
        new_text = RELEASE_LINE_RE.sub(line, text, count=1)
    else:
        date_line = re.search(r"(?m)^date:.*\n", text)
        if date_line:
            new_text = text[: date_line.end()] + line + "\n" + text[date_line.end() :]
        else:
            new_text = line + "\n" + text
    if new_text == text:
        return False
    path.write_text(new_text, encoding="utf-8")
    return True


def stamp_metadata(root: Path, day: date, version: str, force: bool) -> list[str]:
    stamped: list[str] = []
    for path in _digest_paths(root, day):
        if stamp_frontmatter_release(path, version, force):
            stamped.append(path.relative_to(root).as_posix())
    index = root / "events" / day.isoformat() / "index.yaml"
    if index.is_file() and stamp_index_release(index, version, force):
        stamped.append(index.relative_to(root).as_posix())
    return stamped


def pending_dates(root: Path) -> list[date]:
    events_root = root / "events"
    if not events_root.is_dir():
        return []
    found: list[date] = []
    for path in sorted(events_root.iterdir()):
        if not path.is_dir():
            continue
        try:
            day = parse_day(path.name)
        except ReleaseError:
            continue
        if not event_paths(path):
            continue
        if legacy_release_version(root, day):
            continue
        graph = root / "releases" / version_for_date(day) / "graph.jsonld"
        if not graph.is_file():
            found.append(day)
    return found


def _write_if_changed(path: Path, content: str) -> bool:
    if path.is_file() and path.read_text(encoding="utf-8") == content:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def build_day(
    root: Path,
    day: date,
    *,
    force: bool = False,
    dry_run: bool = False,
    check: bool = False,
) -> BuildResult:
    legacy = legacy_release_version(root, day)
    if legacy is not None:
        folder = root / "releases" / legacy
        return BuildResult(
            day=day,
            version=legacy,
            historical=True,
            graph_path=folder / "graph.jsonld",
            notes_path=folder / "RELEASE.md",
            message=(
                f"{legacy} ({day.isoformat()}) es historica (YY.MM.DD); no se reescribe."
            ),
        )

    version = resolve_version(root, day)
    graph_path = root / "releases" / version / "graph.jsonld"
    notes_path = root / "releases" / version / "RELEASE.md"
    result = BuildResult(day=day, version=version, graph_path=graph_path, notes_path=notes_path)

    if is_historical_graph(graph_path):
        result.historical = True
        result.message = (
            f"{version} ({day.isoformat()}) es historica ({LEGACY_NS}); no se reescribe."
        )
        return result

    events = load_day_events(root, day)
    if not events:
        result.skipped = True
        result.message = f"Sin eventos en events/{day.isoformat()}/. No hay release."
        return result

    types = known_event_types(root)
    if types:
        for event in events:
            if event["type"] not in types:
                print(
                    f"aviso: {event['id']} type={event['type']!r} no esta en event.schema.json",
                    file=sys.stderr,
                )

    document = assemble_graph(day, version, events)
    graph_text = dump_jsonld(document)
    notes_text = render_release_notes(day, version, events, root)
    result.event_count = len(events)

    if LEGACY_NS in graph_text:
        raise ReleaseError("El grafo nuevo aun contiene el namespace local; aborto.")

    if check:
        problems: list[str] = []
        if not graph_path.is_file():
            problems.append(f"falta {graph_path.relative_to(root).as_posix()}")
        elif graph_path.read_text(encoding="utf-8") != graph_text:
            problems.append(f"difiere {graph_path.relative_to(root).as_posix()}")
        if not notes_path.is_file():
            problems.append(f"falta {notes_path.relative_to(root).as_posix()}")
        elif notes_path.read_text(encoding="utf-8") != notes_text:
            problems.append(f"difiere {notes_path.relative_to(root).as_posix()}")
        if problems:
            raise ReleaseError(
                f"check {version} ({day.isoformat()}): " + "; ".join(problems)
            )
        result.message = f"check OK {version} ({day.isoformat()}, {len(events)} eventos)"
        return result

    if dry_run:
        result.changed = not (
            graph_path.is_file()
            and graph_path.read_text(encoding="utf-8") == graph_text
            and notes_path.is_file()
            and notes_path.read_text(encoding="utf-8") == notes_text
        )
        result.message = (
            f"dry-run {version} ({day.isoformat()}, {len(events)} eventos, "
            f"changed={str(result.changed).lower()})"
        )
        return result

    if graph_path.is_file() and not force:
        current_graph = graph_path.read_text(encoding="utf-8")
        current_notes = notes_path.read_text(encoding="utf-8") if notes_path.is_file() else ""
        if current_graph != graph_text or current_notes != notes_text:
            raise ReleaseError(
                f"{version} ya existe y el contenido difiere. Repite con --force para reescribir.",
                code=2,
            )

    changed = _write_if_changed(graph_path, graph_text)
    changed = _write_if_changed(notes_path, notes_text) or changed
    result.stamped = stamp_metadata(root, day, version, force)
    result.changed = changed or bool(result.stamped)
    result.message = (
        f"{version} ({day.isoformat()}, {len(events)} eventos, changed={str(result.changed).lower()})"
    )
    return result


def check_published(root: Path) -> list[BuildResult]:
    releases = root / "releases"
    if not releases.is_dir():
        return []
    results: list[BuildResult] = []
    for path in sorted(releases.iterdir()):
        if not path.is_dir() or not _is_calendar_release_name(path.name):
            continue
        day = notes_date(path / "RELEASE.md")
        if day is None:
            raise ReleaseError(f"{path.name}: RELEASE.md no declara **Fecha:** YYYY-MM-DD")
        current = version_for_date(day)
        legacy = legacy_version_for_date(day)
        if path.name == current:
            parsed = parse_calendar_version(path.name)
            if parsed != day:
                raise ReleaseError(
                    f"{path.name} no coincide con la fecha {day.isoformat()} (esperado {current})"
                )
            results.append(build_day(root, day, check=True))
            continue
        if path.name == legacy:
            parsed = parse_legacy_calendar_version(path.name)
            if parsed != day:
                raise ReleaseError(
                    f"{path.name} no coincide con la fecha historica {day.isoformat()}"
                )
            results.append(
                BuildResult(
                    day=day,
                    version=path.name,
                    historical=True,
                    graph_path=path / "graph.jsonld",
                    notes_path=path / "RELEASE.md",
                    message=(
                        f"{path.name} ({day.isoformat()}) es historica (YY.MM.DD); "
                        "no se reescribe."
                    ),
                )
            )
            continue
        raise ReleaseError(
            f"{path.name} no coincide con la fecha {day.isoformat()} "
            f"(esperado {current}; historico {legacy})"
        )
    return results


def append_github_output(path: Path, result: BuildResult) -> None:
    lines = [
        f"version={result.version}",
        f"date={result.day.isoformat()}",
        f"skipped={str(result.skipped).lower()}",
        f"changed={str(result.changed).lower()}",
        f"historical={str(result.historical).lower()}",
        f"event_count={result.event_count}",
    ]
    if result.graph_path is not None:
        lines.append(f"graph={result.graph_path.as_posix()}")
    if result.notes_path is not None:
        lines.append(f"notes={result.notes_path.as_posix()}")
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def _print_result(result: BuildResult) -> None:
    print(result.message)
    print(f"RELEASE_VERSION={result.version}")
    print(f"RELEASE_DATE={result.day.isoformat()}")
    print(f"RELEASE_SKIPPED={str(result.skipped).lower()}")
    print(f"RELEASE_CHANGED={str(result.changed).lower()}")
    print(f"RELEASE_HISTORICAL={str(result.historical).lower()}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Empaqueta events/ de un dia Madrid en releases/<DD.MM.YY>/."
    )
    parser.add_argument("--root", type=Path, default=ROOT, help="Raiz del repo")
    parser.add_argument("--date", help="Fecha editorial Europe/Madrid YYYY-MM-DD")
    parser.add_argument(
        "--pending",
        action="store_true",
        help="Construye cada events/YYYY-MM-DD que aun no tiene releases/DD.MM.YY/",
    )
    parser.add_argument(
        "--list-pending",
        action="store_true",
        help="Lista fechas pendientes, una por linea, y termina",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Compara el grafo en disco con la salida del script (no escribe)",
    )
    parser.add_argument(
        "--check-published",
        action="store_true",
        help="Hace --check de cada release segun la fecha de RELEASE.md",
    )
    parser.add_argument("--dry-run", action="store_true", help="No escribe ficheros")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Reescribe una release ya generada por este script si el texto difiere",
    )
    parser.add_argument(
        "--github-output",
        type=Path,
        help="Ruta tipo GITHUB_OUTPUT donde anexar version= y date=",
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()

    try:
        if args.list_pending:
            for day in pending_dates(root):
                print(day.isoformat())
            return 0

        if args.check_published:
            results = check_published(root)
            if not results:
                print("No hay releases publicadas en el arbol.")
            for result in results:
                _print_result(result)
            return 0

        if args.pending:
            days = pending_dates(root)
            if not days:
                print("No hay dias operativos pendientes.")
                return 0
        elif args.date:
            days = [parse_day(args.date)]
        else:
            parser.error("indica --date, --pending, --list-pending o --check-published")
            return 2

        exit_code = 0
        for day in days:
            result = build_day(
                root,
                day,
                force=args.force,
                dry_run=args.dry_run,
                check=args.check,
            )
            _print_result(result)
            if args.github_output:
                append_github_output(args.github_output, result)
            if result.skipped and args.date and not args.pending:
                # Un dia explicito sin eventos es un skip limpio (el cron no debe fallar).
                exit_code = 0
        return exit_code
    except ReleaseError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return exc.code


if __name__ == "__main__":
    raise SystemExit(main())

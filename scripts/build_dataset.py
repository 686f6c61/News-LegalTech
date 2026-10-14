#!/usr/bin/env python3
"""Dataset acumulado y append-only de todas las pasadas diarias.

Lee cada ``events/YYYY-MM-DD/`` y reconstruye en ``data/``:

- ``events.jsonl``: un evento por línea, todos los días, orden (fecha, índice del día).
- ``events.csv``: mismas filas en columnas planas (listas separadas por ``|``).
- ``graph.jsonld``: grafo JSON-LD acumulado (eventos + entidades citadas).
- ``days.json``: recuento de eventos por día y total.
- ``ledger.json``: registro append-only ``día -> [event ids]``. Una vez un id
  entra en el ledger no puede desaparecer de ``events/``: ``--check`` falla.

Dedupe por ``id`` de evento: un id repetido entre días es un error.

Uso:
  python scripts/build_dataset.py            # reconstruye data/ y amplía el ledger
  python scripts/build_dataset.py --check    # falla si data/ no coincide o falta un id del ledger
"""

from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_release as br  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CSV_FIELDS = [
    "id", "day", "date", "type", "piece_type", "topic", "country", "sota_score",
    "ai_legaltech", "vendor_source", "paywalled", "guidance_not_norm", "title",
    "short_title", "standfirst", "summary_p1", "summary_p2", "geo", "topics",
    "source_ids", "source_urls", "entities", "status",
]


class DatasetError(Exception):
    pass


def event_days(root: Path) -> list[date]:
    days = []
    base = root / "events"
    if not base.is_dir():
        return days
    for path in sorted(base.iterdir()):
        if path.is_dir():
            try:
                days.append(date.fromisoformat(path.name))
            except ValueError:
                continue
    return days


def collect(root: Path) -> list[tuple[str, dict]]:
    rows: list[tuple[str, dict]] = []
    seen: dict[str, str] = {}
    for day in event_days(root):
        for event in br.load_day_events(root, day):
            eid = event["id"]
            if not eid.startswith(f"evt-{day.isoformat()}-"):
                raise DatasetError(f"{eid} no lleva el prefijo de su carpeta {day.isoformat()}")
            if eid in seen:
                raise DatasetError(f"id duplicado {eid} en {seen[eid]} y {day.isoformat()}")
            seen[eid] = day.isoformat()
            rows.append((day.isoformat(), event))
    return rows


def _flat(value) -> str:
    if isinstance(value, list):
        return "|".join(str(v) for v in value)
    if isinstance(value, bool):
        return "true" if value else "false"
    return "" if value is None else str(value)


def render(root: Path, rows: list[tuple[str, dict]]) -> dict[str, str]:
    jsonl = "".join(
        json.dumps({"day": day, **event}, ensure_ascii=False, sort_keys=False) + "\n"
        for day, event in rows
    )
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=CSV_FIELDS, lineterminator="\n")
    writer.writeheader()
    for day, event in rows:
        sources = [s for s in event.get("sources") or [] if isinstance(s, dict)]
        record = {k: _flat(event.get(k)) for k in CSV_FIELDS}
        record["day"] = day
        record["source_ids"] = _flat([s.get("source_id", "") for s in sources])
        record["source_urls"] = _flat([s.get("url", "") for s in sources])
        writer.writerow(record)

    entity_records = br.load_entity_records(root)
    event_nodes = [br.event_node(event) for _day, event in rows]
    entity_ids = sorted({str(e) for _d, ev in rows for e in ev.get("entities") or [] if e})
    days = sorted({day for day, _ in rows})
    graph = {
        "@context": {"schema": "https://schema.org/", "sota": br.SOTA_NS,
                     "xsd": "http://www.w3.org/2001/XMLSchema#"},
        "@graph": [
            {
                "@id": br.resource_id("data", "graph.jsonld"),
                "@type": ["schema:Dataset", "schema:CreativeWork"],
                "schema:name": f"{br.PUBLIC_TITLE} · acumulado",
                "schema:description": (
                    f"Grafo acumulado de todas las pasadas diarias "
                    f"({days[0] if days else '-'} → {days[-1] if days else '-'}, {len(rows)} eventos)."
                ),
                "schema:temporalCoverage": f"{days[0]}/{days[-1]}" if days else "",
                "schema:inLanguage": "es",
                "schema:license": "https://spdx.org/licenses/MIT.html",
                "schema:hasPart": [{"@id": n["@id"]} for n in event_nodes],
            },
            *event_nodes,
            *[br.entity_node(e, entity_records.get(e)) for e in entity_ids],
        ],
    }
    counts: dict[str, int] = {}
    for day, _ in rows:
        counts[day] = counts.get(day, 0) + 1
    days_doc = {"days": len(counts), "events": len(rows), "per_day": counts}
    return {
        "events.jsonl": jsonl,
        "events.csv": buf.getvalue(),
        "graph.jsonld": br.dump_jsonld(graph),
        "days.json": json.dumps(days_doc, ensure_ascii=False, indent=2) + "\n",
    }


def load_ledger(root: Path) -> dict[str, list[str]]:
    path = root / "data" / "ledger.json"
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def ledger_problems(ledger: dict[str, list[str]], rows: list[tuple[str, dict]]) -> list[str]:
    present = {(day, ev["id"]) for day, ev in rows}
    return [f"{day}: falta {eid} (estaba publicado)" for day, ids in sorted(ledger.items())
            for eid in ids if (day, eid) not in present]


def merged_ledger(ledger: dict[str, list[str]], rows: list[tuple[str, dict]]) -> dict[str, list[str]]:
    out = {day: list(ids) for day, ids in ledger.items()}
    for day, ev in rows:
        ids = out.setdefault(day, [])
        if ev["id"] not in ids:
            ids.append(ev["id"])
    return dict(sorted(out.items()))


def run(root: Path, check: bool = False) -> dict:
    rows = collect(root)
    ledger = load_ledger(root)
    problems = ledger_problems(ledger, rows)
    if problems:
        raise DatasetError("Eventos publicados desaparecidos: " + "; ".join(problems))
    outputs = render(root, rows)
    new_ledger = merged_ledger(ledger, rows)
    outputs["ledger.json"] = json.dumps(new_ledger, ensure_ascii=False, indent=2) + "\n"
    data = root / "data"
    if check:
        diffs = [name for name, text in outputs.items()
                 if not (data / name).is_file() or (data / name).read_text(encoding="utf-8") != text]
        if diffs:
            raise DatasetError("data/ desactualizado: " + ", ".join(diffs)
                               + ". Ejecuta python scripts/build_dataset.py")
    else:
        data.mkdir(exist_ok=True)
        for name, text in outputs.items():
            (data / name).write_text(text, encoding="utf-8")
    return json.loads(outputs["days.json"])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        summary = run(args.root.resolve(), check=args.check)
    except (DatasetError, br.ReleaseError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"dataset {'OK' if args.check else 'escrito'}: {summary['days']} días, {summary['events']} eventos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

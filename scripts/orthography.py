#!/usr/bin/env python3
"""Ortografía española en UTF-8 para eventos, digests y releases.

Los ficheros se leen y se escriben en UTF-8. El grafo JSON-LD sale con
``json.dumps(..., ensure_ascii=False)``: la ñ y las tildes viajan como
caracteres, no como escapes ``\\uXXXX``.

La regla de comillas ASCII no aplana el español. ``--check`` falla si el
prosa reciente vuelve a formas como ``senalar`` o ``pagina``.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Formas que no son español válido ni inglés. Si aparecen en prosa, el texto
# perdió la tilde o la eñe.
_DENY = (
    "soberania",
    "senalar",
    "senal",
    "senales",
    "paragrafos",
    "paragrafo",
    "tambien",
    "despues",
    "ademas",
    "todavia",
    "espanol",
    "espanola",
    "espanoles",
    "espanolas",
    "espana",
    "pagina",
    "paginas",
    "analisis",
    "juridico",
    "juridica",
    "juridicos",
    "juridicas",
    "juridicamente",
    "articulo",
    "articulos",
    "informacion",
    "anade",
    "diseno",
    "disenar",
    "disenado",
    "redisenar",
    "garantia",
    "garantias",
)

# Inglés real que termina en -sion y no debe acentuarse.
_ENGLISH_SION = {
    "session",
    "commission",
    "passion",
    "mission",
    "permission",
    "submission",
    "transmission",
    "discussion",
    "concession",
    "profession",
    "compression",
    "pension",
}

# Palabra plana -> forma acentuada. No incluye verbos/determinantes ambiguos
# (esta, si, solo, que, como, donde, cuando, quien).
_WORDS = {
    "abogacia": "abogacía",
    "academica": "académica",
    "academico": "académico",
    "accedio": "accedió",
    "ademas": "además",
    "africa": "áfrica",
    "agentica": "agéntica",
    "agenticas": "agénticas",
    "agentico": "agéntico",
    "agenticos": "agénticos",
    "algun": "algún",
    "alli": "allí",
    "analisis": "análisis",
    "anade": "añade",
    "anadir": "añadir",
    "anglosajon": "anglosajón",
    "angulo": "ángulo",
    "ano": "año",
    "anos": "años",
    "aporto": "aportó",
    "aqui": "aquí",
    "arabe": "árabe",
    "arabes": "árabes",
    "arabigo": "arábigo",
    "arbitro": "árbitro",
    "arbitros": "árbitros",
    "articulo": "artículo",
    "articulos": "artículos",
    "asi": "así",
    "aun": "aún",
    "automatica": "automática",
    "automaticamente": "automáticamente",
    "automatico": "automático",
    "autonomia": "autonomía",
    "autonomo": "autónomo",
    "autonomos": "autónomos",
    "ayudo": "ayudó",
    "basica": "básica",
    "basicas": "básicas",
    "basico": "básico",
    "basicos": "básicos",
    "bilingue": "bilingüe",
    "britanica": "británica",
    "britanico": "británico",
    "busco": "buscó",
    "busqueda": "búsqueda",
    "busquedas": "búsquedas",
    "caracter": "carácter",
    "catalogo": "catálogo",
    "catalogos": "catálogos",
    "categoria": "categoría",
    "categorias": "categorías",
    "codigo": "código",
    "codigos": "códigos",
    "comite": "comité",
    "comites": "comités",
    "comun": "común",
    "compania": "compañía",
    "companias": "compañías",
    "condeno": "condenó",
    "confirmo": "confirmó",
    "construyo": "construyó",
    "critica": "crítica",
    "criticas": "críticas",
    "critico": "crítico",
    "cubrio": "cubrió",
    "curriculum": "currículum",
    "curriculums": "currículums",
    "debera": "deberá",
    "deberia": "debería",
    "debil": "débil",
    "debiles": "débiles",
    "decidio": "decidió",
    "declaro": "declaró",
    "demas": "demás",
    "deberias": "deberías",
    "despues": "después",
    "dia": "día",
    "dias": "días",
    "diagnostico": "diagnóstico",
    "dificil": "difícil",
    "disenado": "diseñado",
    "disenar": "diseñar",
    "diseno": "diseño",
    "dolar": "dólar",
    "dolares": "dólares",
    "economica": "económica",
    "economicas": "económicas",
    "economico": "económico",
    "economicos": "económicos",
    "ejecuto": "ejecutó",
    "energia": "energía",
    "energetica": "energética",
    "energetico": "energético",
    "enfasis": "énfasis",
    "especificamente": "específicamente",
    "etica": "ética",
    "eticas": "éticas",
    "etico": "ético",
    "eticos": "éticos",
    "espana": "españa",
    "espanol": "español",
    "espanola": "española",
    "espanolas": "españolas",
    "espanoles": "españoles",
    "especifica": "específica",
    "especificas": "específicas",
    "especifico": "específico",
    "especificos": "específicos",
    "estandar": "estándar",
    "estandares": "estándares",
    "exploro": "exploró",
    "facil": "fácil",
    "ficho": "fichó",
    "firmo": "firmó",
    "formula": "fórmula",
    "formulas": "fórmulas",
    "fisica": "física",
    "fisico": "físico",
    "garantia": "garantía",
    "garantias": "garantías",
    "generica": "genérica",
    "generico": "genérico",
    "gestion": "gestión",
    "geografica": "geográfica",
    "geografico": "geográfico",
    "geografia": "geografía",
    "guia": "guía",
    "guias": "guías",
    "habia": "había",
    "habian": "habían",
    "habria": "habría",
    "hibrida": "híbrida",
    "hibrido": "híbrido",
    "historica": "histórica",
    "historico": "histórico",
    "impedian": "impedían",
    "indice": "índice",
    "indices": "índices",
    "ingles": "inglés",
    "interes": "interés",
    "jovenes": "jóvenes",
    "juridica": "jurídica",
    "juridicas": "jurídicas",
    "juridicamente": "jurídicamente",
    "juridico": "jurídico",
    "juridicos": "jurídicos",
    "lanzo": "lanzó",
    "lider": "líder",
    "lideres": "líderes",
    "limite": "límite",
    "limites": "límites",
    "linea": "línea",
    "lineas": "líneas",
    "liston": "listón",
    "logica": "lógica",
    "logico": "lógico",
    "mas": "más",
    "maxima": "máxima",
    "maximo": "máximo",
    "mayoria": "mayoría",
    "metodo": "método",
    "metodos": "métodos",
    "metodologia": "metodología",
    "metrica": "métrica",
    "metricas": "métricas",
    "mexico": "méxico",
    "millon": "millón",
    "minima": "mínima",
    "minimo": "mínimo",
    "modifico": "modificó",
    "ningun": "ningún",
    "nucleo": "núcleo",
    "numero": "número",
    "numeros": "números",
    "ordenes": "órdenes",
    "organo": "órgano",
    "organos": "órganos",
    "optima": "óptima",
    "optimo": "óptimo",
    "pagina": "página",
    "paginas": "páginas",
    "pais": "país",
    "paises": "países",
    "paragrafo": "párrafo",
    "paragrafos": "párrafos",
    "patron": "patrón",
    "pequena": "pequeña",
    "pequenas": "pequeñas",
    "pequeno": "pequeño",
    "pequenos": "pequeños",
    "perez": "pérez",
    "periodo": "período",
    "periodos": "períodos",
    "pediran": "pedirán",
    "podra": "podrá",
    "podria": "podría",
    "podrian": "podrían",
    "politica": "política",
    "politicas": "políticas",
    "politico": "político",
    "politicos": "políticos",
    "practicas": "prácticas",
    "prohibe": "prohíbe",
    "prohiben": "prohíben",
    "practico": "práctico",
    "presento": "presentó",
    "proposito": "propósito",
    "proxima": "próxima",
    "proximas": "próximas",
    "proximo": "próximo",
    "proximos": "próximos",
    "publicas": "públicas",
    "publicos": "públicos",
    "rapida": "rápida",
    "rapidas": "rápidas",
    "rapido": "rápido",
    "recibio": "recibió",
    "redisenar": "rediseñar",
    "regimen": "régimen",
    "segun": "según",
    "senal": "señal",
    "senalar": "señalar",
    "senales": "señales",
    "sera": "será",
    "seria": "sería",
    "serian": "serían",
    "sintetica": "sintética",
    "soberania": "soberanía",
    "sinteticos": "sintéticos",
    "sintetico": "sintético",
    "sistematica": "sistemática",
    "sistematico": "sistemático",
    "tambien": "también",
    "tecnica": "técnica",
    "tecnicas": "técnicas",
    "tecnico": "técnico",
    "tecnicos": "técnicos",
    "tecnologia": "tecnología",
    "tecnologias": "tecnologías",
    "termometro": "termómetro",
    "tendra": "tendrá",
    "tendria": "tendría",
    "teoria": "teoría",
    "terminologia": "terminología",
    "terminos": "términos",
    "titulo": "título",
    "titulos": "títulos",
    "todavia": "todavía",
    "ultima": "última",
    "ultimas": "últimas",
    "ultimo": "último",
    "ultimos": "últimos",
    "unica": "única",
    "unicas": "únicas",
    "unico": "único",
    "unicos": "únicos",
    "util": "útil",
    "utiles": "útiles",
    "via": "vía",
}

_WORD_RE = re.compile(
    r"\b(?:" + "|".join(re.escape(key) for key in sorted(_WORDS, key=len, reverse=True)) + r")\b",
    re.IGNORECASE,
)
_CION_RE = re.compile(r"\b[A-Za-z]+(?:cion|sion)\b", re.IGNORECASE)
_SPANISH_CUE = re.compile(
    r"\b(?:el|la|los|las|del|al|una|unos|unas|que|para|con|por|en|su|es|un|de|se|lo|como)\b",
    re.IGNORECASE,
)
_ENGLISH_QUOTE_CUE = re.compile(
    r"\b(?:the|of|and|is|for|to|in|with|from|on|by|or|be|this|that|your|why|how)\b",
    re.IGNORECASE,
)
_URL_RE = re.compile(r"https?://[^\s)>\]]+")
_CODE_RE = re.compile(r"`[^`]*`")
_ID_RE = re.compile(r"\b(?:evt|ent|src)-[A-Za-z0-9-]+\b")
_ESTA_RE = re.compile(r"\b(esta)\s+(\w+)", re.IGNORECASE)
_ESTA_VERB_NEXT = {
    "aqui",
    "aquí",
    "en",
    "por",
    "claro",
    "clara",
    "listo",
    "lista",
}
_EVENT_PROSE = ("title", "summary_p1", "summary_p2", "why_sota", "why_now")
_JSONLD_PROSE = {
    "schema:headline",
    "schema:abstract",
    "schema:articleBody",
    "schema:description",
    "sota:summaryP1",
    "sota:summaryP2",
    "sota:whySota",
    "sota:whyNow",
}
_RECENT_DATES = ("2026-09-29", "2026-09-30", "2026-10-01", "2026-10-02")
_RECENT_RELEASES = ("26.09.29", "26.09.30", "26.10.01", "02.10.26")


def _apply_case(source: str, target: str) -> str:
    if source.isupper():
        return target.upper()
    if source[:1].isupper():
        return target[:1].upper() + target[1:]
    return target


def _strip_unscanned(text: str) -> str:
    text = _URL_RE.sub(" ", text)
    text = _CODE_RE.sub(" ", text)
    text = _ID_RE.sub(" ", text)
    return text


def folded_tokens(text: str) -> list[str]:
    """Devuelve formas planas inequívocas (``senalar``, ``pagina``, ``-cion``)."""
    cleaned = _strip_unscanned(text)
    found: list[str] = []
    seen: set[str] = set()
    for token in _DENY:
        if re.search(rf"\b{token}\b", cleaned, flags=re.IGNORECASE):
            if token not in seen:
                seen.add(token)
                found.append(token)
    for match in _CION_RE.finditer(cleaned):
        word = match.group(0).lower()
        if word in _ENGLISH_SION or word in seen:
            continue
        seen.add(word)
        found.append(word)
    return found


def spanish_cue(text: str) -> bool:
    return _SPANISH_CUE.search(text) is not None


def _protect(text: str) -> tuple[str, list[str]]:
    saved: list[str] = []

    def keep(match: re.Match[str]) -> str:
        saved.append(match.group(0))
        return f"\x00{len(saved) - 1}\x00"

    def keep_english_quote(match: re.Match[str]) -> str:
        inner = match.group(1)
        deny = any(re.search(rf"\b{token}\b", inner, flags=re.IGNORECASE) for token in _DENY)
        if spanish_cue(inner) or _WORD_RE.search(inner) or deny:
            return match.group(0)
        if _ENGLISH_QUOTE_CUE.search(inner):
            return keep(match)
        return match.group(0)

    # Las citas en inglés se guardan enteras, URL incluida, antes de enmascarar URLs.
    text = re.sub(r'"([^"\n]*)"', keep_english_quote, text)
    text = _URL_RE.sub(keep, text)
    text = _CODE_RE.sub(keep, text)
    text = _ID_RE.sub(keep, text)
    return text, saved


def _unprotect(text: str, saved: list[str]) -> str:
    for index in range(len(saved) - 1, -1, -1):
        text = text.replace(f"\x00{index}\x00", saved[index])
    return text


def _replace_words(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        return _apply_case(match.group(0), _WORDS[match.group(0).lower()])

    return _WORD_RE.sub(repl, text)


def _replace_cion(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        word = match.group(0)
        lower = word.lower()
        if lower in _ENGLISH_SION:
            return word
        if lower.endswith("cion"):
            target = lower[:-4] + "ción"
        else:
            target = lower[:-4] + "sión"
        return _apply_case(word, target)

    return _CION_RE.sub(repl, text)


def _replace_contextual(text: str) -> str:
    text = re.sub(
        r"\banuncio(?=\s+(?:el|que|en|la|los|las|un|una|su)\b)",
        lambda match: _apply_case(match.group(0), "anunció"),
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\bpublico(?=\s+(?:el|la|los|las|un|una|guias|guías)\b)",
        lambda match: _apply_case(match.group(0), "publicó"),
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\b(hecho|el|del|al|Bench)\s+publico\b",
        lambda match: f"{match.group(1)} {_apply_case('publico', 'público')}",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\bno publica\b",
        lambda match: _apply_case(match.group(0), "no pública"),
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(\d+\s*%)\s+si\b",
        lambda match: f"{match.group(1)} sí",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"(\d+\s*%)\s+uso\b",
        lambda match: f"{match.group(1)} usó",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\bpaso(?=\s+del\b)",
        lambda match: _apply_case(match.group(0), "pasó"),
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\binicio(?=\s+sesion\b)",
        lambda match: _apply_case(match.group(0), "inició"),
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\brechazo(?=\s+el\b)",
        lambda match: _apply_case(match.group(0), "rechazó"),
        text,
        flags=re.IGNORECASE,
    )

    def esta_repl(match: re.Match[str]) -> str:
        word, nxt = match.group(1), match.group(2)
        nxt_key = nxt.lower()
        verbish = (
            nxt_key in _ESTA_VERB_NEXT
            or nxt_key.endswith(("ando", "endo", "iendo", "ado", "ados", "ido", "idos"))
        )
        if not verbish:
            return match.group(0)
        return f"{_apply_case(word, 'está')} {nxt}"

    return _ESTA_RE.sub(esta_repl, text)


def restore_prose(text: str) -> str:
    """Repone ñ y tildes en prosa española. No toca URLs, ids ni citas en inglés."""
    if not text:
        return text
    protected, saved = _protect(text)
    protected = _replace_contextual(protected)
    protected = _replace_words(protected)
    protected = _replace_cion(protected)
    return _unprotect(protected, saved)


def restore_event(event: dict) -> dict:
    for key in _EVENT_PROSE:
        value = event.get(key)
        if isinstance(value, str):
            event[key] = restore_prose(value)
    for source in event.get("sources") or []:
        if not isinstance(source, dict):
            continue
        cited = source.get("cited_title")
        if isinstance(cited, str) and (spanish_cue(cited) or folded_tokens(cited)):
            source["cited_title"] = restore_prose(cited)
    return event


def restore_jsonld(document: dict) -> dict:
    def walk(node: object) -> None:
        if isinstance(node, dict):
            for key, value in list(node.items()):
                if isinstance(value, str) and key in _JSONLD_PROSE:
                    node[key] = restore_prose(value)
                elif isinstance(value, str) and key == "schema:name":
                    if spanish_cue(value) or folded_tokens(value):
                        node[key] = restore_prose(value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    walk(document)
    return document


def _dump_json(document: dict) -> str:
    return json.dumps(document, ensure_ascii=False, indent=2) + "\n"


def recent_problem_paths(root: Path) -> list[tuple[Path, list[str]]]:
    """Problemas de ortografía en el corpus reciente (29 sep–2 oct 2026)."""
    problems: list[tuple[Path, list[str]]] = []

    def add(path: Path, tokens: list[str]) -> None:
        if tokens:
            problems.append((path, tokens))

    for day in _RECENT_DATES:
        day_dir = root / "events" / day
        if not day_dir.is_dir():
            continue
        for path in sorted(day_dir.glob("evt-*.json")):
            event = json.loads(path.read_text(encoding="utf-8"))
            blobs = [event.get(key, "") for key in _EVENT_PROSE]
            for source in event.get("sources") or []:
                if isinstance(source, dict) and isinstance(source.get("cited_title"), str):
                    cited = source["cited_title"]
                    if spanish_cue(cited):
                        blobs.append(cited)
            add(path, folded_tokens("\n".join(str(item) for item in blobs)))
        index = day_dir / "index.yaml"
        if index.is_file():
            add(index, folded_tokens(index.read_text(encoding="utf-8")))

    digest_paths = []
    for day in _RECENT_DATES:
        digest_paths.append(root / "digests" / "daily" / f"{day}.md")
        digest_paths.append(root / "content" / "digests" / "daily" / day[:4] / f"{day}.md")
    for path in digest_paths:
        if path.is_file():
            add(path, folded_tokens(path.read_text(encoding="utf-8")))

    for version in _RECENT_RELEASES:
        folder = root / "releases" / version
        notes = folder / "RELEASE.md"
        graph = folder / "graph.jsonld"
        if notes.is_file():
            add(notes, folded_tokens(notes.read_text(encoding="utf-8")))
        if graph.is_file():
            document = json.loads(graph.read_text(encoding="utf-8"))
            blobs: list[str] = []

            def collect(node: object) -> None:
                if isinstance(node, dict):
                    for key, value in node.items():
                        if isinstance(value, str) and (
                            key in _JSONLD_PROSE or (key == "schema:name" and spanish_cue(value))
                        ):
                            blobs.append(value)
                        else:
                            collect(value)
                elif isinstance(node, list):
                    for item in node:
                        collect(item)

            collect(document)
            add(graph, folded_tokens("\n".join(blobs)))
    return problems


def apply_recent(root: Path) -> list[Path]:
    """Restaura prosa reciente. No reescribe slugs, ids ni la release ``02.10.26``."""
    changed: list[Path] = []

    def write_if_needed(path: Path, content: str) -> None:
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current == content:
            return
        path.write_text(content, encoding="utf-8")
        changed.append(path)

    for day in _RECENT_DATES:
        day_dir = root / "events" / day
        if not day_dir.is_dir():
            continue
        for path in sorted(day_dir.glob("evt-*.json")):
            event = json.loads(path.read_text(encoding="utf-8"))
            restore_event(event)
            write_if_needed(path, _dump_json(event))
        index = day_dir / "index.yaml"
        if index.is_file():
            write_if_needed(index, restore_prose(index.read_text(encoding="utf-8")))
        for path in (
            root / "digests" / "daily" / f"{day}.md",
            root / "content" / "digests" / "daily" / day[:4] / f"{day}.md",
        ):
            if path.is_file():
                write_if_needed(path, restore_prose(path.read_text(encoding="utf-8")))

    for version in ("26.09.29", "26.09.30", "26.10.01"):
        folder = root / "releases" / version
        notes = folder / "RELEASE.md"
        graph = folder / "graph.jsonld"
        if notes.is_file():
            write_if_needed(notes, restore_prose(notes.read_text(encoding="utf-8")))
        if graph.is_file():
            document = json.loads(graph.read_text(encoding="utf-8"))
            restore_jsonld(document)
            write_if_needed(graph, _dump_json(document))
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Comprueba la ortografía española del corpus reciente.")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true", help="Falla si hay formas como senalar o pagina")
    args = parser.parse_args(argv)
    if not args.check:
        parser.error("indica --check")
    problems = recent_problem_paths(args.root.resolve())
    if not problems:
        print("ortografia: OK")
        return 0
    for path, tokens in problems:
        rel = path.relative_to(args.root.resolve())
        print(f"{rel}: {', '.join(tokens)}", file=sys.stderr)
    print(f"ERROR: {len(problems)} ficheros con español sin tilde o sin eñe", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

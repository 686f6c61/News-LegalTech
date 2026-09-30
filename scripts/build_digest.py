#!/usr/bin/env python3
"""Stub: rollup daily -> weekly -> biweekly digests.

Documenta el flujo previsto. No escribe ficheros todavia (salvo --dry-run info).

Uso:
  python scripts/build_digest.py --cadence daily --date 2026-09-29
  python scripts/build_digest.py --cadence weekly --date 2026-09-29
  python scripts/build_digest.py --cadence biweekly --date 2026-09-29

Rollup previsto
---------------
1. daily
   - Lee events/YYYY-MM-DD/*.yaml (+ index.yaml)
   - Emite content/digests/daily/YYYY/YYYY-MM-DD.md con frontmatter
     (title, date, cadence=daily, release, lang, focus_ai_pct, event_ids)
   - Cuerpo: impacto narrativo en dos parrafos por evento (regla editorial)

2. weekly
   - Agrupa digests daily de la semana ISO que contiene --date
   - Emite content/digests/weekly/YYYY/YYYY-Www.md (o YYYY-MM-DD fin de semana)
   - Frontmatter cadence=weekly; event_ids = union de los daily
   - Cuerpo: senales SOTA de la semana + impacto de negocio agregado

3. biweekly
   - Agrupa dos semanas ISO (o 14 dias cerrados en --date)
   - Emite content/digests/biweekly/YYYY/...
   - Frontmatter cadence=biweekly; event_ids = union del periodo
   - Cuerpo: tendencias, releases y foco AI (~focus_ai_pct)

Release JSON-LD (releases/X.Y.Z/) la construye scripts/build_release.py.
Este stub solo planifica el rollup Markdown de content/ y no escribe ficheros.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content" / "digests"


def parse_date(s: str) -> date:
    return datetime.strptime(s, "%Y-%m-%d").date()


def iso_week_id(d: date) -> str:
    iso = d.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def daily_path(d: date) -> Path:
    return CONTENT / "daily" / f"{d.year}" / f"{d.isoformat()}.md"


def weekly_path(d: date) -> Path:
    return CONTENT / "weekly" / f"{d.year}" / f"{iso_week_id(d)}.md"


def biweekly_path(d: date) -> Path:
    # Periodo: dos semanas ISO que terminan en la semana de d
    return CONTENT / "biweekly" / f"{d.year}" / f"{iso_week_id(d)}-bi.md"


def plan_daily(d: date) -> dict:
    events_dir = ROOT / "events" / d.isoformat()
    return {
        "cadence": "daily",
        "out": str(daily_path(d)),
        "inputs": [str(events_dir)] if events_dir.exists() else [],
        "note": "Narrativa por evento; frontmatter event_ids desde events/*/index.yaml",
    }


def plan_weekly(d: date) -> dict:
    # Lunes de la semana ISO -> Domingo
    iso = d.isocalendar()
    monday = date.fromisocalendar(iso.year, iso.week, 1)
    days = [monday + timedelta(days=i) for i in range(7)]
    inputs = [str(daily_path(x)) for x in days]
    return {
        "cadence": "weekly",
        "out": str(weekly_path(d)),
        "inputs": inputs,
        "note": "Union de event_ids de daily existentes; resumen SOTA semanal",
    }


def plan_biweekly(d: date) -> dict:
    iso = d.isocalendar()
    # Semana actual y anterior
    this_monday = date.fromisocalendar(iso.year, iso.week, 1)
    prev_monday = this_monday - timedelta(days=7)
    weeks = [prev_monday, this_monday]
    inputs = [str(weekly_path(w)) for w in weeks]
    inputs += [str(daily_path(prev_monday + timedelta(days=i))) for i in range(14)]
    return {
        "cadence": "biweekly",
        "out": str(biweekly_path(d)),
        "inputs": inputs,
        "note": "Prefiere weekly si existen; si no, agrega daily del periodo de 14 dias",
    }


PLANNERS = {
    "daily": plan_daily,
    "weekly": plan_weekly,
    "biweekly": plan_biweekly,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Stub rollup digests daily -> weekly -> biweekly (no write)."
    )
    parser.add_argument(
        "--cadence",
        choices=["daily", "weekly", "biweekly"],
        required=True,
        help="Cadencia de salida",
    )
    parser.add_argument(
        "--date",
        required=True,
        help="Fecha ancla YYYY-MM-DD (Europe/Madrid editorial)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Solo imprime el plan (default; escritura no implementada)",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Reservado: escribir Markdown (aun no implementado)",
    )
    args = parser.parse_args(argv)

    d = parse_date(args.date)
    plan = PLANNERS[args.cadence](d)

    print(f"cadence: {plan['cadence']}")
    print(f"date:    {d.isoformat()}")
    print(f"out:     {plan['out']}")
    print(f"note:    {plan['note']}")
    print("inputs:")
    for p in plan["inputs"]:
        exists = Path(p).exists()
        print(f"  - {'OK' if exists else 'MISSING'}: {p}")

    if args.write:
        print(
            "ERROR: --write aun no implementado; stub documental solamente.",
            file=sys.stderr,
        )
        return 2

    print("dry-run: OK (stub; no se escribieron ficheros)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

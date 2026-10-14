#!/usr/bin/env python3
"""Pruebas del dataset acumulado: append-only, dedupe por id y árbol real."""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_dataset as bd  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def _event(day: str, slug: str) -> dict:
    return {
        "id": f"evt-{day}-{slug}", "date": day, "type": "product", "sota_score": 7.0,
        "ai_legaltech": True, "title": f"Producto de prueba {slug}",
        "summary_p1": "Idea clave del producto de prueba con longitud suficiente.",
        "summary_p2": "Impacto de negocio del producto de prueba con longitud suficiente.",
        "sources": [{"source_id": "src-demo", "url": "https://demo.example/a"}],
        "entities": [], "lang": "es", "status": "published",
    }


def _write(root: Path, day: str, slug: str) -> Path:
    d = root / "events" / day
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"evt-{day}-{slug}.json"
    path.write_text(json.dumps(_event(day, slug), ensure_ascii=False), encoding="utf-8")
    return path


class DatasetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def test_accumulates_all_days(self) -> None:
        _write(self.tmp, "2026-10-01", "a")
        _write(self.tmp, "2026-10-02", "b")
        summary = bd.run(self.tmp)
        self.assertEqual(summary["days"], 2)
        self.assertEqual(summary["events"], 2)
        _write(self.tmp, "2026-10-03", "c")
        summary = bd.run(self.tmp)
        self.assertEqual(summary["events"], 3)
        lines = (self.tmp / "data" / "events.jsonl").read_text(encoding="utf-8").splitlines()
        self.assertEqual([json.loads(x)["day"] for x in lines], ["2026-10-01", "2026-10-02", "2026-10-03"])

    def test_past_day_disappearing_fails(self) -> None:
        old = _write(self.tmp, "2026-10-01", "a")
        _write(self.tmp, "2026-10-02", "b")
        bd.run(self.tmp)
        old.unlink()
        with self.assertRaises(bd.DatasetError):
            bd.run(self.tmp)
        with self.assertRaises(bd.DatasetError):
            bd.run(self.tmp, check=True)

    def test_duplicate_id_across_days_fails(self) -> None:
        _write(self.tmp, "2026-10-01", "a")
        d = self.tmp / "events" / "2026-10-02"
        d.mkdir(parents=True)
        (d / "evt-2026-10-01-a.json").write_text(
            json.dumps(_event("2026-10-01", "a")), encoding="utf-8")
        with self.assertRaises(bd.DatasetError):
            bd.run(self.tmp)

    def test_check_detects_stale_data(self) -> None:
        _write(self.tmp, "2026-10-01", "a")
        bd.run(self.tmp)
        _write(self.tmp, "2026-10-02", "b")
        with self.assertRaises(bd.DatasetError):
            bd.run(self.tmp, check=True)


class RealTreeTests(unittest.TestCase):
    def test_repo_ledger_intact_and_data_current(self) -> None:
        summary = bd.run(ROOT, check=True)
        ledger = bd.load_ledger(ROOT)
        self.assertEqual(summary["events"], sum(len(v) for v in ledger.values()))
        # Suelo histórico: lo publicado en la landing desde el primer día.
        self.assertGreaterEqual(len(ledger.get("2026-09-29", [])), 12)
        self.assertGreaterEqual(summary["days"], 16)
        self.assertGreaterEqual(summary["events"], 149)


if __name__ == "__main__":
    unittest.main()

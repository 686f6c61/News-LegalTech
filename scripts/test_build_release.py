#!/usr/bin/env python3
"""Pruebas del versionado 1.N.0 y del grafo publico."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_release as br


class VersionTests(unittest.TestCase):
    def test_baseline_and_following_days(self) -> None:
        self.assertEqual(br.version_for_date(date(2026, 9, 29)), "1.0.0")
        self.assertEqual(br.version_for_date(date(2026, 9, 30)), "1.1.0")
        self.assertEqual(br.version_for_date(date(2026, 10, 1)), "1.2.0")
        self.assertEqual((date(2026, 10, 1) - br.BASELINE_DATE).days, 2)

    def test_before_baseline_rejected(self) -> None:
        with self.assertRaises(br.ReleaseError):
            br.version_for_date(date(2026, 9, 28))

    def test_date_wins_over_dense_gap(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "releases" / "1.0.0").mkdir(parents=True)
            (root / "releases" / "1.0.0" / "RELEASE.md").write_text(
                "**Fecha:** 2026-09-29 (Europe/Madrid)\n",
                encoding="utf-8",
            )
            # Hueco: no existe 1.1.0. El 2026-10-01 sigue siendo 1.2.0.
            self.assertEqual(br.next_folder_version(root), "1.1.0")
            self.assertEqual(br.resolve_version(root, date(2026, 10, 1)), "1.2.0")

    def test_version_collision_with_other_date(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            notes = root / "releases" / "1.1.0"
            notes.mkdir(parents=True)
            (notes / "RELEASE.md").write_text(
                "**Fecha:** 2026-10-02 (Europe/Madrid)\n",
                encoding="utf-8",
            )
            with self.assertRaises(br.ReleaseError) as ctx:
                br.resolve_version(root, date(2026, 9, 30))
            self.assertEqual(ctx.exception.code, 2)


class GraphTests(unittest.TestCase):
    def test_public_namespace_and_event_shape(self) -> None:
        event = {
            "id": "evt-2026-09-30-demo",
            "date": "2026-09-29",
            "type": "litigation",
            "sota_score": 9.2,
            "ai_legaltech": True,
            "title": "Titulo de prueba suficientemente largo",
            "summary_p1": "Parrafo uno con la idea clave del evento de prueba para el grafo.",
            "summary_p2": "Parrafo dos con el impacto de negocio del evento de prueba para el grafo.",
            "why_sota": "Porque mueve el estado del arte.",
            "why_now": "Porque cae en este digest.",
            "geo": ["US"],
            "topics": ["copyright"],
            "sources": [
                {
                    "source_id": "src-demo",
                    "url": "https://example.com/demo",
                    "cited_title": "Demo",
                }
            ],
            "entities": ["ent-aepd"],
            "lang": "es",
        }
        document = br.assemble_graph(date(2026, 9, 30), "1.1.0", [event])
        text = br.dump_jsonld(document)
        self.assertNotIn(br.LEGACY_NS, text)
        self.assertIn(br.SOTA_NS, text)
        self.assertEqual(document["@context"]["sota"], br.SOTA_NS)
        dataset = document["@graph"][0]
        self.assertEqual(dataset["schema:version"], "1.1.0")
        self.assertEqual(dataset["schema:datePublished"], "2026-09-30")
        self.assertEqual(
            dataset["@id"],
            "https://github.com/686f6c61/News-LegalTech/releases/1.1.0",
        )
        self.assertEqual(
            dataset["schema:url"],
            "https://github.com/686f6c61/News-LegalTech/releases/download/1.1.0/graph.jsonld",
        )
        article = document["@graph"][1]
        self.assertEqual(article["sota:type"], "litigation")
        self.assertEqual(article["sota:sotaScore"], 9.2)
        self.assertIn("Parrafo dos", article["schema:articleBody"])
        self.assertEqual(article["schema:citation"][0]["sota:sourceId"], "src-demo")
        entity = document["@graph"][2]
        self.assertEqual(entity["schema:identifier"], "ent-aepd")
        parsed = json.loads(text)
        self.assertEqual(parsed["@graph"][1]["sota:sotaScore"], 9.2)

    def test_day_without_events_skips(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "events").mkdir()
            result = br.build_day(root, date(2026, 10, 1), dry_run=True)
            self.assertTrue(result.skipped)
            self.assertEqual(result.version, "1.2.0")
            self.assertFalse((root / "releases" / "1.2.0").exists())

    def test_roundtrip_write_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            day_dir = root / "events" / "2026-09-30"
            day_dir.mkdir(parents=True)
            event = {
                "id": "evt-2026-09-30-demo",
                "date": "2026-09-30",
                "type": "product",
                "sota_score": 7.0,
                "ai_legaltech": True,
                "title": "Producto de prueba para la release diaria",
                "summary_p1": "Idea clave del producto de prueba con longitud suficiente para el esquema.",
                "summary_p2": "Impacto de negocio del producto de prueba con longitud suficiente para el esquema.",
                "sources": [
                    {
                        "source_id": "src-demo",
                        "url": "https://example.com/a",
                        "cited_title": "Fuente",
                    }
                ],
                "entities": [],
            }
            (day_dir / "evt-2026-09-30-demo.json").write_text(
                json.dumps(event),
                encoding="utf-8",
            )
            (day_dir / "index.yaml").write_text(
                "date: '2026-09-30'\nevents:\n- id: evt-2026-09-30-demo\n",
                encoding="utf-8",
            )
            digest = root / "content" / "digests" / "daily" / "2026" / "2026-09-30.md"
            digest.parent.mkdir(parents=True)
            digest.write_text(
                '---\ntitle: "Digest"\ndate: 2026-09-30\nrelease: "full-radar-local"\n---\n\nCuerpo\n',
                encoding="utf-8",
            )
            first = br.build_day(root, date(2026, 9, 30))
            self.assertTrue(first.changed)
            self.assertEqual(first.version, "1.1.0")
            graph = (root / "releases" / "1.1.0" / "graph.jsonld").read_text(encoding="utf-8")
            self.assertNotIn("legaltech-sota.local", graph)
            self.assertIn('release: "1.1.0"', digest.read_text(encoding="utf-8"))
            self.assertIn("release: 1.1.0", (day_dir / "index.yaml").read_text(encoding="utf-8"))
            second = br.build_day(root, date(2026, 9, 30))
            self.assertFalse(second.changed)
            checked = br.build_day(root, date(2026, 9, 30), check=True)
            self.assertIn("check OK", checked.message)


class RepoTests(unittest.TestCase):
    def test_real_day_30_version_and_count(self) -> None:
        events = br.load_day_events(br.ROOT, date(2026, 9, 30))
        self.assertEqual(len(events), 6)
        self.assertEqual(events[0]["id"], "evt-2026-09-30-tr-ross-3rd-circuit")
        self.assertEqual(br.version_for_date(date(2026, 9, 30)), "1.1.0")
        document = br.assemble_graph(date(2026, 9, 30), "1.1.0", events)
        self.assertEqual(len(document["@graph"][0]["schema:hasPart"]), 6)
        self.assertNotIn(br.LEGACY_NS, br.dump_jsonld(document))


if __name__ == "__main__":
    unittest.main()

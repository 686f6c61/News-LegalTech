#!/usr/bin/env python3
"""Pruebas del versionado DD.MM.YY y del grafo publico."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import build_release as br


def _git(root: Path, *args: str) -> None:
    subprocess.run(
        ["git", "-C", str(root), *args],
        check=True,
        capture_output=True,
        text=True,
    )


def _write_event(root: Path, day: date) -> None:
    day_dir = root / "events" / day.isoformat()
    day_dir.mkdir(parents=True)
    event_id = f"evt-{day.isoformat()}-demo"
    event = {
        "id": event_id,
        "date": day.isoformat(),
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
    (day_dir / f"{event_id}.json").write_text(
        json.dumps(event, ensure_ascii=False),
        encoding="utf-8",
    )


class VersionTests(unittest.TestCase):
    def test_calendar_versions(self) -> None:
        self.assertEqual(br.version_for_date(date(2026, 10, 2)), "02.10.26")
        self.assertEqual(br.version_for_date(date(2026, 10, 1)), "01.10.26")
        self.assertEqual(br.version_for_date(date(2026, 9, 29)), "29.09.26")
        self.assertEqual(br.version_for_date(date(2026, 9, 30)), "30.09.26")
        self.assertEqual(br.legacy_version_for_date(date(2026, 9, 29)), "26.09.29")
        self.assertEqual(br.legacy_version_for_date(date(2026, 9, 30)), "26.09.30")
        self.assertEqual(br.legacy_version_for_date(date(2026, 10, 1)), "26.10.01")
        self.assertEqual(br.parse_calendar_version("02.10.26"), date(2026, 10, 2))
        self.assertEqual(br.parse_calendar_version("01.10.26"), date(2026, 10, 1))
        self.assertEqual(br.parse_calendar_version("v30.09.26"), date(2026, 9, 30))
        self.assertEqual(br.parse_legacy_calendar_version("26.10.01"), date(2026, 10, 1))
        self.assertEqual(br.parse_legacy_calendar_version("v26.09.30"), date(2026, 9, 30))
        self.assertEqual(br.parse_legacy_calendar_version("26.09.29"), date(2026, 9, 29))
        self.assertIsNone(br.parse_calendar_version("1.1.0"))
        self.assertIsNone(br.parse_calendar_version("26.10.1"))
        self.assertIsNone(br.parse_calendar_version("26.13.01"))
        self.assertIsNone(br.parse_legacy_calendar_version("26.13.01"))

    def test_missing_day_does_not_renumber(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "releases" / "26.09.29").mkdir(parents=True)
            (root / "releases" / "26.09.29" / "RELEASE.md").write_text(
                "**Fecha:** 2026-09-29 (Europe/Madrid)\n",
                encoding="utf-8",
            )
            self.assertEqual(br.resolve_version(root, date(2026, 10, 2)), "02.10.26")
            self.assertEqual(br.version_for_date(date(2026, 10, 1)), "01.10.26")

    def test_version_collision_with_other_date(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            notes = root / "releases" / "02.10.26"
            notes.mkdir(parents=True)
            (notes / "RELEASE.md").write_text(
                "**Fecha:** 2026-09-30 (Europe/Madrid)\n",
                encoding="utf-8",
            )
            with self.assertRaises(br.ReleaseError) as ctx:
                br.resolve_version(root, date(2026, 10, 2))
            self.assertEqual(ctx.exception.code, 2)

    def test_legacy_folder_conflicts_with_new_format_of_another_day(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / "releases" / "26.09.29"
            folder.mkdir(parents=True)
            (folder / "RELEASE.md").write_text(
                "**Fecha:** 2026-09-29 (Europe/Madrid)\n",
                encoding="utf-8",
            )
            with self.assertRaises(br.ReleaseError) as ctx:
                br.resolve_version(root, date(2029, 9, 26))
            self.assertEqual(ctx.exception.code, 2)
            self.assertEqual(br.resolve_version(root, date(2026, 10, 2)), "02.10.26")

    def test_tag_conflict_uses_new_format(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _git(root, "init")
            _git(root, "config", "user.email", "test@example.com")
            _git(root, "config", "user.name", "test")
            (root / "README.md").write_text("x\n", encoding="utf-8")
            _git(root, "add", "README.md")
            _git(root, "commit", "-m", "init")
            _git(root, "tag", "02.10.26")
            _git(root, "tag", "26.09.29")
            with self.assertRaises(br.ReleaseError) as ctx:
                br.resolve_version(root, date(2026, 10, 2))
            self.assertEqual(ctx.exception.code, 2)
            self.assertIn("02.10.26", str(ctx.exception))
            self.assertEqual(br.resolve_version(root, date(2026, 10, 3)), "03.10.26")

    def test_legacy_release_is_not_rewritten(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            day = date(2026, 10, 1)
            _write_event(root, day)
            legacy = root / "releases" / "26.10.01"
            legacy.mkdir(parents=True)
            graph = legacy / "graph.jsonld"
            graph.write_text('{"@id": "historical"}\n', encoding="utf-8")
            (legacy / "RELEASE.md").write_text(
                "# Radar LegalTech · 26.10.01\n\n**Fecha:** 2026-10-01 (Europe/Madrid)\n",
                encoding="utf-8",
            )
            result = br.build_day(root, day, force=True)
            self.assertTrue(result.historical)
            self.assertEqual(result.version, "26.10.01")
            self.assertEqual(graph.read_text(encoding="utf-8"), '{"@id": "historical"}\n')
            self.assertFalse((root / "releases" / "01.10.26").exists())
            self.assertEqual(br.pending_dates(root), [])


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
        document = br.assemble_graph(date(2026, 9, 30), "30.09.26", [event])
        text = br.dump_jsonld(document)
        self.assertNotIn(br.LEGACY_NS, text)
        self.assertIn(br.SOTA_NS, text)
        self.assertEqual(document["@context"]["sota"], br.SOTA_NS)
        dataset = document["@graph"][0]
        self.assertEqual(dataset["schema:version"], "30.09.26")
        self.assertEqual(dataset["schema:name"], "Radar LegalTech · 30.09.26")
        self.assertEqual(dataset["schema:datePublished"], "2026-09-30")
        self.assertEqual(
            dataset["@id"],
            "https://github.com/686f6c61/News-LegalTech/releases/30.09.26",
        )
        self.assertEqual(
            dataset["schema:url"],
            "https://github.com/686f6c61/News-LegalTech/releases/download/30.09.26/graph.jsonld",
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
            result = br.build_day(root, date(2026, 10, 2), dry_run=True)
            self.assertTrue(result.skipped)
            self.assertEqual(result.version, "02.10.26")
            self.assertFalse((root / "releases" / "02.10.26").exists())

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
            digest = root / "content" / "digests" / "daily" / "2026" / "2026-09-30.md"
            digest.parent.mkdir(parents=True)
            digest.write_text(
                '---\ntitle: "Digest"\ndate: 2026-09-30\nrelease: "1.1.0"\n---\n\nCuerpo\n',
                encoding="utf-8",
            )
            (day_dir / "index.yaml").write_text(
                "date: '2026-09-30'\nrelease: 1.1.0\nevents:\n- id: evt-2026-09-30-demo\n",
                encoding="utf-8",
            )
            first = br.build_day(root, date(2026, 9, 30))
            self.assertTrue(first.changed)
            self.assertEqual(first.version, "30.09.26")
            graph = (root / "releases" / "30.09.26" / "graph.jsonld").read_text(encoding="utf-8")
            self.assertNotIn("legaltech-sota.local", graph)
            self.assertIn('release: "30.09.26"', digest.read_text(encoding="utf-8"))
            self.assertIn("release: 30.09.26", (day_dir / "index.yaml").read_text(encoding="utf-8"))
            notes = (root / "releases" / "30.09.26" / "RELEASE.md").read_text(encoding="utf-8")
            self.assertTrue(notes.startswith("# Radar LegalTech · 30.09.26\n"))
            self.assertIn("`DD.MM.YY`", notes)
            self.assertNotIn("1.N.0", notes)
            second = br.build_day(root, date(2026, 9, 30))
            self.assertFalse(second.changed)
            checked = br.build_day(root, date(2026, 9, 30), check=True)
            self.assertIn("check OK", checked.message)


class RepoTests(unittest.TestCase):
    def test_real_day_30_version_and_count(self) -> None:
        events = br.load_day_events(br.ROOT, date(2026, 9, 30))
        self.assertEqual(len(events), 6)
        self.assertEqual(events[0]["id"], "evt-2026-09-30-tr-ross-3rd-circuit")
        self.assertEqual(br.version_for_date(date(2026, 9, 30)), "30.09.26")
        self.assertEqual(br.legacy_version_for_date(date(2026, 9, 30)), "26.09.30")
        document = br.assemble_graph(date(2026, 9, 30), "30.09.26", events)
        self.assertEqual(len(document["@graph"][0]["schema:hasPart"]), 6)
        self.assertNotIn(br.LEGACY_NS, br.dump_jsonld(document))

    def test_published_legacy_tree_stays_put(self) -> None:
        historical = {
            date(2026, 9, 29): "26.09.29",
            date(2026, 9, 30): "26.09.30",
            date(2026, 10, 1): "26.10.01",
        }
        for day, legacy in historical.items():
            folder = br.ROOT / "releases" / legacy
            before = (folder / "RELEASE.md").read_text(encoding="utf-8")
            result = br.build_day(br.ROOT, day, force=True)
            self.assertTrue(result.historical)
            self.assertEqual(result.version, legacy)
            self.assertEqual((folder / "RELEASE.md").read_text(encoding="utf-8"), before)
            self.assertFalse((br.ROOT / "releases" / br.version_for_date(day)).exists())
        self.assertEqual(br.pending_dates(br.ROOT), [])
        checked = br.check_published(br.ROOT)
        self.assertEqual(
            [item.version for item in checked],
            ["02.10.26", "26.09.29", "26.09.30", "26.10.01"],
        )
        by_version = {item.version: item for item in checked}
        self.assertFalse(by_version["02.10.26"].historical)
        self.assertTrue(all(by_version[v].historical for v in ("26.09.29", "26.09.30", "26.10.01")))
        self.assertEqual(br.resolve_version(br.ROOT, date(2026, 10, 2)), "02.10.26")


class OrthographyTests(unittest.TestCase):
    def test_restore_keeps_utf8_and_english_quotes(self) -> None:
        import orthography as orth

        self.assertEqual(orth.restore_prose("senalar la pagina"), "señalar la página")
        self.assertEqual(orth.restore_prose("esta ventana"), "esta ventana")
        self.assertEqual(orth.restore_prose("Ivo anuncio el dato"), "Ivo anunció el dato")
        self.assertEqual(orth.restore_prose("Anuncio RelFest"), "Anuncio RelFest")
        self.assertEqual(
            orth.restore_prose('la decision y "The decision is final"'),
            'la decisión y "The decision is final"',
        )
        self.assertEqual(orth.restore_prose("pension provider"), "pension provider")
        self.assertEqual(
            orth.restore_prose("https://ejemplo.test/pagina senalar"),
            "https://ejemplo.test/pagina señalar",
        )
        restored = orth.restore_prose("señalar")
        self.assertEqual(orth.restore_prose(restored), restored)

    def test_utf8_roundtrip_in_graph(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            day = date(2026, 10, 3)
            day_dir = root / "events" / day.isoformat()
            day_dir.mkdir(parents=True)
            event_id = f"evt-{day.isoformat()}-enie"
            event = {
                "id": event_id,
                "date": day.isoformat(),
                "type": "product",
                "sota_score": 7.0,
                "ai_legaltech": True,
                "title": "Hay que señalar la página",
                "summary_p1": "La señal está en la página y no en un senuelo plano con longitud suficiente.",
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
            raw = json.dumps(event, ensure_ascii=False)
            self.assertIn("señalar", raw)
            self.assertNotIn("\\u00f1", raw)
            (day_dir / f"{event_id}.json").write_text(raw, encoding="utf-8")
            result = br.build_day(root, day)
            self.assertFalse(result.skipped)
            graph = result.graph_path.read_text(encoding="utf-8")
            self.assertIn("señalar", graph)
            self.assertIn("página", graph)
            self.assertNotIn("\\u00f1", graph)

    def test_folded_spanish_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            day_dir = root / "events" / "2026-10-03"
            day_dir.mkdir(parents=True)
            event = {
                "id": "evt-2026-10-03-malo",
                "date": "2026-10-03",
                "type": "product",
                "sota_score": 7.0,
                "ai_legaltech": True,
                "title": "Hay que senalar la pagina",
                "summary_p1": "Idea clave del producto de prueba con longitud suficiente para el esquema.",
                "summary_p2": "Impacto de negocio del producto de prueba con longitud suficiente para el esquema.",
                "sources": [
                    {
                        "source_id": "src-demo",
                        "url": "https://example.com/a",
                        "cited_title": "Fuente",
                    }
                ],
            }
            path = day_dir / "evt-2026-10-03-malo.json"
            path.write_text(json.dumps(event, ensure_ascii=False), encoding="utf-8")
            with self.assertRaises(br.ReleaseError):
                br.load_event(path)

    def test_recent_corpus_orthography(self) -> None:
        import orthography as orth

        self.assertEqual(orth.recent_problem_paths(br.ROOT), [])


class IntegrityTests(unittest.TestCase):
    def test_hosts_align(self) -> None:
        self.assertFalse(
            br.hosts_align(
                "https://www.lawsitesblog.com/",
                "https://www.gov.ca.gov/2026/09/30/bill",
            )
        )
        self.assertFalse(
            br.hosts_align(
                "https://www.lawyerpress.com/",
                "https://cincodias.elpais.com/legal/pieza.html",
            )
        )
        self.assertTrue(
            br.hosts_align(
                "https://www.lawnext.com/",
                "https://www.lawnext.com/2026/09/pieza.html",
            )
        )
        self.assertTrue(
            br.hosts_align(
                "https://www.law.com/legaltechnews/",
                "https://www.law.com/legaltechnews/2026/10/01/pieza/",
            )
        )
        self.assertFalse(
            br.hosts_align(
                "https://www.gov.ca.gov/",
                "https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml",
            )
        )
        self.assertTrue(
            br.hosts_align(
                "https://www.aepd.es/",
                "https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/nota",
            )
        )

    def test_utf8_is_not_escaped(self) -> None:
        text = br.dump_jsonld({"schema:name": "España"})
        self.assertIn("España", text)
        self.assertNotIn("\\u00f1", text)

    def test_entity_stub_and_license_land_in_graph(self) -> None:
        event = {
            "id": "evt-2026-10-02-demo",
            "date": "2026-10-02",
            "type": "product",
            "sota_score": 7.0,
            "ai_legaltech": True,
            "title": "Titulo de prueba suficientemente largo",
            "summary_p1": "Parrafo uno con la idea clave del evento de prueba para el grafo.",
            "summary_p2": "Parrafo dos con el impacto de negocio del evento de prueba para el grafo.",
            "sources": [
                {
                    "source_id": "src-demo",
                    "url": "https://example.com/demo",
                    "cited_title": "Demo",
                }
            ],
            "entities": ["ent-demo"],
        }
        document = br.assemble_graph(
            date(2026, 10, 2),
            "02.10.26",
            [event],
            {
                "ent-demo": {
                    "id": "ent-demo",
                    "name": "Demo",
                    "type": "vendor",
                    "url": "https://example.com/",
                    "stub": True,
                }
            },
        )
        self.assertEqual(
            document["@graph"][0]["schema:license"],
            "https://spdx.org/licenses/MIT.html",
        )
        entity = document["@graph"][2]
        self.assertEqual(entity["schema:name"], "Demo")
        self.assertEqual(entity["sota:entityType"], "vendor")
        self.assertTrue(entity["sota:stub"])

    def test_mismatch_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "sources").mkdir()
            (root / "sources" / "catalog.yaml").write_text(
                "count: 1\n"
                "sources:\n"
                "  - id: src-lawsites-bob-ambrogi\n"
                "    url: https://www.lawsitesblog.com/\n",
                encoding="utf-8",
            )
            day = root / "events" / "2026-10-02"
            day.mkdir(parents=True)
            event = {
                "id": "evt-2026-10-02-demo",
                "date": "2026-10-02",
                "type": "regulation",
                "sota_score": 8,
                "ai_legaltech": True,
                "title": "Governor signs a statute on generative tools",
                "summary_p1": "The governor signed a statute that limits how lawyers delegate work to a model.",
                "summary_p2": "Firms that file in that state need a human to check every citation before submission.",
                "sources": [
                    {
                        "source_id": "src-lawsites-bob-ambrogi",
                        "url": "https://www.gov.ca.gov/2026/09/30/bill",
                    }
                ],
                "entities": [],
            }
            (day / "evt-2026-10-02-demo.json").write_text(
                json.dumps(event),
                encoding="utf-8",
            )
            problems = br.integrity_problems(root)
            self.assertTrue(any("gov.ca.gov" in item for item in problems), problems)

    def test_repo_integrity(self) -> None:
        self.assertEqual(br.integrity_problems(br.ROOT), [])


if __name__ == "__main__":
    unittest.main()

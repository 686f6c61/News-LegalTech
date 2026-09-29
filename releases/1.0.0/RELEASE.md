# Release 1.0.0: Observatorio LegalTech SOTA

**Fecha:** 2026-09-29 (Europe/Madrid)  
**Versión:** `1.0.0`  
**Significado:** **primera release diaria** del Observatorio. El grafo JSON-LD de cada día se publica como artefacto de CI; `1.0.0` corresponde al primer día operativo.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/1.0.0/graph.jsonld` |
| Digest diario | `digests/daily/2026-09-29.md` |
| Eventos | `events/2026-09-29/` |
| Schemas | `schemas/` |
| Sources (starter) | `sources/` |
| Entities | `entities/` |

## Eventos incluidos

1. `evt-2026-09-29-aepd-ia-agentica`: flagship AEPD IA agéntica (sota 9.5)
2. `evt-2026-09-29-openai-astra-for-law`: OpenAI Astra for Law (sota 9.0)
3. `evt-2026-09-29-alesis-uk-sovereign-ai`: Alesis UK sovereign AI (sota 8.0)

## Versionado

- Esquema: `MAJOR.MINOR.PATCH` semver ligero sobre el artefacto diario.
- `1.0.0` = primer día (baseline).
- Días siguientes: normalmente `1.N.0` (N = día secuencial) o bump según política de CI cuando GitHub sea SoT.
- El digest Markdown y el `graph.jsonld` van juntos en cada release.

## Notas

- Workspace-only por ahora (GitHub será SoT más adelante).
- Sin Obsidian.
- Catálogo completo de fuentes (~128): `/workspace/legaltech/fuentes-legaltech-mundiales.md`.

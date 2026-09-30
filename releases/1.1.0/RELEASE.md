# Release 1.1.0: Observatorio LegalTech SOTA

**Fecha:** 2026-09-30 (Europe/Madrid)  
**Versión:** `1.1.0`  
**Significado:** día operativo N=1 desde el baseline `1.0.0` (2026-09-29). Semver `1.N.0` con `N = (fecha - 2026-09-29).days`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/1.1.0/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-09-30.md` |
| Eventos | `events/2026-09-30/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-09-30-tr-ross-3rd-circuit` (sota 9.2, litigation): 3rd Circuit afirma la victoria de Thomson Reuters frente a ROSS Intelligence: primer fallo federal de apelacion sobre fair use en entrenamiento de IA
2. `evt-2026-09-30-aepd-ia-curriculums` (sota 8.8, guidance): AEPD: advertencia preventiva sobre IA para cribado y puntuacion de curriculums (EXP202600427)
3. `evt-2026-09-30-morae-morai-spend` (sota 7.6, product): Morae lanza Legal Intelligence Platform con MorAI Spend Intelligence (IA + revision humana de facturas)
4. `evt-2026-09-30-relativity-clair-aap` (sota 7.2, product): Relativity claiR: KPMG y Big Law entran en Advanced Access (GA prevista inicios 2027)
5. `evt-2026-09-30-ascom-aicom` (sota 7.0, standards): ASCOM lanza AICOM: certificacion profesional de Compliance en Inteligencia Artificial (EU AI Act)
6. `evt-2026-09-30-8am-mycase-mcp` (sota 6.8, product): 8am MyCase lanza conector MCP oficial para Claude (73 acciones) e IQ Firm Agent / Draft en roadmap

**Foco AI LegalTech:** 6/6 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/1.1.0` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/1.1.0/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/1.0.0/` conserva `https://legaltech-sota.local/` y no se reescribe.

## Versionado

- `1.0.0` = 2026-09-29 (baseline, primer día).
- Esta fecha fija `1.1.0` (N=1).
- El script contrasta carpetas `releases/` y tags git antes de escribir.
- Un día sin `events/` no genera release: el menor puede saltarse y la fecha sigue mapeando al mismo `1.N.0`.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

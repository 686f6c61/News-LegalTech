# Radar LegalTech · 14.10.26

**Fecha:** 2026-10-14 (Europe/Madrid)  
**Versión:** `14.10.26`  
**Significado:** release del día 2026-10-14 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/14.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-14.md` |
| Eventos | `events/2026-10-14/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-14-jylo-3-0-agentes-addins-gasto-ia` (sota 8.0, product): Jylo 3.0: agentes configurables, add-ins de Outlook, PowerPoint y Excel, y controles de gasto de IA
2. `evt-2026-10-14-legora-intake-front-door-inhouse-slack` (sota 7.8, product): Legora lanza Intake: una puerta de entrada agéntica para in-house que prepara el trabajo desde Slack
3. `evt-2026-10-14-steno-litigation-genius-open-beta` (sota 7.2, product): Steno abre la beta pública de Litigation Genius: IA sobre el expediente completo, no solo el transcript
4. `evt-2026-10-14-sixfifty-agente-hr-compliance-paychex` (sota 7.0, product): SixFifty (Paychex) lanza un agente de compliance laboral: handbooks, posters y filings por jurisdicción
5. `evt-2026-10-14-useabi-asociado-ia-ma-sin-prompting` (sota 7.4, product): useABI, de un ex M&A de Greenberg Traurig: markups, issues list y diligence como un asociado, sin prompting
6. `evt-2026-10-14-legora-laurel-captura-tiempo-automatica` (sota 6.8, market): Legora y Laurel se alían: cada tarea en Legora genera un time entry listo para revisar
7. `evt-2026-10-14-legatics-harvey-mcp-estado-deal` (sota 6.9, product): Legatics entra en la Connector Library de Harvey: el estado vivo del deal vía MCP
8. `evt-2026-10-14-lexisnexis-brecha-gobernanza-ia-legal-futures` (sota 6.6, other): LexisNexis: dos tercios usan IA a diario o varias veces por semana, pero casi uno de cada cinco no sabe quién gobierna esa IA
9. `evt-2026-10-14-tromans-ley-incentivo-adversarial-ia` (sota 6.5, other): Tromans formula la «Law of Adversarial Incentives»: más conflicto, más trabajo extra pese a la IA
10. `evt-2026-10-14-permeta-ferc-ai-elibrary-mcp` (sota 6.4, product): Permeta lanza FERC.ai: la eLibrary de FERC consultable en Claude, Copilot y ChatGPT con citas

**Foco AI LegalTech:** 10/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/14.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/14.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `14.10.26`.
- El título público es `Radar LegalTech · 14.10.26`.
- El script contrasta la carpeta y el tag `14.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

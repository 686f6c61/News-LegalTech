# Radar LegalTech · 03.10.26

**Fecha:** 2026-10-03 (Europe/Madrid)  
**Versión:** `03.10.26`  
**Significado:** release del día 2026-10-03 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/03.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-03.md` |
| Eventos | `events/2026-10-03/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-03-falcon-dejonghe` (sota 8.8, market): Wim Dejonghe (ex-A&O) respalda Falcon: New Model AI-native belga con flat fee y revisión same-day
2. `evt-2026-10-03-mitratech-botdojo` (sota 8.5, market): Mitratech adquiere BotDojo: agentes gobernados y MCP bidireccional sobre ARIES
3. `evt-2026-10-03-harvey-legalscape` (sota 8.4, product): Harvey se asocia con Legalscape: derecho japonés (leyes, jurisprudencia y libros) dentro de Harvey
4. `evt-2026-10-03-es-ts-ia-recursos` (sota 8.2, regulation): Ministerio de Justicia pone IA en la Sala Civil del Tribunal Supremo para tramitar recursos
5. `evt-2026-10-03-barcelona-ia-autoridad` (sota 8.0, case_law): Audiencia de Barcelona: la IA no es un «argumento de autoridad» en un recurso judicial
6. `evt-2026-10-03-ross-scotus-petition` (sota 7.9, regulation): ROSS pedirá al Supreme Court revisar el fallo del 3rd Circuit a favor de Thomson Reuters
7. `evt-2026-10-03-pierson-ferdinand-300` (sota 7.6, market): Pierson Ferdinand (Zero Associates, Harvey) supera 300 partners globales
8. `evt-2026-10-03-relativity-frontier-labs` (sota 7.4, product): Relativity: deadline cloud 2028 se mantiene y prioriza labs frontier frente a Harvey/Legora
9. `evt-2026-10-03-lf-ai-maturity-conveyancing` (sota 7.0, market): InfoTrack DCMI UK: madurez digital +10% relativo, pero IA firm-wide solo en el 18%
10. `evt-2026-10-03-imanage-chatgpt` (sota 6.8, product): iManage lanza plugin de ChatGPT Enterprise con knowledge gobernado (ethical walls y audit)

**Foco AI LegalTech:** 10/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/03.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/03.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `03.10.26`.
- El título público es `Radar LegalTech · 03.10.26`.
- El script contrasta la carpeta y el tag `03.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

# Radar LegalTech · 13.10.26

**Fecha:** 2026-10-13 (Europe/Madrid)  
**Versión:** `13.10.26`  
**Significado:** release del día 2026-10-13 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/13.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-13.md` |
| Eventos | `events/2026-10-13/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-13-anthropic-claude-tip-falso-policia-filadelfia` (sota 8.2, other): Anthropic confirma que Claude envió un tip falso sobre un homicidio a la policía de Filadelfia durante pruebas con sitios web reales
2. `evt-2026-10-13-florida-juez-peffer-suspension-deepfake-ia` (sota 7.6, case_law): El Tribunal Supremo de Florida suspende 30 días y multa con 10.000 dólares a una juez por usar un deepfake de IA en su campaña
3. `evt-2026-10-13-leela-seed-46m-compliance-agentes-finanzas` (sota 7.1, funding): Leela sale del sigilo con 4,6 millones de dólares: agentes de IA que ejecutan compliance de punta a punta en finanzas reguladas de EE. UU.
4. `evt-2026-10-13-z-ai-glm-legal-harvey-lab-19pct` (sota 6.9, product): Z.ai lanza GLM-Legal: un modelo agéntico jurídico con 19,2% de all-pass en el Harvey LAB y beta solo por solicitud
5. `evt-2026-10-13-3rd-circuit-desella-ross-copyright-ordinario` (sota 6.7, case_law): El 3rd Circuit desella su opinión en Thomson Reuters v. ROSS: «no more than an ordinary copyright case» y distingue la IA generativa
6. `evt-2026-10-13-gateley-cto-tranter-jylo-ai` (sota 5.9, market): Gateley nombra CTO a Nigel Tranter (ex Orrick y Pinsent Masons) para acelerar el despliegue de su plataforma Jylo AI
7. `evt-2026-10-13-ofac-icc-licencia-software-ediscovery` (sota 5.8, regulation): EE. UU. sanciona al Tribunal Penal Internacional: ComplexDiscovery pregunta si la licencia OFAC de software empresarial cubre eDiscovery

**Foco AI LegalTech:** 6/7 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/13.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/13.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `13.10.26`.
- El título público es `Radar LegalTech · 13.10.26`.
- El script contrasta la carpeta y el tag `13.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

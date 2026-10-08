# Radar LegalTech · 08.10.26

**Fecha:** 2026-10-08 (Europe/Madrid)  
**Versión:** `08.10.26`  
**Significado:** release del día 2026-10-08 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/08.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-08.md` |
| Eventos | `events/2026-10-08/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-08-stanford-codex-keystone-redline-standard` (sota 8.4, research): Stanford CodeX lanza Keystone, con Google como socio ancla, para que los despachos compartan sus redlines (marcas de revisión) y formar abogados capaces de supervisar a la IA
2. `evt-2026-10-08-spellbook-autonomous-contract-management-ga` (sota 8.1, product): Spellbook abre a todos su Autonomous Contract Management (gestión autónoma de contratos) y lo presenta como sustituto «AI-native» del CLM
3. `evt-2026-10-08-pilot5-ia-adversarial-cinco-modelos` (sota 7.8, product): Pilot5 lanza una IA adversarial para abogados: cinco modelos analizan el asunto, uno ataca el consenso y el abogado recibe una recomendación con el mejor contraargumento
4. `evt-2026-10-08-lawvu-lens-cartera-contratos` (sota 7.6, product): LawVu lanza Lens: preguntas en lenguaje natural sobre toda la cartera de contratos de la empresa, con cita a cada documento
5. `evt-2026-10-08-sirius-xm-desestimada-demanda-ia-seleccion` (sota 7.6, case_law): Un juez federal de Detroit desestima la demanda contra Sirius XM por discriminación racial atribuida a su IA de selección de personal
6. `evt-2026-10-08-everlaw-informe-2026-adopcion-ia` (sota 7.5, research): El informe 2026 de Everlaw cifra en un 49% el uso de IA generativa en el sector legal, pero solo un 34% la integra en toda la organización y apenas un 3% usa agentes
7. `evt-2026-10-08-alemania-ley-violencia-digital-deepfakes` (sota 7.4, regulation): Alemania aprueba en Consejo de Ministros su ley contra la violencia digital: nuevos delitos por crear o difundir deepfakes y vía rápida para identificar a usuarios anónimos
8. `evt-2026-10-08-wordsmith-goodlawyer-abogados-embebidos-ia` (sota 7.2, product): Wordsmith y Goodlawyer se alían: los abogados in-house fraccionales y embebidos de la red canadiense trabajarán con la IA de Wordsmith
9. `evt-2026-10-08-teddy-ai-seed-60m` (sota 7.0, funding): Teddy AI cierra un seed de 60 millones de dólares y dice facturar más de 25, pero no revela a qué se dedica, quién la dirige ni quién ha invertido
10. `evt-2026-10-08-neolegal-adquiere-leya` (sota 6.8, market): Neolegal compra Leya y suma a 50.000 personas que tienen acceso a un abogado como beneficio de empresa en Quebec

**Foco AI LegalTech:** 8/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/08.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/08.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `08.10.26`.
- El título público es `Radar LegalTech · 08.10.26`.
- El script contrasta la carpeta y el tag `08.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

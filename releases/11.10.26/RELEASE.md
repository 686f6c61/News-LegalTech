# Radar LegalTech · 11.10.26

**Fecha:** 2026-10-11 (Europe/Madrid)  
**Versión:** `11.10.26`  
**Significado:** release del día 2026-10-11 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/11.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-11.md` |
| Eventos | `events/2026-10-11/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-11-oab-sp-enter-accion-civil-publica-ia-abogacia` (sota 8.4, litigation): La OAB de São Paulo demanda a Enter, la legaltech de IA agéntica valorada en 1.200 millones de dólares: pide supervisión humana verificable y que no venda a quien no es abogado
2. `evt-2026-10-11-tianjin-ia-plagio-opinion-supremo-popular` (sota 7.4, case_law): Un juzgado de Tianjin cierra por mediación un caso de serie animada hecha con IA a partir de una novela ajena, bajo la nueva Opinión del Supremo Popular sobre litigios de IA
3. `evt-2026-10-11-ropes-gray-100-horas-experimentar-ia` (sota 7.0, market): Ropes & Gray deja que más de 1.000 asociados y counsel computen hasta 100 horas de experimentación con IA como horas facturables
4. `evt-2026-10-11-vlex-clio-barcelona-hub-ia-encuesta-abogados` (sota 6.9, market): Los fundadores de vLex, ya dentro de Clio, dicen que el 89% de los abogados independientes y de despachos pequeños usa IA, sobre todo ChatGPT, y la mitad con versiones gratuitas
5. `evt-2026-10-11-nyai-ai-studio-agentes-legal-compliance-india` (sota 6.7, product): NYAI lanza AI Studio en India: una plataforma model-agnostic para que despachos y equipos de compliance construyan y gobiernen sus propios agentes de IA
6. `evt-2026-10-11-legalitas-alex-asistente-ia-leads-curia` (sota 6.6, market): Legálitas cuenta cómo su asistente Álex alcanza 1,5 millones de usuarios y unos 10.000 leads al mes, y cómo su herramienta Curia reduce la redacción de diez minutos a uno
7. `evt-2026-10-11-ideallegal-ai-equipo-ia-multimodelo-word` (sota 6.2, product): iDealLegal.ai, una startup bootstrapped de 2026, pone en Word un equipo de IA que cruza GPT, Claude y Gemini y marca para revisión humana los desacuerdos entre modelos

**Foco AI LegalTech:** 7/7 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/11.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/11.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `11.10.26`.
- El título público es `Radar LegalTech · 11.10.26`.
- El script contrasta la carpeta y el tag `11.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

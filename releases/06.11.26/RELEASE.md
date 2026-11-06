# Radar LegalTech · 06.11.26

**Fecha:** 2026-11-06 (Europe/Madrid)  
**Versión:** `06.11.26`  
**Significado:** release del día 2026-11-06 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/06.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-06.md` |
| Eventos | `events/2026-11-06/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-06-ao-shearman-compromiso-1100m-ia-practicas` (sota 8.6, market): A&O Shearman compromete 1.100 millones de dólares en cinco años para que cada práctica dedique al menos el 3% de su tiempo a construir herramientas de IA especializadas
2. `evt-2026-11-06-fieldfisher-despliega-legora-1400-profesionales` (sota 8.2, product): Fieldfisher despliega Legora en unos 1.400 abogados y profesionales de Business Services tras un piloto de seis semanas con 137 usuarios en Europa
3. `evt-2026-11-06-harvey-forum-chicago-graph-fact-outlook-imanage` (sota 8.0, product): Harvey presenta en FORUM Chicago su Graph de contexto, el Fact Graph para litigación, agentes en Outlook y la sincronización bidireccional con iManage
4. `evt-2026-11-06-lopezmarques-adopta-harvey-litigacion-mercantil-penal` (sota 7.4, product): Lopezmarqués adopta Harvey en litigación y arbitraje, mercantil y penal económico, trabajando sobre las bases de conocimiento propias del despacho
5. `evt-2026-11-06-farhat-cutera-legora-citas-erroneas-sin-sancion` (sota 7.8, case_law): El Distrito Norte de California no sanciona a la abogada de Cutera que usó Legora, pero descarta las citas erróneas del escrito y no admite las correcciones posteriores
6. `evt-2026-11-06-comite-prueba-eeuu-atasco-reglas-ia-deepfakes` (sota 7.1, regulation): El comité federal de reglas de prueba de EE. UU. sigue atascado con las normas sobre IA y deepfakes; Maura Grossman se declara poco esperanzada
7. `evt-2026-11-06-crcica-adopta-jus-ai-archivo-arbitraje` (sota 7.0, product): CRCICA, el centro de arbitraje de El Cairo, adopta Jus AI de Jus Mundi para consultar su propio archivo institucional de laudos y doctrina
8. `evt-2026-11-06-reino-unido-revision-regulacion-servicios-juridicos-lloyd` (sota 7.5, regulation): El Gobierno británico acepta la revisión Lloyd y lanza un repaso completo de la regulación de servicios jurídicos, con AI y lawtech en el alcance, de cara a 2029
9. `evt-2026-11-06-madrid-ley-abogacia-general-diez-anos` (sota 6.8, regulation): Madrid aprueba una nueva Ley de la Abogacía General que exige diez años de experiencia para dirigir los servicios jurídicos autonómicos y separa asesoramiento y litigios
10. `evt-2026-11-06-meta-google-tiktok-demandan-california-ab1709-menores` (sota 7.2, litigation): Meta, Google y TikTok demandan al fiscal general de California para bloquear la ley AB 1709 que restringe feeds personalizados y autoplay a menores de 16 años

**Foco AI LegalTech:** 7/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/06.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/06.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `06.11.26`.
- El título público es `Radar LegalTech · 06.11.26`.
- El script contrasta la carpeta y el tag `06.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

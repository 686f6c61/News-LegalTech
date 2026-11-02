# Radar LegalTech · 02.11.26

**Fecha:** 2026-11-02 (Europe/Madrid)  
**Versión:** `02.11.26`  
**Significado:** release del día 2026-11-02 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/02.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-02.md` |
| Eventos | `events/2026-11-02/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-02-corea-jueces-precedentes-falsos-ia-encuesta-supremo` (sota 8.0, research): Ocho de cada diez jueces surcoreanos de civil, familia y contencioso han visto citar precedentes falsos o inexistentes generados por IA, según una encuesta del Tribunal Supremo, que estudia multas y verificación obligatoria
2. `evt-2026-11-02-nysba-directrices-eticas-ia-facturacion-supervision` (sota 7.8, guidance): El Colegio de Abogados del Estado de Nueva York aprueba sus directrices éticas sobre IA: se puede facturar el tiempo de verificar lo que produce la herramienta, pero no el de aprender a usarla, y el coste de la herramienta es gasto general
3. `evt-2026-11-02-cma-investiga-meta-terminos-contenido-editores-ia` (sota 7.6, regulation): La CMA británica abre expediente a Meta por abuso de posición dominante: sus términos para empresas le permitirían usar el contenido de las webs de los editores para sus productos de IA sin darles opción
4. `evt-2026-11-02-drcf-declaracion-agentes-ia-responsabilidad-empresas` (sota 7.4, guidance): Los cuatro reguladores digitales británicos avisan de que la autonomía de un agente de IA no reduce la responsabilidad de quien lo despliega y de que las normas de consumo, datos, competencia y pagos ya se aplican
5. `evt-2026-11-02-runway-demanda-youtube-dmca-1201-sigue-adelante` (sota 7.2, case_law): Un juez federal de Nueva York deja seguir la demanda colectiva de creadores de YouTube contra Runway por saltarse las protecciones técnicas de la plataforma para descargar vídeos con los que entrenar su modelo
6. `evt-2026-11-02-google-cloud-cursos-gemini-equipos-juridicos` (sota 6.2, product): Google Cloud lanza en Google Skills cursos gratuitos de Gemini para equipos jurídicos y de servicios financieros, con un programa para pasar a construir agentes en producción
7. `evt-2026-11-02-cps-cita-sentencia-inexistente-high-court-r-v-j` (sota 6.8, case_law): La Fiscalía británica vuelve a apoyarse ante la High Court en una sentencia que no existe, ahora en la decisión de seguir procesando a un niño de 11 años, y el tribunal lo llama "insatisfactorio" pero irrelevante
8. `evt-2026-11-02-brechas-despachos-registro-california-ingenieria-social` (sota 6.9, market): Diez despachos estadounidenses, entre ellos Baker McKenzie, Troutman, WilmerHale y Greenberg Traurig, han notificado este año en California brechas de datos causadas en su mayoría por engaños a su propio personal
9. `evt-2026-11-02-supremo-viudedad-completa-victimas-violencia-genero-compensatoria` (sota 6.4, case_law): El Supremo fija en Pleno que las víctimas de violencia de género divorciadas cobran la pensión de viudedad completa aunque recibieran una pensión compensatoria menor

**Foco AI LegalTech:** 6/9 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/02.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/02.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `02.11.26`.
- El título público es `Radar LegalTech · 02.11.26`.
- El script contrasta la carpeta y el tag `02.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

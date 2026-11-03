# Radar LegalTech · 03.11.26

**Fecha:** 2026-11-03 (Europe/Madrid)  
**Versión:** `03.11.26`  
**Significado:** release del día 2026-11-03 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/03.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-03.md` |
| Eventos | `events/2026-11-03/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-03-nyt-demanda-brave-scraping-ia` (sota 8.2, litigation): The New York Times demanda al navegador Brave por copiar su contenido saltándose el muro de pago y venderlo a desarrolladores de IA como Anthropic, Perplexity, Mistral, xAI o Cohere
2. `evt-2026-11-03-vetta-scissero-pujan-activos-abogados-weil` (sota 7.8, market): Otras dos firmas nativas de IA, Vetta y Scissero, pujan por los abogados, los precedentes y la tecnología de Weil, incluida su plataforma propia para operaciones, y se suman a Crosby
3. `evt-2026-11-03-nueva-jersey-chatbots-ia-responsabilidad-producto` (sota 7.6, regulation): Nueva Jersey tramita un proyecto de ley que permitiría demandar a los proveedores de chatbots de IA bajo la ley de responsabilidad por productos defectuosos, y los abogados defensores avisan de una avalancha de demandas
4. `evt-2026-11-03-maine-bar-deja-decisis-clio-library-clio-work` (sota 7.2, market): El colegio de abogados de Maine deja Decisis por Clio Library, ahorra más de 50.000 dólares al año y dará a sus colegiados cuatro meses gratis de Clio Work, la IA de Clio
5. `evt-2026-11-03-litmas-ai-asociado-agentico-litigacion` (sota 6.6, product): Litmas AI relanza su plataforma de litigación como Agentic Associate, un asociado agéntico que va de la investigación del caso a la redacción de una moción de juicio sumario
6. `evt-2026-11-03-lexisnexis-canada-investigacion-agentica` (sota 6.4, guidance): LexisNexis Canadá explica cómo encargar investigación jurídica a un agente de IA: un encargo bien definido, y el abogado sigue respondiendo del análisis
7. `evt-2026-11-03-clio-canada-95-por-ciento-usa-ia` (sota 6.2, research): El 95% de los profesionales jurídicos canadienses ya usa IA, según el informe de Clio, y el 66% dice que ha mejorado los ingresos de su despacho, pero solo el 47% en los pequeños
8. `evt-2026-11-03-corte-suprema-argentina-anonimizador-documentos-judiciales` (sota 7.0, product): La Corte Suprema argentina implanta un anonimizador de documentos judiciales que detecta más de 15 tipos de datos personales y los sustituye por marcadores como [Persona 1] antes de publicar o entregar resoluciones
9. `evt-2026-11-03-despachos-canadienses-brechas-datos-phishing` (sota 7.0, other): Cuatro grandes despachos canadienses, McCarthy Tétrault, Borden Ladner Gervais, Bennett Jones y Davies, notifican brechas de datos tras una campaña de phishing contra el sector legal y financiero
10. `evt-2026-11-03-cgpj-trienios-juezas-sustitutas-antiguedad` (sota 7.0, regulation): El CGPJ niega a las juezas sustitutas la antigüedad por todo el tiempo de nombramiento: para los trienios solo cuenta el servicio efectivo, por 19 votos a 2
11. `evt-2026-11-03-examen-abogacia-eeuu-caen-aprobados-california` (sota 6.6, research): Caen los aprobados del examen de acceso a la abogacía en EE. UU.: California aprueba solo al 48,3% en julio, su peor dato de julio en cinco años, y Nueva York baja al 67%

**Foco AI LegalTech:** 7/11 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/03.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/03.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `03.11.26`.
- El título público es `Radar LegalTech · 03.11.26`.
- El script contrasta la carpeta y el tag `03.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

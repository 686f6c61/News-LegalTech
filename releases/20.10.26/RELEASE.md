# Radar LegalTech · 20.10.26

**Fecha:** 2026-10-20 (Europe/Madrid)  
**Versión:** `20.10.26`  
**Significado:** release del día 2026-10-20 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/20.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-20.md` |
| Eventos | `events/2026-10-20/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-20-en-18286-primera-norma-armonizada-ai-act-calidad` (sota 8.0, standards): La Comisión publica en el Diario Oficial la primera norma armonizada del Reglamento de IA: la EN 18286 da presunción de conformidad al sistema de gestión de calidad del artículo 17
2. `evt-2026-10-20-bag-citas-inventadas-ia-recurso-inadmitido` (sota 7.8, case_law): El Tribunal Federal de Trabajo alemán inadmite un recurso con siete citas falsas o deformadas: firmar sin revisar un escrito hecho con IA equivale a no estar representado
3. `evt-2026-10-20-disney-character-ai-quiebra-sin-demandas` (sota 7.4, market): Disney se queda con la plantilla y la tecnología de Character.AI a través de su quiebra, mientras las demandas por daños a menores se quedan en la empresa vaciada
4. `evt-2026-10-20-harvey-midpage-legora-blue-j-conectores-mcp` (sota 7.2, product): Harvey se conecta a Midpage y Legora a Blue J: las plataformas de IA jurídica abren su interfaz a bases de investigación de terceros vía MCP
5. `evt-2026-10-20-tirant-estudio-ia-abogacia-espanola-generalista` (sota 7.0, research): Un estudio impulsado por Grupo Tirant sobre 760 abogados españoles: el 78,4% usa IA, sobre todo generalista, pero las IA jurídicas puntúan mejor en rigor, fuentes y privacidad
6. `evt-2026-10-20-legalon-agent-builder-beta-juridico-interno` (sota 6.9, product): LegalOn abre en beta Agent Builder: agentes que ejecutan solos tareas del departamento jurídico cuando se cumple una condición en el gestor de asuntos
7. `evt-2026-10-20-lawtechuk-inversion-record-primer-semestre` (sota 6.8, funding): La inversión en lawtech británico bate récord con 227 millones de libras en seis meses, pero más concentrada: tres empresas se llevan el 69%
8. `evt-2026-10-20-uswitch-encuesta-ia-en-lugar-de-abogado` (sota 6.6, research): Cuatro de cada diez británicos preguntarían a la IA antes que a un solicitor, aunque casi uno de cada cuatro usuarios recibió consejos erróneos con consecuencias
9. `evt-2026-10-20-apdcat-circular-1-2026-videovigilancia` (sota 6.4, regulation): La APDCAT sustituye su instrucción de 2009 por la Circular 1/2026 de videovigilancia: incluye drones, vehículos y uniformes y entra en vigor el 8 de noviembre

**Foco AI LegalTech:** 7/9 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/20.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/20.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `20.10.26`.
- El título público es `Radar LegalTech · 20.10.26`.
- El script contrasta la carpeta y el tag `20.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

# Radar LegalTech · 08.11.26

**Fecha:** 2026-11-08 (Europe/Madrid)  
**Versión:** `08.11.26`  
**Significado:** release del día 2026-11-08 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/08.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-08.md` |
| Eventos | `events/2026-11-08/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-08-cozen-oconnor-harvey-firmwide-1000-abogados` (sota 8.3, product): Cozen O'Connor implanta Harvey en toda la firma, más de 1.000 abogados, tras un piloto en el que ya construyó agentes propios para inmobiliario, mercantil y private client
2. `evt-2026-11-08-wongpartnership-august-ia-a-medida-singapur` (sota 7.9, product): WongPartnership, primer gran despacho de Singapur con August, construirá IA a medida para abogados y personal no letrado sin abandonar Harvey ni su piloto de CoCounsel
3. `evt-2026-11-08-lawsites-mapa-50-estados-ia-jueces-clio-judiciary` (sota 8.2, analysis): Clio quiere vender IA a los jueces, pero un mapa de 50 estados de LawSites muestra que las reglas van del veto de Massachusetts a la apertura controlada de Nueva York
4. `evt-2026-11-08-tri-ie-state-european-legal-markets-espana-66-ia` (sota 8.0, research): El 66% de los abogados de despacho en España dice ahorrar tiempo de forma significativa con IA, frente al 52% en Europa y el 32% mundial, según Thomson Reuters Institute e IE Law School
5. `evt-2026-11-08-bythelaw-compra-advia-8000-abogados-portugal` (sota 7.6, market): ByTheLaw compra la plataforma advIA y supera los 8.000 abogados usuarios en Portugal, más de una quinta parte de los colegiados en ejercicio
6. `evt-2026-11-08-hesse-tribunales-sociales-avalancha-escritos-ia-herramientas` (sota 7.8, other): Los tribunales sociales alemanes reciben una oleada de demandas redactadas con IA y Hesse responde con herramientas propias para anonimizar, estructurar datos y tramitar procedimientos masivos
7. `evt-2026-11-08-orbital-derecho-escoces-inmobiliario-pinsent-masons` (sota 7.5, product): Orbital lanza 22 flujos de IA para inmobiliario comercial bajo Derecho escocés tras un piloto con Pinsent Masons: títulos, escrituras Sasine, arrendamientos y certificados de título
8. `evt-2026-11-08-joanna-smith-peritos-ia-declaracion-lista-practica` (sota 7.6, guidance): La jueza Joanna Smith, coautora del informe del Civil Justice Council, da a los peritos una lista práctica para usar IA: declarar solo cuando influya en el fondo y poder explicarlo bajo juramento
9. `evt-2026-11-08-ratio-law-negligencia-100000-libras-garantia-hipotecaria` (sota 7.2, case_law): Un tribunal de Manchester condena a Ratio Law a pagar 100.000 libras por borrar sin querer la cifra garantizada de una hipoteca, lo que la dejó sin efecto por indeterminación
10. `evt-2026-11-08-saskatchewan-ley-regula-agentes-no-abogados` (sota 7.0, regulation): Saskatchewan presenta una ley para que su Law Society regule a los agentes no abogados que representan a clientes de forma habitual ante tribunales y organismos administrativos

**Foco AI LegalTech:** 8/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/08.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/08.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `08.11.26`.
- El título público es `Radar LegalTech · 08.11.26`.
- El script contrasta la carpeta y el tag `08.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

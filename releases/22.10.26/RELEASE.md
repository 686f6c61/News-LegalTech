# Radar LegalTech · 22.10.26

**Fecha:** 2026-10-22 (Europe/Madrid)  
**Versión:** `22.10.26`  
**Significado:** release del día 2026-10-22 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/22.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-22.md` |
| Eventos | `events/2026-10-22/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-22-legora-serie-e-550m-valoracion-8800m` (sota 8.2, funding): Legora levanta 550 millones de dólares en una Serie E que la valora en 8.800 millones y asegura haber pasado de 200 millones de ingresos recurrentes
2. `evt-2026-10-22-law-society-nota-practica-ia-consentimiento-facturacion` (sota 8.0, guidance): La Law Society de Inglaterra y Gales avisa de que usar IA puede exigir el consentimiento del cliente y de que no se puede facturar el tiempo que la tarea habría llevado sin IA
3. `evt-2026-10-22-enter-justica-federal-niega-cautelar-oab-sp-preservacion` (sota 7.9, litigation): La Justicia Federal de São Paulo no frena por ahora a la legaltech Enter, pero le ordena conservar contratos, versiones de sus modelos de IA y registros de uso desde 2024
4. `evt-2026-10-22-harvey-mary-technology-conector-hechos-litigacion` (sota 7.2, product): Harvey se conecta al expediente de hechos de Mary Technology: el trabajo ya revisado por el equipo de litigación, con contradicciones y lagunas, entra en el asistente
5. `evt-2026-10-22-august-products-servicios-productizados-agentes` (sota 6.9, product): August lanza Products: los despachos convierten un servicio en producto a precio fijo que ejecutan sus agentes con sus precedentes y un abogado que valida
6. `evt-2026-10-22-everlaw-informe-in-house-menos-trabajo-despachos-externos` (sota 6.8, research): Más de la mitad de los equipos in-house ya envían menos trabajo a despachos externos y el 81% cree que en cinco años casi todo se cobrará por resultado, según un informe de Everlaw
7. `evt-2026-10-22-estonia-grabacion-consultas-medicas-ia-base-juridica` (sota 6.7, guidance): La IA que graba y resume consultas médicas se extiende en Estonia y el regulador de datos advierte de que el audio necesita su propia base jurídica, probablemente el consentimiento explícito
8. `evt-2026-10-22-weil-programa-ia-summer-associates-laser` (sota 6.2, market): Weil crea un programa de verano para estudiantes de primero que trabajarán con su equipo de ingeniería jurídica en IA: Python, una red neuronal propia y proyectos reales
9. `evt-2026-10-22-meta-nuevo-mexico-sancion-25000-millones-privacidad` (sota 6.6, case_law): Un juez de Nuevo México fija en 25.000 millones de dólares la sanción a Meta por engañar a los usuarios sobre el control de sus datos, cinco veces la multa de la FTC de 2019
10. `evt-2026-10-22-bgh-schufa-scoring-derecho-acceso-logica-rgpd` (sota 6.5, case_law): El Supremo alemán precisa cuándo debe la Schufa explicar cómo calcula su scoring: primero hay que probar que el score pesó en un perjuicio concreto, pero basta la coincidencia en el tiempo
11. `evt-2026-10-22-tjue-c-70-25-phishing-reembolso-inmediato-bancos` (sota 6.0, case_law): El TJUE obliga a los bancos a devolver primero el dinero robado por phishing, como tarde al final del día hábil siguiente, aunque sospechen negligencia grave del cliente

**Foco AI LegalTech:** 8/11 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/22.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/22.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `22.10.26`.
- El título público es `Radar LegalTech · 22.10.26`.
- El script contrasta la carpeta y el tag `22.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

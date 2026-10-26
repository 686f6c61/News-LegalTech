# Radar LegalTech · 26.10.26

**Fecha:** 2026-10-26 (Europe/Madrid)  
**Versión:** `26.10.26`  
**Significado:** release del día 2026-10-26 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/26.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-26.md` |
| Eventos | `events/2026-10-26/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-26-reguladores-bancarios-eeuu-preguntan-si-pueden-apagar-agentes-ia` (sota 8.1, regulation): La Reserva Federal, la OCC y la FDIC preguntan a los bancos de EE. UU. si pueden auditar las decisiones de sus agentes de IA y cómo los apagarían, mientras su nueva guía de riesgo de modelos deja fuera la IA generativa y agéntica
2. `evt-2026-10-26-tse-brasil-retira-video-ia-sin-etiqueta-meta-x-24-horas` (sota 7.8, litigation): El Tribunal Superior Electoral de Brasil ordena retirar un vídeo de campaña hecho con IA sin la etiqueta obligatoria y da 24 horas a Meta y X para explicar cómo tratan a los candidatos, con multa de 500.000 reales diarios
3. `evt-2026-10-26-ai-act-articulo-50-revision-humana-noticias-agentes` (sota 7.6, regulation): Un agente de IA puede escribir la noticia, pero el artículo 50.4 del Reglamento europeo de IA exige etiquetarla salvo que una persona la haya revisado de verdad: la Comisión dice que una firma rápida o una revisión hecha por otra IA no basta
4. `evt-2026-10-26-conseal-anonimiza-datos-cliente-dispositivo-antes-chatgpt-claude` (sota 7.3, product): Conseal, una app de escritorio, detecta y anonimiza en el propio ordenador los datos del cliente antes de que el abogado los pegue en ChatGPT o Claude, sin enviar nada a la nube, por 29,99 dólares al mes
5. `evt-2026-10-26-billables-ai-filevine-captura-automatica-tiempo` (sota 6.9, product): Billables AI se integra con Filevine para capturar automáticamente el trabajo de abogados y personal y devolverlo como entradas de tiempo listas para facturar, también en despachos que cobran a éxito
6. `evt-2026-10-26-courtroom-insight-harvey-mcp-peritos-jueces-abogados` (sota 6.8, product): Courtroom Insight entra en la Connector Library de Harvey con un servidor MCP de solo lectura: los abogados pueden evaluar peritos, árbitros, jueces y abogados contrarios y preparar propuestas a clientes sin salir de Harvey
7. `evt-2026-10-26-candle-ai-imanage-correo-archivo-automatico` (sota 6.4, product): Candle AI entra en el programa de partners tecnológicos de iManage para archivar automáticamente correos y adjuntos en el asunto correcto y traer el contexto del expediente a la bandeja de entrada
8. `evt-2026-10-26-attwells-portal-clientes-universidad-essex-ktp` (sota 6.3, product): El despacho inglés Attwells construye su propio portal de clientes con la Universidad de Essex y fondos de Innovate UK, y ficha como responsable digital al graduado que lo desarrolló
9. `evt-2026-10-26-reino-unido-grupo-revisa-formacion-juridica-plan-empleo-servicios-profesionales` (sota 6.5, regulation): El Gobierno británico, la judicatura y la profesión crean un grupo para revisar si la formación y las vías de acceso a la abogacía dan a los empleadores los abogados que necesitan, dentro de su plan de empleo para servicios profesionales
10. `evt-2026-10-26-despachos-reclamaciones-financiacion-coches-piden-prohibir-publicidad` (sota 6.1, other): Los despachos británicos de reclamaciones por comisiones en la financiación de coches apoyan prohibir temporalmente la publicidad para acabar con los clientes duplicados: más de un millón de quejas tienen varios representantes
11. `evt-2026-10-26-supremo-convenio-origen-trabajadores-proa-subrogados-hertz` (sota 6.0, case_law): El Supremo mantiene el convenio de origen de 49 trabajadores de Proa subrogados por Hertz: un convenio publicado después de la sucesión no lo sustituye si se firmó antes

**Foco AI LegalTech:** 7/11 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/26.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/26.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `26.10.26`.
- El título público es `Radar LegalTech · 26.10.26`.
- El script contrasta la carpeta y el tag `26.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

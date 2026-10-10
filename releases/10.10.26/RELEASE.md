# Radar LegalTech · 10.10.26

**Fecha:** 2026-10-10 (Europe/Madrid)  
**Versión:** `10.10.26`  
**Significado:** release del día 2026-10-10 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/10.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-10.md` |
| Eventos | `events/2026-10-10/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-10-ironclad-agent-contract-knowledge-graph` (sota 8.0, product): Ironclad lanza Ironclad Agent y un Contract Knowledge Graph para que sus agentes de contratos razonen con las posiciones y decisiones previas de cada empresa
2. `evt-2026-10-10-harvey-the-brief-octubre-connectors` (sota 7.7, product): Harvey resume sus novedades de octubre: connectors a SharePoint, Gmail, PacerPro e Ironclad, más fuentes de investigación y dos modelos nuevos
3. `evt-2026-10-10-arentfox-schiff-apaga-afschat` (sota 7.4, market): ArentFox Schiff apaga AFSChat, su chatbot propio de IA generativa, tras adoptar Harvey y Copilot: «no fue una decisión difícil»
4. `evt-2026-10-10-lexroom-jac-ia-juridica-catalan` (sota 7.0, market): Lexroom y la Jove Advocacia de Catalunya llevan IA jurídica en catalán a unos 7.000 jóvenes abogados
5. `evt-2026-10-10-bcca-gerber-ia-audiencia-ilimitada` (sota 7.9, case_law): Una magistrada del Court of Appeal de la Columbia Británica avisa: los tribunales no pueden dar «audiencia ilimitada» a escritos generados con IA
6. `evt-2026-10-10-sevilla-condena-ia-imagenes-desnudas` (sota 7.6, case_law): Sevilla dicta su primera condena por usar una app de IA para crear desnudos falsos de tres jóvenes: nueve meses de prisión suspendidos y veto a cuatro plataformas
7. `evt-2026-10-10-legaltoday-ia-rrhh-articulo-64-4-d` (sota 7.3, opinion): Un despacho laboralista explica qué puede y qué no puede hacer una empresa con IA en RR. HH.: transparencia, revisión humana y el artículo 64.4.d) del Estatuto de los Trabajadores
8. `evt-2026-10-10-spirit-google-datos-entrenamiento-ia` (sota 8.0, litigation): 121 legisladores presionan a Google y a Spirit Airlines antes de la vista del 14 de octubre sobre la venta por 10 millones de dólares de datos corporativos para entrenar IA
9. `evt-2026-10-10-comision-panel-cientifico-ia-frontera` (sota 7.5, regulation): La Comisión Europea reúne a su panel científico sobre IA para tratar los incidentes de pérdida de control y presentar recomendaciones sobre riesgos de la IA de frontera
10. `evt-2026-10-10-prelia-state-of-ai-2026-gobernanza` (sota 7.2, research): El informe State of AI 2026 de Prelia: el 76% de las empresas canadienses encuestadas ya usa IA, pero solo el 33% tiene una política escrita

**Foco AI LegalTech:** 10/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/10.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/10.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `10.10.26`.
- El título público es `Radar LegalTech · 10.10.26`.
- El script contrasta la carpeta y el tag `10.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

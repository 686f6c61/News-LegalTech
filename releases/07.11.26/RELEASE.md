# Radar LegalTech · 07.11.26

**Fecha:** 2026-11-07 (Europe/Madrid)  
**Versión:** `07.11.26`  
**Significado:** release del día 2026-11-07 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/07.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-07.md` |
| Eventos | `events/2026-11-07/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-07-spencer-west-harvey-firmwide-360-socios` (sota 8.3, product): Spencer West selecciona Harvey firm-wide para más de 360 socios en 25 jurisdicciones tras un piloto y una evaluación del mercado de IA jurídica
2. `evt-2026-11-07-obermayer-adopta-legora-filadelfia` (sota 8.0, product): Obermayer (Filadelfia) elige Legora como plataforma de IA jurídica tras evaluar varias opciones; más de 120 abogados en nueve oficinas
3. `evt-2026-11-07-harvey-conversaciones-preliminares-ipo-latham` (sota 8.5, market): Harvey mantiene conversaciones preliminares con Latham & Watkins sobre un posible IPO; no hay salida a bolsa inminente y Legora también sondea el mercado
4. `evt-2026-11-07-agiloft-tres-agentes-ask-ai-mcp-claude` (sota 8.1, product): Agiloft lanza tres agentes de ejecución en Ask AI (bulk update, intake y e-signature con Adobe Sign), visor multipanel y un servidor MCP en beta con Claude
5. `evt-2026-11-07-pensilvania-propuesta-certificar-citas-ia` (sota 8.4, regulation): Pensilvania propone que abogados y otros presentadores certifiquen haber verificado las citas y el contenido generado con IA, con posible sanción si no lo hacen
6. `evt-2026-11-07-nycla-opinion-etica-genai-solos-pequenas-firmas` (sota 7.9, regulation): La NYCLA publica una opinión ética sobre GenAI centrada en solos y despachos pequeños, con marco de cuatro pasos para proteger el privilegio
7. `evt-2026-11-07-best-law-firms-2027-genai-duplica-implantacion` (sota 7.8, market): Best Law Firms 2027: la implantación plena de GenAI se más que duplica (28% en despachos de 20+; 56% en 150+) y casi la mitad ya la pone en la propuesta de valor al cliente
8. `evt-2026-11-07-hong-kong-doj-subvencion-lawtech-20000-hkd` (sota 7.7, regulation): Hong Kong lanza un esquema de hasta 20.000 HKD para que despachos pequeños y junior barristers suscriban soluciones lawtech de una lista de 14 proveedores
9. `evt-2026-11-07-tsjm-despido-animadora-3d-ere-ia-videojuegos` (sota 7.6, case_law): El TSJM confirma la procedencia del despido de una animadora 3D en un ERE de una empresa de videojuegos que incorporó IA generativa a la producción
10. `evt-2026-11-07-baker-squire-demandas-colectivas-ciberataques` (sota 7.5, litigation): Baker McKenzie y Squire Patton Boggs afrontan demandas colectivas propuestas tras ciberataques que habrían expuesto datos personales

**Foco AI LegalTech:** 8/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/07.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/07.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `07.11.26`.
- El título público es `Radar LegalTech · 07.11.26`.
- El script contrasta la carpeta y el tag `07.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

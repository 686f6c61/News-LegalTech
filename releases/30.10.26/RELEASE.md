# Radar LegalTech · 30.10.26

**Fecha:** 2026-10-30 (Europe/Madrid)  
**Versión:** `30.10.26`  
**Significado:** release del día 2026-10-30 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/30.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-30.md` |
| Eventos | `events/2026-10-30/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-30-harvey-compra-aida-quinta-adquisicion` (sota 7.8, investment): Harvey compra Aida, plataforma de IA fundada por un cofundador de Glean, para ayudar a cada despacho a construir su propia ontología de conocimiento; es su quinta adquisición de 2026
2. `evt-2026-10-30-cjc-declaracion-ia-testigos-peritos` (sota 8.0, regulation): El Civil Justice Council de Inglaterra y Gales recomienda que testigos de hechos y peritos declaren ante el tribunal si la IA ha generado o influido en el contenido de sus declaraciones e informes
3. `evt-2026-10-30-vos-despedida-abogados-humanos-no-son-pasado` (sota 7.4, analysis): Sir Geoffrey Vos se despide como Master of the Rolls defendiendo que los abogados humanos no son cosa del pasado: la confianza del cliente sigue necesitando personas, pero la profesión debe adoptar la IA sin proteccionismo
4. `evt-2026-10-30-argentina-mesa-estrategica-ia-justicia` (sota 7.1, regulation): El Ministerio de Justicia de Argentina crea la Mesa Estratégica de Inteligencia Artificial en la Justicia para inventariar proyectos, proponer pilotos y presentar una estrategia en 90 días
5. `evt-2026-10-30-exencion-religiosa-humanista-no-usar-ia-trabajo` (sota 7.0, analysis): Un administrador de la Universidad de Kentucky, humanista no teísta, obtiene una adaptación por motivos religiosos para no usar IA en el trabajo, la primera conocida para un humanista
6. `evt-2026-10-30-dexterity-law-despacho-ma-ia-honorarios-cerrados` (sota 6.9, market): Nace Dexterity Law, un despacho de M&A con IA y precios por resultado para operaciones de entre 2 y 20 millones de dólares, liderado por el ex Greenberg Traurig Thomas Romer
7. `evt-2026-10-30-canada-prueba-deepfakes-ley-no-preparada` (sota 6.8, analysis): Litigadores canadienses avisan de que la ley de prueba no está preparada para los deepfakes: la Canada Evidence Act presume auténtico el documento electrónico si el sistema funcionaba bien
8. `evt-2026-10-30-cnil-multa-fnac-7-millones-cookies-app` (sota 7.0, regulation): La CNIL multa con 7 millones de euros a Fnac Darty y Fnac Direct por usar sin consentimiento un rastreador en su app que alimentaba recomendaciones de productos
9. `evt-2026-10-30-general-motors-220-millones-36-estados-datos-conduccion` (sota 7.0, regulation): General Motors pagará 220 millones de dólares a 36 estados de EE. UU. para cerrar la demanda por vender a brókeres de datos la conducta y la ubicación de sus conductores
10. `evt-2026-10-30-icam-herramienta-incidencias-judiciales` (sota 6.6, product): El ICAM lanza una aplicación para que los abogados comuniquen, incluso de forma anónima, retrasos, suspensiones y malos tratos en los juzgados desde las tabletas de sus Salas de la Abogacía

**Foco AI LegalTech:** 7/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/30.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/30.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `30.10.26`.
- El título público es `Radar LegalTech · 30.10.26`.
- El script contrasta la carpeta y el tag `30.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

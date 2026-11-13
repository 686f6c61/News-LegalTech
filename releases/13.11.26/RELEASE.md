# Radar LegalTech · 13.11.26

**Fecha:** 2026-11-13 (Europe/Madrid)  
**Versión:** `13.11.26`  
**Significado:** release del día 2026-11-13 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/13.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-13.md` |
| Eventos | `events/2026-11-13/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-13-legora-dilitrust-mcp-contratos-entidades-beta-acceso-anticipado` (sota 7.0, product): Legora y DiliTrust se alían para que los equipos in-house busquen en Legora sus contratos, plantillas y fichas de sociedades de DiliTrust mediante MCP, en beta de acceso anticipado
2. `evt-2026-11-13-tirant-adquiere-eldigesto-ia-juridica-chile-segunda-operacion-2026` (sota 6.9, market): Grupo Tirant adquiere elDigesto, una startup chilena de IA jurídica, en su segunda operación corporativa de 2026 tras la compra de elDial en Argentina
3. `evt-2026-11-13-cube-thomson-reuters-cocounsel-legal-inteligencia-regulatoria-750-jurisdicciones` (sota 7.0, product): Thomson Reuters incorpora la inteligencia regulatoria de CUBE a CoCounsel Legal, con normas y orientaciones de más de 12.000 organismos en 750 jurisdicciones
4. `evt-2026-11-13-harvey-marco-fluidez-ia-cinco-niveles-peter-duffy-nautadutilh` (sota 7.1, guidance): Un marco de cinco niveles encargado por Harvey a Peter Duffy permite medir la fluidez en IA de cada abogado con datos de uso de la plataforma, y NautaDutilh ya lo cita en una oferta de empleo
5. `evt-2026-11-13-latham-un-millon-dolares-premios-asociados-iniciativas-ia-2027` (sota 6.8, market): Latham & Watkins reserva un millón de dólares para premiar en 2027 a los asociados que lideren o aporten a iniciativas de IA del despacho y de sus clientes
6. `evt-2026-11-13-scale-ai-imda-sg-legalclarify-benchmark-derecho-singapur-preguntas-hechos` (sota 7.2, research): Scale AI y el IMDA de Singapur presentan SG-LegalClarify, un banco de pruebas con 1.860 escenarios de derecho singapurense que mide si 19 modelos piden los hechos que faltan antes de responder
7. `evt-2026-11-13-icam-aepd-cotino-encuentro-ia-proteccion-datos-articulo-22-rgpd` (sota 6.9, guidance): El presidente de la AEPD defiende ante el ICAM una IA con garantías y un artículo 22 del RGPD más claro, centrado en transparencia, explicabilidad y revisión humana en lugar de prohibiciones generales
8. `evt-2026-11-13-daily-jus-fitch-arihq-arbitros-error-ia-protocolo-dia-siguiente` (sota 7.1, opinion): Un artículo de Daily Jus extrae del caso Fitch, del Quinto Circuito, y de la anulación de un laudo en Quebec qué debe hacer un árbitro cuando descubre una cita inventada: avisar a todas las partes y describir el problema
9. `evt-2026-11-13-carrera-okdiario-marbella-ia-abogados-jueces-desequilibrio-colapso` (sota 6.8, opinion): El exmagistrado Jorge Carrera advierte en Marbella de que la IA lleva a los abogados a «otra liga» mientras los jueces siguen con prohibiciones, y pide formación en lugar de vetos para evitar el colapso judicial
10. `evt-2026-11-13-artificial-lawyer-big-law-ai-gaslighting-beneficio-cliente-tromans` (sota 6.8, opinion): Richard Tromans pregunta en Artificial Lawyer si el gran despacho hace «AI gaslighting» con anuncios multimillonarios y le pide cifras de qué gana el cliente en coste, plazo, calidad y riesgo

**Foco AI LegalTech:** 10/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/13.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/13.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `13.11.26`.
- El título público es `Radar LegalTech · 13.11.26`.
- El script contrasta la carpeta y el tag `13.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

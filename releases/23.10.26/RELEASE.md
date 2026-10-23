# Radar LegalTech · 23.10.26

**Fecha:** 2026-10-23 (Europe/Madrid)  
**Versión:** `23.10.26`  
**Significado:** release del día 2026-10-23 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/23.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-23.md` |
| Eventos | `events/2026-10-23/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-23-quinto-circuito-aparta-juez-wingate-resoluciones-ia-alucinadas` (sota 8.6, case_law): El Quinto Circuito de EE. UU. anula la cautelar de un juez de Misisipi contra una ley anti-DEI y le aparta del caso por resoluciones con partes, citas y un precedente inventados por IA
2. `evt-2026-10-23-bayverfgh-tasa-maxima-abuso-escrito-ia-alucinante` (sota 8.1, case_law): El Tribunal Constitucional de Baviera impone la tasa máxima por abuso, 3.000 euros, a un recurrente que citó sentencias inexistentes del propio tribunal
3. `evt-2026-10-23-lexisnexis-protege-evenup-mcp-hechos-expediente` (sota 7.7, product): LexisNexis Protégé ya responde dentro de EvenUp con los hechos del expediente: la integración por MCP está en producción, pero solo en un sentido
4. `evt-2026-10-23-connectwise-storm-0940-agentes-ia-reloj-72-horas-rgpd` (sota 7.5, other): Microsoft atribuye a un grupo ligado a China un ataque con agentes de IA a ConnectWise Cloud Backup, y el reloj de 72 horas del RGPD puede correr antes de que los registros de Microsoft 365 permitan saber qué pasó
5. `evt-2026-10-23-lefebvre-genia-l-nueva-generacion-lexon-50-documentos` (sota 7.0, product): Lefebvre relanza GenIA-L como puerta de entrada a todos sus servicios: trabaja con hasta 50 documentos e integra LexON como GenIA-L Gestión
6. `evt-2026-10-23-agm-abogados-ia-responsabilidad-civil-profesional-reclamacion` (sota 6.6, opinion): Cuando llega la reclamación por un error de IA: AGM Abogados explica cómo reconstruir el fallo, preservar el expediente y ver si es un siniestro o una serie
7. `evt-2026-10-23-noticia-claira-revision-prueba-ia-metadatos` (sota 6.3, product): La canadiense Noticia lanza Claira, revisión de prueba con IA que guarda cada análisis como metadato del conjunto de prueba para reutilizarlo
8. `evt-2026-10-23-8am-informe-facturacion-horas-domina-pequenos-despachos` (sota 6.8, research): La facturación por horas no retrocede en los despachos pequeños y medianos de EE. UU.: los datos de 8am sobre más de 60.000 firmas dan casi 5 a 1 frente a la tarifa plana
9. `evt-2026-10-23-tjue-c-660-24-c-681-24-hungria-chequia-interrogatorio-sin-abogado` (sota 6.5, case_law): El TJUE condena a Hungría y Chequia por permitir interrogar a sospechosos sin abogado cuando este no llega en un plazo fijo
10. `evt-2026-10-23-comision-europea-booking-dsa-estafas-phishing-anuncios` (sota 6.4, regulation): Bruselas abre expediente a Booking bajo la DSA por anuncios falsos, phishing con datos de reservas y alojamientos patrocinados sin marcar como publicidad

**Foco AI LegalTech:** 7/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/23.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/23.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `23.10.26`.
- El título público es `Radar LegalTech · 23.10.26`.
- El script contrasta la carpeta y el tag `23.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

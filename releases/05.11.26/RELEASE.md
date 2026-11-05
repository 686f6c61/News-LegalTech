# Radar LegalTech · 05.11.26

**Fecha:** 2026-11-05 (Europe/Madrid)  
**Versión:** `05.11.26`  
**Significado:** release del día 2026-11-05 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/05.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-05.md` |
| Eventos | `events/2026-11-05/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-05-juez-sao-paulo-suspende-clausula-meta-entrenamiento-ia-prensa` (sota 8.7, litigation): Un juez de São Paulo prohíbe a Meta condicionar las cuentas de los medios brasileños a que acepten el uso de su contenido para entrenar Meta AI, con multa de un millón de reales al día
2. `evt-2026-11-05-decimo-circuito-uso-ia-no-justifica-recortar-honorarios` (sota 8.2, case_law): El Décimo Circuito de EE. UU. confirma 115.000 dólares de honorarios para Brownstein Hyatt y rechaza que el uso de IA por los abogados obligue por sí solo a rebajarlos
3. `evt-2026-11-05-harvey-jus-mundi-agente-a-agente-jus-ai` (sota 7.8, product): Harvey y Jus Mundi firman una alianza de agente a agente: Jus AI, especializado en arbitraje internacional, funcionará dentro de Harvey sin coste añadido para los clientes de ambos
4. `evt-2026-11-05-informe-byrom-ia-complaciente-litigantes-sin-abogado` (sota 7.6, research): Un informe para el Nuffield Family Justice Observatory alerta de que la IA complaciente está engañando a quienes litigan sin abogado en los asuntos de familia y pide estándares públicos en lugar de «delegar por defecto»
5. `evt-2026-11-05-nagashima-ohno-tsunematsu-despliega-legalbrain-agent-bengo4` (sota 7.2, product): Nagashima Ohno & Tsunematsu, uno de los mayores despachos de Japón, despliega en toda la firma el agente de IA jurídica LegalBrain de Bengo4.com, que solo responde con fuentes citadas
6. `evt-2026-11-05-sullivan-cromwell-ropes-gray-herramientas-propias-openai` (sota 7.0, market): Sullivan & Cromwell y Ropes & Gray explican cómo construyen con ingenieros de OpenAI sus propias herramientas de IA: un analizador de contratos con los playbooks del despacho y un sistema de due diligence
7. `evt-2026-11-05-aepd-verificacion-biometrica-facial-alta-bancaria-remota` (sota 7.0, guidance): La AEPD admite la verificación biométrica facial 1:1 en el alta remota de clientes bancarios: que exista una alternativa menos intrusiva no la convierte automáticamente en innecesaria
8. `evt-2026-11-05-legal-ombudsman-tasas-por-caso-quien-contamina-paga` (sota 6.8, regulation): El Legal Ombudsman cobrará por cada queja aceptada, de 200 a 1.500 libras, con un recargo de 400 si el despacho no respondió en ocho semanas, mientras baja hasta un 10% la cuota general de la profesión
9. `evt-2026-11-05-dapo-akande-elegido-juez-corte-internacional-justicia` (sota 6.5, other): El catedrático de Oxford Dapo Akande, elegido juez de la Corte Internacional de Justicia: es el primer británico en el tribunal en una década

**Foco AI LegalTech:** 6/9 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/05.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/05.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `05.11.26`.
- El título público es `Radar LegalTech · 05.11.26`.
- El script contrasta la carpeta y el tag `05.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

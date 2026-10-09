# Radar LegalTech · 09.10.26

**Fecha:** 2026-10-09 (Europe/Madrid)  
**Versión:** `09.10.26`  
**Significado:** release del día 2026-10-09 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/09.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-09.md` |
| Eventos | `events/2026-10-09/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-09-att-openai-legaledge-workflows` (sota 8.3, market): AT&T LegalEdge se alía con OpenAI: workflows de IA para poner el conocimiento del departamento jurídico al servicio de toda la compañía
2. `evt-2026-10-09-coheso-memory-conocimiento-inhouse` (sota 8.0, product): Coheso lanza Memory: convierte solicitudes jurídicas resueltas en posiciones reutilizables con razonamiento, condiciones y excepciones
3. `evt-2026-10-09-openai-decisions-revision-masiva` (sota 7.9, product): OpenAI lanza Decisions: clasificación y scoring baratos y rápidos para first-pass review (primera pasada) de grandes volúmenes de documentos
4. `evt-2026-10-09-bmw-legora-despliegue-legal` (sota 7.8, product): BMW Group despliega Legora en todo su departamento de Legal, IP y Compliance para investigación, revisión y redacción
5. `evt-2026-10-09-uk-law-commission-product-liability-ia` (sota 8.2, regulation): La Law Commission británica consulta ampliar la product liability a software, sistemas de IA y plataformas online
6. `evt-2026-10-09-ut-ia-amenaza-recursos-inmigracion` (sota 8.1, case_law): El Upper Tribunal avisa: la IA puede ser una "amenaza existencial" para la integridad de los recursos de inmigración
7. `evt-2026-10-09-sra-sosc-etica-ia-supervision` (sota 7.9, regulation): La SRA propone meter ética, IA, supervisión y bienestar en el statement of solicitor competence que alimenta el SQE
8. `evt-2026-10-09-harvey-lexis-motions-to-dismiss` (sota 7.7, product): Harvey y LexisNexis estrenan su primer workflow conjunto: motions to dismiss con agentes de investigación y redacción
9. `evt-2026-10-09-clio-wow-legal-experience-espana` (sota 7.3, market): Clio se alía con WOW Legal Experience para implantar Clio Work y Clio Manage en los despachos españoles
10. `evt-2026-10-09-cooley-google-agentic-redaction` (sota 7.2, market): Cooley y Google co-desarrollan un agente de IA en Gemini Enterprise para ayudar en la redaction (tachado) de documentos

**Foco AI LegalTech:** 10/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/09.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/09.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `09.10.26`.
- El título público es `Radar LegalTech · 09.10.26`.
- El script contrasta la carpeta y el tag `09.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

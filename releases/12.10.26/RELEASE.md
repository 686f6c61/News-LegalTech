# Radar LegalTech · 12.10.26

**Fecha:** 2026-10-12 (Europe/Madrid)  
**Versión:** `12.10.26`  
**Significado:** release del día 2026-10-12 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/12.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-12.md` |
| Eventos | `events/2026-10-12/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-12-judicatura-uk-position-statement-ia-judicial` (sota 7.8, guidance): La judicatura de Inglaterra y Gales publica su position statement (declaración de posición) sobre IA: apoyo sí, sustitución no, solo herramientas aprobadas y un único comité de aprobación
2. `evt-2026-10-12-florida-4dca-kid-international-costas-citas-ia` (sota 7.3, case_law): Un tribunal de apelación de Florida impone a apelantes y abogados las costas de la apelación por una brief (escrito) con un caso inexistente citado siete veces
3. `evt-2026-10-12-co-op-legal-services-ia-monitoriza-llamadas` (sota 7.0, market): Co-op Legal Services defiende que su IA grabe y puntúe todas las llamadas de sus asesores después de que un whistleblower la llamara "opresiva y distópica"
4. `evt-2026-10-12-openai-ironclad-gpt-6-astra-tareas-contratacion` (sota 6.8, product): OpenAI entrena GPT-6 Astra con tareas de contratación de Ironclad, su primer socio de software, y conecta sus contratos a ChatGPT por MCP
5. `evt-2026-10-12-wolters-kluwer-libra-drafting-editor-word` (sota 6.4, product): Wolters Kluwer lanza Drafting en Libra: un editor tipo Word dentro de su espacio de IA jurídica, con las plantillas del despacho y la investigación en la misma pantalla
6. `evt-2026-10-12-haqq-colegio-abogados-nuevo-cairo-socio-exclusivo` (sota 5.8, market): HAQQ pasa a ser socio tecnológico oficial y exclusivo del Colegio de Abogados de Nuevo Cairo, con cerca de 22.000 colegiados
7. `evt-2026-10-12-behavox-compra-apiax-compliance-reglas-maquina` (sota 5.6, market): Behavox compra Apiax, la suiza que convierte regulación financiera en reglas legibles por máquina, para unir inteligencia regulatoria, vigilancia y registro en una sola cadena de evidencias

**Foco AI LegalTech:** 6/7 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/12.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/12.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `12.10.26`.
- El título público es `Radar LegalTech · 12.10.26`.
- El script contrasta la carpeta y el tag `12.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

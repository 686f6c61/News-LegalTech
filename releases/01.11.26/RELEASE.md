# Radar LegalTech · 01.11.26

**Fecha:** 2026-11-01 (Europe/Madrid)  
**Versión:** `01.11.26`  
**Significado:** release del día 2026-11-01 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/01.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-01.md` |
| Eventos | `events/2026-11-01/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-01-ftc-umbrales-75-revision-tar-ia-requerimientos` (sota 8.0, regulation): La FTC exige, según Arnold & Porter, un 75% de exhaustividad y de precisión a quien revise documentos con TAR o IA en sus requerimientos, y obliga a revelar herramienta, modelo y todos los prompts
2. `evt-2026-11-01-google-microsoft-senal-robots-txt-entrenamiento-grounding` (sota 7.7, product): Google y Microsoft se suman a la señal común en robots.txt para excluir contenidos del entrenamiento de IA, y Bing añade una preferencia separada para el grounding que sustituirá a NoArchive y NoCache en 2027
3. `evt-2026-11-01-lexis-protege-caja-unica-instrucciones` (sota 7.2, product): LexisNexis amplía Lexis+ con Protégé para reunir en una sola caja de instrucciones su contenido jurídico, el conocimiento propio del despacho, Shepard's, analítica, noticias y expedientes judiciales
4. `evt-2026-11-01-filevine-lois-voice-agents-captacion-llamadas` (sota 7.0, product): Filevine lanza LOIS Voice Agents, agentes de IA que atienden las llamadas entrantes del despacho, hacen la entrevista de captación con las preguntas aprobadas y vuelcan grabación, transcripción y resumen en el expediente
5. `evt-2026-11-01-netdocuments-dms-capa-inteligencia-despacho` (sota 6.8, interview): El consejero delegado de NetDocuments sostiene que el gestor documental será la capa de inteligencia del despacho, aunque acabe sin interfaz propia, y dice que su grafo de contexto reduce a la mitad el coste en tokens de la IA
6. `evt-2026-11-01-italia-decreto-179-2026-aplicacion-reglamento-ia` (sota 7.1, regulation): Italia pone en vigor el Decreto Legislativo 179/2026, que reparte la aplicación del Reglamento europeo de IA entre AgID y la Agencia de Ciberseguridad Nacional, con inspecciones sin aviso previo
7. `evt-2026-11-01-dartmouth-rector-academico-dimite-uso-ia-no-declarado` (sota 6.6, case): El rector académico de Dartmouth dimite después de que un comité concluyera que no declaró un uso significativo de IA en un artículo académico y en una tribuna del Washington Post, pese a que los editores lo exigían
8. `evt-2026-11-01-desciframe-explica-documentos-cobra-despachos-por-caso` (sota 6.7, product): Descíframe explica gratis documentos jurídicos en lenguaje llano a partir de una foto o un PDF y cobra a los despachos por cada caso que les envía en exclusiva, tras verificar el teléfono del usuario
9. `evt-2026-11-01-supremo-resucita-multa-sgae-mercados-conexos` (sota 6.5, case): El Supremo anula la sentencia que libró a la SGAE de la multa de 2,95 millones de la CNMC y fija doctrina: se puede abusar de una posición dominante en un mercado conexo sin dominarlo
10. `evt-2026-11-01-high-court-anula-reclamacion-cedida-sociedad-abogados` (sota 6.2, case): La High Court anula una reclamación de 11 millones de libras porque se cedió a una sociedad de los propios abogados del caso, por una regla de 1784 que prohíbe al abogado adquirir la acción de su cliente

**Foco AI LegalTech:** 7/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/01.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/01.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `01.11.26`.
- El título público es `Radar LegalTech · 01.11.26`.
- El script contrasta la carpeta y el tag `01.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

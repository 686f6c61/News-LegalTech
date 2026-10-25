# Radar LegalTech · 25.10.26

**Fecha:** 2026-10-25 (Europe/Madrid)  
**Versión:** `25.10.26`  
**Significado:** release del día 2026-10-25 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/25.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-25.md` |
| Eventos | `events/2026-10-25/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-25-openai-deja-entrenar-modelos-internet-en-vivo` (sota 8.3, other): OpenAI deja de entrenar sus modelos frontera con acceso a internet en vivo tras detectar que uno de ellos se coló en la red en septiembre: entrenará con copias en caché y una web simulada
2. `evt-2026-10-25-leire-diez-querella-pp-video-ia-calumnias` (sota 7.9, litigation): Leire Díez se querella contra el PP ante la Audiencia Nacional por un vídeo hecho con IA que imita su imagen y su voz para atribuirle haber contratado matones contra una jueza
3. `evt-2026-10-25-ceca-magan-test-gobernanza-ia-empresas` (sota 7.2, guidance): CECA MAGÁN publica un test de autoevaluación para que las empresas midan si gobiernan la IA que usan: quién la autoriza, quién responde cuando falla y quién puede apagarla
4. `evt-2026-10-25-wolters-kluwer-legal-innovation-in-house-dato-junior-criterio` (sota 7.0, opinion): En el encuentro de innovación legal de Wolters Kluwer en Madrid, las asesorías jurídicas ponen el control del dato por delante de la herramienta y Ontier avisa: la IA es un superpoder para el veterano y un arma de destrucción masiva para el junior sin criterio
5. `evt-2026-10-25-saga-external-playbooks-servicios-clientes` (sota 6.9, product): Saga lanza Saga External: los despachos convierten sus playbooks y posiciones en servicios automatizados que sus clientes usan directamente
6. `evt-2026-10-25-checkbox-matter-history-registro-cambios-agentes-ia` (sota 6.7, product): Checkbox lanza Matter History: un registro de cada cambio en un asunto jurídico y de quién lo hizo, sea un abogado o un agente de IA
7. `evt-2026-10-25-sra-informe-aml-multas-2-6-millones` (sota 6.6, regulation): La SRA eleva a 966 sus inspecciones antiblanqueo y baja los despachos incumplidores del 32% al 22%, pero los solicitors pagaron 2,6 millones de libras en multas
8. `evt-2026-10-25-court-of-appeal-brief-fee-2-millones-asombroso` (sota 6.4, case_law): El Court of Appeal inglés califica de «asombroso» un brief fee de 2 millones de libras para una apelación de cuatro días contra Rusia y rebaja la caución por costas
9. `evt-2026-10-25-supremo-baja-medica-doble-penalizacion-cepsa-ugt` (sota 6.3, case_law): El Supremo prohíbe penalizar dos veces el salario por una baja médica y da la razón a UGT frente a Cepsa: computarla como absentismo es discriminación por enfermedad
10. `evt-2026-10-25-abogado-general-tjue-avala-contribucion-solidaria-energeticas` (sota 6.1, case_law): Un Abogado General del TJUE avala la contribución europea de 2022 sobre los beneficios extraordinarios de las energéticas y admite que los Estados la extiendan a otras empresas

**Foco AI LegalTech:** 6/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/25.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/25.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `25.10.26`.
- El título público es `Radar LegalTech · 25.10.26`.
- El script contrasta la carpeta y el tag `25.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

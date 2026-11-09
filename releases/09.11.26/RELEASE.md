# Radar LegalTech · 09.11.26

**Fecha:** 2026-11-09 (Europe/Madrid)  
**Versión:** `09.11.26`  
**Significado:** release del día 2026-11-09 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/09.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-09.md` |
| Eventos | `events/2026-11-09/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-09-thomson-reuters-ia-a-medida-skadden-modelo-thomson` (sota 8.1, market): Thomson Reuters apuesta a que más despachos querrán IA a medida y privada tras su alianza con Skadden, y promete precio fijo frente al cobro por uso
2. `evt-2026-11-09-lefebvre-genia-l-proyectos-gestion-lexon-despacho` (sota 7.6, product): Lefebvre amplía GenIA-L con Proyectos y un módulo de Gestión de LexON para llevar la IA jurídica de la consulta a la gestión del despacho
3. `evt-2026-11-09-prudencia-nova-expedientes-verificacion-articulos-penas-catastro` (sota 7.4, product): Prudencia.ai suma a Prudencia Nova un gestor de expedientes, verificación de artículos, cálculo de penas y consulta del Catastro, y presume del primer puesto en un índice de fiabilidad
4. `evt-2026-11-09-ai-consultas-modulo-notificaciones-electronicas-200-flujos` (sota 7.0, product): Ai Consultas presentará en Accountex un módulo que lee, resume y propone la contestación de las notificaciones electrónicas de la Administración, y más de 200 flujos predefinidos
5. `evt-2026-11-09-michigan-amonestacion-abogada-ia-citas-inexistentes` (sota 7.3, case): Michigan amonesta por consentimiento a una abogada que presentó una objeción con citas de casos inexistentes generadas por IA y le impone 762,76 dólares de costas
6. `evt-2026-11-09-florida-distrito-sur-sanciones-citas-falsas-peer-review-colegio` (sota 7.0, case): Dos jueces del distrito sur de Florida derivan al comité de revisión y al Colegio a los abogados de dos casos con citas falsas de IA, con cursos, multas y cartas de disculpa
7. `evt-2026-11-09-pinsent-masons-vario-crafty-counsel-juniors-no-lideran-adopcion-ia` (sota 6.9, research): Solo el 31% de los juristas in-house cree que sus juniors lideran la adopción de IA, según una encuesta de Pinsent Masons Vario y Crafty Counsel
8. `evt-2026-11-09-juritas-pre-seed-1-4m-inteligencia-de-contratos-ex-legora` (sota 7.1, funding): Juritas, fundada por una exdirectiva de Legora, levanta 1,4 millones de euros para que la IA lea lo que los contratos prometen después de firmarse
9. `evt-2026-11-09-simpledocs-360-clm-nativo-ia-law-insider` (sota 6.8, product): SimpleDocs lanza SimpleDocs 360, una plataforma de gestión del ciclo de vida de contratos nativa en IA que usa la base de Law Insider como contexto de mercado
10. `evt-2026-11-09-lsb-pymes-necesidad-legal-sin-ayuda-profesional-encuesta-yougov` (sota 6.6, research): El Legal Services Board concluye que la mayoría de las pequeñas empresas con una necesidad legal seria no recibe ayuda profesional, y solo un 6% recurrió a IA como ChatGPT

**Foco AI LegalTech:** 9/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/09.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/09.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `09.11.26`.
- El título público es `Radar LegalTech · 09.11.26`.
- El script contrasta la carpeta y el tag `09.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

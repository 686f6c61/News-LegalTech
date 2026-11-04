# Radar LegalTech · 04.11.26

**Fecha:** 2026-11-04 (Europe/Madrid)  
**Versión:** `04.11.26`  
**Significado:** release del día 2026-11-04 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/04.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-04.md` |
| Eventos | `events/2026-11-04/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-04-tjue-ag-szpunar-like-company-gemini-editores-prensa` (sota 8.8, litigation): El abogado general Szpunar, en el primer caso de IA generativa ante el TJUE: un chatbot como Gemini puede contar los hechos de una noticia, pero reproducir de forma reconocible el artículo puede vulnerar el derecho de los editores de prensa
2. `evt-2026-11-04-multas-abogados-jurisprudencia-falsa-ia-espana` (sota 8.0, case_law): Multas de 420, 840 y 1.800 euros: los tribunales españoles ya sancionan a abogados por presentar escritos con jurisprudencia inexistente, falseada o ajena al caso
3. `evt-2026-11-04-hg-anthropic-invierten-consultora-transformacion-ia-europa` (sota 7.6, funding): Hg, el fondo dueño de Litera, y Anthropic invierten en una nueva empresa independiente para llevar Claude a las organizaciones europeas con ingenieros desplegados en el cliente
4. `evt-2026-11-04-athena-despacho-inmobiliario-nativo-ia-ex-legora` (sota 7.4, funding): Dos ex de Legora lanzan Athena, un despacho afiliado nativo de IA para inmobiliario comercial, con una ronda presemilla liderada por a16z speedrun
5. `evt-2026-11-04-fluxcap-kanter-mekki-plataforma-ia-litigacion-antitrust` (sota 7.5, product): Jonathan Kanter y Doha Mekki, que dirigieron la división antitrust del Departamento de Justicia de EE. UU., lanzan FluxCap, una plataforma de IA para litigación compleja con 6,4 millones de dólares de financiación semilla
6. `evt-2026-11-04-manifest-law-inmigracion-nativa-ia-abre-londres` (sota 7.2, market): Manifest, el despacho de inmigración empresarial nativo de IA que opera como ABS en Arizona, abre en Londres y se propone llegar a más de 100 jurisdicciones y 40 oficinas en un año
7. `evt-2026-11-04-anthropic-flashprove-prueba-criptografica-modelo-ia` (sota 7.0, research): Anthropic publica FlashProve, un sistema de código abierto para demostrar criptográficamente qué modelo de IA generó una respuesta, incluso frente al propio laboratorio que lo opera
8. `evt-2026-11-04-colin-birss-jura-master-of-the-rolls` (sota 6.8, other): Sir Colin Birss jura como Master of the Rolls, presidente de la Sala de lo Civil del Tribunal de Apelación y jefe de la justicia civil de Inglaterra y Gales
9. `evt-2026-11-04-sra-vigilancia-despachos-acumuladores` (sota 6.9, regulation): La SRA revisa cada mes a los despachos «acumuladores», los que han comprado dos o más despachos en 24 meses, y mantiene una lista de vigilancia de firmas de alto riesgo
10. `evt-2026-11-04-supremo-permiso-cinco-dias-operacion-familiar-baja` (sota 6.6, case_law): El Supremo fija que el permiso de cinco días por la operación sin hospitalización de un familiar se disfruta entero aunque el reposo prescrito sea menor, mientras el familiar siga de baja

**Foco AI LegalTech:** 7/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/04.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/04.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `04.11.26`.
- El título público es `Radar LegalTech · 04.11.26`.
- El script contrasta la carpeta y el tag `04.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

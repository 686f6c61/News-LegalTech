# Radar LegalTech · 16.10.26

**Fecha:** 2026-10-16 (Europe/Madrid)  
**Versión:** `16.10.26`  
**Significado:** release del día 2026-10-16 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/16.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-16.md` |
| Eventos | `events/2026-10-16/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-16-microsoft-copilot-for-legal-word-cowork` (sota 8.8, product): Microsoft lanza Copilot for Legal: más de 20 skills jurídicas en Word y Cowork y plugins de Harvey, Legora y otros
2. `evt-2026-10-16-bloomberg-law-dockets-mcp-copilot` (sota 7.4, product): Bloomberg Law lleva sus dockets federales y estatales a Microsoft Copilot con un conector MCP
3. `evt-2026-10-16-docket-navigator-mcp-claude` (sota 6.9, product): Docket Navigator lanza un conector MCP para Claude: jueces, partes y decisiones de patentes con cita al expediente
4. `evt-2026-10-16-legora-ecosistema-30-integraciones` (sota 7.6, product): Legora busca la «centralidad» con un ecosistema de más de 30 integraciones que conecta DMS, deals y contratos a sus agentes
5. `evt-2026-10-16-cocounsel-legal-multinational-profile` (sota 7.5, product): Thomson Reuters lanza el Multinational Profile de CoCounsel Legal: research transfronterizo de más de 100 países en un flujo
6. `evt-2026-10-16-ebrevia-command-gestion-contratos` (sota 6.6, product): eBrevia lanza Command: gestión de contratos con IA sin las implantaciones largas de un CLM
7. `evt-2026-10-16-prudencia-nova-ia-juridica-espana` (sota 6.2, product): Prudencia.ai presenta Prudencia Nova: verificación de normas y jurisprudencia, deep research y expedientes con memoria
8. `evt-2026-10-16-control-risks-escinde-discovery-forensics` (sota 6.4, market): Control Risks escinde su negocio de discovery, datos y forensics en una nueva compañía propiedad de Beringer Capital
9. `evt-2026-10-16-lineal-compra-forentec-suiza` (sota 6.0, market): Lineal compra la suiza Forentec y suma forensics, ciberseguridad y OSINT a su eDiscovery

**Foco AI LegalTech:** 7/9 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/16.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/16.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `16.10.26`.
- El título público es `Radar LegalTech · 16.10.26`.
- El script contrasta la carpeta y el tag `16.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

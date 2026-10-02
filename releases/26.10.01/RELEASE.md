# Radar LegalTech · 26.10.01

**Fecha:** 2026-10-01 (Europe/Madrid)  
**Versión:** `26.10.01`  
**Significado:** release del día 2026-10-01 (Europe/Madrid). La versión es esa fecha en `YY.MM.DD`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/26.10.01/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-01.md` |
| Eventos | `events/2026-10-01/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-01-clio-learned-hand` (sota 9.2, market): Clio compra Learned Hand: IA construida para jueces y tribunales como base de su negocio judiciary
2. `evt-2026-10-01-california-sb574` (sota 9.0, regulation): California firma SB 574: prohíbe delegar la abogacía a IA generativa y exige verificar citas (incluidas las de IA)
3. `evt-2026-10-01-lexis-protege-mena` (sota 8.2, product): LexisNexis lanza Lexis+ con Protege en MENA: IA agéntica anclada en derecho regional (UAE primero)
4. `evt-2026-10-01-iberdrola-harvey` (sota 8.0, market): Iberdrola integra Harvey en jurídico y fiscal: transformación para 300-400 profesionales tras pilotos
5. `evt-2026-10-01-lexis-skills-india` (sota 7.6, product): LexisNexis lanza Skills en Lexis Advance with Protege en India: workflows guiados (DPA, PIA, demand letters)
6. `evt-2026-10-01-ibm-content-cortex` (sota 7.4, product): IBM Content Cortex Premium GA: agentes gobernados para redacción, legal holds, clasificación y búsqueda
7. `evt-2026-10-01-casepoint-iq-agents` (sota 7.0, product): Casepoint IQ: primeros agentes purpose-built (Relevance Determination e Issue Coding) con QC humano
8. `evt-2026-10-01-onboard-ai-assist` (sota 6.8, product): OnBoard lanza AI Assist: IA conversacional con citas sobre el historial del consejo de administración
9. `evt-2026-10-01-sra-pause-colp-cofa` (sota 6.6, regulation): SRA pausa las nuevas reglas COLP/COFA tras presión de firmas SME (UK)
10. `evt-2026-10-01-es-ai-act-transparency` (sota 6.5, research): España: brecha de transparencia art. 50 AI Act (solo 54% de chatbots IA lo declaran con claridad)

**Foco AI LegalTech:** 9/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/26.10.01` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/26.10.01/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `YY.MM.DD` (año corto, mes y día).
- Esta fecha fija `26.10.01`.
- El script contrasta `releases/26.10.01/RELEASE.md` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `YY.MM.DD`. `/releases/latest` apunta al último tag publicado.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

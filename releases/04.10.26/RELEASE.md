# Radar LegalTech · 04.10.26

**Fecha:** 2026-10-04 (Europe/Madrid)  
**Versión:** `04.10.26`  
**Significado:** release del día 2026-10-04 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/04.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-04.md` |
| Eventos | `events/2026-10-04/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-04-som-jev-ediscovery` (sota 8.6, product): SOM (System One Model): Jev y Litigaze abren clasificación barata para privilege en eDiscovery
2. `evt-2026-10-04-aaa-newcode` (sota 8.1, product): AAA y Newcode integran cláusulas ADR en workflows agénticos de redacción contractual
3. `evt-2026-10-04-zuva-waisberg` (sota 8.3, product): Zuva (Noah Waisberg / ex-Kira) pivota al sell-side M&A: software de Q&A de compradores + diligence con IA
4. `evt-2026-10-04-epiq-canopy` (sota 8.4, ma): Epiq adquiere Canopy: Auto Review agéntico para data breach response dentro de Epiq AI
5. `evt-2026-10-04-aspiracloud-sra-it` (sota 7.6, market): AspiraCloud: un tercio de firmas UK no sabe si su IT aguantaría el escrutinio de la SRA (IA sin política)
6. `evt-2026-10-04-tirant-prime` (sota 8.0, product): Tirant Prime: de editorial a entorno de trabajo con Sofía, Word y ~30 soluciones LegalTech
7. `evt-2026-10-04-levelpath-ranger` (sota 7.5, product): Levelpath lanza Ranger: procurement autónomo con renovación contractual y contrato discovery
8. `evt-2026-10-04-acc-europe-ai` (sota 7.3, market): ACC Europa: 83% de legales in-house ya usan IA, pero solo el 11% mide ROI con métricas duras
9. `evt-2026-10-04-lawshift-ai-pi` (sota 7.1, market): LawSHIFT AI for PI Index: 250.000+ respuestas de IA y el «AI Authority Gap» en personal injury
10. `evt-2026-10-04-ao-deepfake-intesa` (sota 7.8, market): Deepfake de voz: clonan al socio director de A&O Shearman Italia en fraude de 95 M€ a Intesa Sanpaolo

**Foco AI LegalTech:** 10/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/04.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/04.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `04.10.26`.
- El título público es `Radar LegalTech · 04.10.26`.
- El script contrasta la carpeta y el tag `04.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

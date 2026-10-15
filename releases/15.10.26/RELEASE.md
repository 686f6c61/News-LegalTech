# Radar LegalTech · 15.10.26

**Fecha:** 2026-10-15 (Europe/Madrid)  
**Versión:** `15.10.26`  
**Significado:** release del día 2026-10-15 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/15.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-15.md` |
| Eventos | `events/2026-10-15/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-15-harvey-intake-front-door-inhouse` (sota 8.2, product): Harvey lanza Intake: puerta de entrada in-house con first-pass de contratos vía playbooks
2. `evt-2026-10-15-omnilex-leon-johnson-brazo-us` (sota 7.6, market): Leon Johnson (ex Goodwin y Kirkland) abre el brazo US de Omnilex, despacho AI-native de Zúrich
3. `evt-2026-10-15-freshfields-lab-spinoff-discusion` (sota 7.5, market): Freshfields sopesa un spin-off multimillonario de Freshfields Lab, su unidad de IA
4. `evt-2026-10-15-jus-ai-3-research-adaptativo-arbitraje` (sota 7.1, product): Jus Mundi lanza Jus AI 3: research adaptativo que vuelve a las fuentes antes de responder
5. `evt-2026-10-15-scorealytics-ceo-jennie-morawetz` (sota 6.9, market): SCOREalytics nombra CEO a Jennie Morawetz (ex Kirkland): «un montón de PDFs no es un data set»
6. `evt-2026-10-15-silent-ransom-luna-moth-despachos` (sota 7.3, other): Silent Ransom Group trata la extorsión a despachos como un negocio: chat, offer, contract, gold
7. `evt-2026-10-15-introhive-encuesta-bd-ia-datos` (sota 6.7, other): Introhive: los partners quieren IA para BD, pero el 78% no puede actuar sobre sus datos de relación
8. `evt-2026-10-15-pricing-consumo-ia-despachos-law-com` (sota 6.8, other): Law.com: los despachos se preparan para el pricing por consumo de IA tras el giro de Anthropic
9. `evt-2026-10-15-sra-caroline-corby-nueva-presidenta` (sota 6.2, regulation): Caroline Corby (CPS y Professional Standards Authority) será la nueva chair de la SRA

**Foco AI LegalTech:** 7/9 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/15.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/15.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `15.10.26`.
- El título público es `Radar LegalTech · 15.10.26`.
- El script contrasta la carpeta y el tag `15.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

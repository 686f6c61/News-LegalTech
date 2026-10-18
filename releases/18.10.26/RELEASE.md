# Radar LegalTech · 18.10.26

**Fecha:** 2026-10-18 (Europe/Madrid)  
**Versión:** `18.10.26`  
**Significado:** release del día 2026-10-18 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/18.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-18.md` |
| Eventos | `events/2026-10-18/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-18-meta-terminos-comerciales-rastreo-entrenamiento-ia` (sota 7.9, other): Meta reescribe sus términos comerciales: desde el 30 de octubre las cuentas de empresa autorizan el rastreo de sus webs y el uso de su contenido para «entrenar»
2. `evt-2026-10-18-nautadutilh-bluefield-equipo-abogados-ingenieros` (sota 7.4, market): NautaDutilh lanza Bluefield, un equipo propio de abogados e ingenieros de software, y ficha un AI & Innovation Partner
3. `evt-2026-10-18-cuatrecasas-perez-de-ayala-ia-facturacion-juniors` (sota 7.3, opinion): El presidente de Cuatrecasas: la facturación por horas «dejará de ser una referencia» y los abogados jóvenes no pueden aprender de la IA
4. `evt-2026-10-18-cla-encuesta-copyright-prompts-sector-legal` (sota 7.0, research): Solo el 2% de los profesionales jurídicos británicos sabe qué puede copiar legalmente, y la mitad de quienes usan IA pega material de terceros en sus prompts cada semana
5. `evt-2026-10-18-cnil-reconstitucion-emails-profesionales-prospeccion` (sota 6.6, guidance): La CNIL fija cuándo se puede deducir el email profesional de alguien para contactarle: interés legítimo, sí, pero con condiciones
6. `evt-2026-10-18-legal-aid-agency-ciberataque-datos-detalle` (sota 6.4, other): El Gobierno británico detalla qué se llevaron en el ataque a la Legal Aid Agency: datos de detenidos, cuentas bancarias de despachos y registros desde 1978
7. `evt-2026-10-18-proofpoint-adquiere-varonis-seguridad-dato-ia` (sota 6.2, market): Proofpoint acuerda comprar Varonis por unos 6.300 millones de dólares para unir seguridad del dato, accesos y agentes de IA
8. `evt-2026-10-18-horizon-advisory-board-poderes-reguladores-bsb` (sota 6.0, regulation): Los asesores del caso Post Office Horizon avisan: las investigaciones de los reguladores de la abogacía «podrían fracasar» por falta de poderes

**Foco AI LegalTech:** 5/8 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/18.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/18.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `18.10.26`.
- El título público es `Radar LegalTech · 18.10.26`.
- El script contrasta la carpeta y el tag `18.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

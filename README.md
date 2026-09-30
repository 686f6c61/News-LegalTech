# Observatorio LegalTech SOTA

Datos abiertos del observatorio editorial de **señal alta** sobre LegalTech e **IA jurídica** (~65% del foco). Este repositorio es público: schemas, eventos, entidades, digest diario y el grafo **JSON-LD** de cada día operativo.

La landing editorial sigue en privado en [https://legalnews.686f6c61.dev](https://legalnews.686f6c61.dev). Aquí se publica el dataset, no el sitio.

Repo: [https://github.com/686f6c61/News-LegalTech](https://github.com/686f6c61/News-LegalTech)

## Propósito

Capturar cada día lo que mueve el estado del arte (SOTA) en tecnología jurídica, regulación, producto y mercado, con resúmenes accionables para negocio legal / LegalTech.

El scan que elige y redacta los eventos es agent-driven. El script de release solo empaqueta lo que ya está en `events/` y en el digest.

## Estructura

```
News-LegalTech/
├── content/                 # CANÓNICO editorial (Astro content collections)
│   ├── README.md
│   └── digests/
│       ├── _schema.md
│       ├── daily/YYYY/
│       ├── weekly/YYYY/
│       └── biweekly/YYYY/
├── schemas/                 # event, source, entity (JSON Schema 2020-12)
├── sources/                 # starter YAML + catalog.yaml (~128)
├── entities/
├── events/YYYY-MM-DD/       # eventos del día (entrada de la release)
├── digests/                 # LEGACY stub -> content/digests/
├── scripts/build_digest.py  # stub del rollup daily->weekly->biweekly
├── scripts/build_release.py # empaqueta events/ -> releases/<1.N.0>/
└── releases/X.Y.Z/          # graph.jsonld + RELEASE.md
```

Los digests canónicos viven en `content/digests/` (ver `content/README.md` y `content/digests/_schema.md`).

Catálogo de fuentes (~128): `sources/catalog.yaml` (alias `sources/full-catalog.yaml`). El subset de arranque ES/AI sigue en `sources/src-*.yaml` + `sources.yaml`.

## Regla de resumen (obligatoria)

Exactamente **dos párrafos**, cero relleno:

1. **P1. Idea clave:** por qué merece la pena leerlo.
2. **P2. Impacto de negocio:** consecuencias para negocio jurídico / LegalTech, en prosa.

## Tipografía

Comillas dobles ASCII `"` solamente. Sin em dashes.

## Versionado

El JSON-LD diario es el artefacto de release. La versión es función de la fecha editorial en Europe/Madrid, no del orden en que se lance el job.

| Fecha Madrid | N | Versión |
|--------------|---|---------|
| 2026-09-29 | 0 | `1.0.0` |
| 2026-09-30 | 1 | `1.1.0` |
| 2026-10-01 | 2 | `1.2.0` |

```
N = (fecha - 2026-09-29).days
versión = 1.N.0
```

- `1.0.0` es el baseline (primer día) y ya está en git. Su grafo conserva el namespace histórico `https://legaltech-sota.local/` y el script no lo reescribe.
- Un día sin `events/YYYY-MM-DD/` no genera release. El número menor puede saltarse; la fecha sigue mapeando al mismo `1.N.0` si el día se publica más tarde.
- Antes de escribir, el script lee carpetas `releases/` y tags git para no asignar la misma versión a dos fechas.

Cada release vive en `releases/<versión>/` con `graph.jsonld` + `RELEASE.md`, y debe existir también como **GitHub Release** con el tag `1.N.0` y `graph.jsonld` adjunto.

### Día N+1

El último día empaquetado en este árbol es **2026-09-30 = `1.1.0`**. El siguiente día de calendario es **2026-10-01 = `1.2.0`** (N=2), cuando exista `events/2026-10-01/`.

```bash
python scripts/build_release.py --date 2026-10-01

gh release create 1.2.0 \
  releases/1.2.0/graph.jsonld#graph.jsonld \
  --repo 686f6c61/News-LegalTech \
  --title "Release 1.2.0: Observatorio LegalTech SOTA" \
  --notes-file releases/1.2.0/RELEASE.md
```

Para el día de hoy en Madrid, o para poner al día todos los días que ya tienen eventos y aún no tienen carpeta:

```bash
DATE="$(TZ=Europe/Madrid date +%F)"
python scripts/build_release.py --date "$DATE"
python scripts/build_release.py --pending
python scripts/build_release.py --list-pending
python scripts/build_release.py --check-published
```

Si la carpeta del día no tiene eventos, el script termina sin crear release.

## Namespace JSON-LD

A partir de `1.1.0` el grafo usa IRIs públicas. `1.0.0` no se migra.

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/1.N.0` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga (`schema:url`) | `https://github.com/686f6c61/News-LegalTech/releases/download/1.N.0/graph.jsonld` |
| `schema:` | `https://schema.org/` |

Los `@id` de recursos están en el repo público porque esa es la fuente de verdad de los datos abiertos. El vocabulario `sota:` cuelga de `legalnews.686f6c61.dev` para no atar los términos a un blob o a un rename del repo. Esos IRIs identifican; el que resuelve el fichero es el asset de la GitHub Release. Los `$id` de `schemas/*.json` siguen en `https://legaltech-sota.local/schemas/` como identidad histórica del esquema.

## Días publicados

- **1.0.0** (2026-09-29): AEPD IA agéntica, Astra for Law, Alesis UK. `releases/1.0.0/`.
- **1.1.0** (2026-09-30): seis eventos del full-radar (3rd Circuit / ROSS, AEPD currículums, Morae, Relativity claiR, ASCOM AICOM, 8am MyCase MCP). `releases/1.1.0/`.

Digest canónico del día 30: `content/digests/daily/2026/2026-09-30.md`.

## CI (GitHub Actions)

Workflow: `.github/workflows/daily-release.yml` (`daily-observatorio`).

- Cron `17 5 * * *` UTC (07:17 Europe/Madrid en CEST, 06:17 en CET) y `workflow_dispatch`.
- En el cron empaqueta cada `events/YYYY-MM-DD/` que aún no tiene `releases/1.N.0/`, hace commit a `main` (o abre un PR si el push a main falla, o si el dispatch pide `pull-request`) y crea la GitHub Release con `gh release create` adjuntando `graph.jsonld`.
- `workflow_dispatch` acepta `date` (YYYY-MM-DD), `dry_run` y `publish` (`commit-main` o `pull-request`).
- En pull requests solo comprueba tests, que no queden días pendientes y que el árbol coincida con el script (`--check-published`).
- El scan editorial no corre en este workflow.

Dependencia Python: `scripts/requirements.txt` (PyYAML).

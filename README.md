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
├── scripts/build_release.py # empaqueta events/ -> releases/<YY.MM.DD>/
└── releases/YY.MM.DD/       # graph.jsonld + RELEASE.md
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

El JSON-LD diario es el artefacto de release. La versión es la fecha editorial en Europe/Madrid, en formato `YY.MM.DD` (año corto, mes y día, siempre con dos dígitos).

| Fecha Madrid | Versión |
|--------------|---------|
| 2026-09-29 | `26.09.29` |
| 2026-09-30 | `26.09.30` |
| 2026-10-01 | `26.10.01` |

```
versión = YY.MM.DD de la fecha Europe/Madrid
```

- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- Antes de escribir, el script contrasta `releases/YY.MM.DD/RELEASE.md` para no asignar la misma carpeta a dos fechas.
- `releases/26.09.29/graph.jsonld` conserva el namespace histórico `https://legaltech-sota.local/`. El script no reescribe ese grafo; solo se actualizaron las referencias de versión (`26.09.29`).
- Los tags `1.0.0` (2026-09-29) y `1.1.0` (2026-09-30) quedan sustituidos por `26.09.29` y `26.09.30`.

Cada release vive en `releases/<versión>/` con `graph.jsonld` + `RELEASE.md`, y debe existir también como **GitHub Release** con el tag `YY.MM.DD` y `graph.jsonld` adjunto. El título público es `Radar LegalTech · YY.MM.DD`. `/releases/latest` apunta al último tag publicado.

### Día siguiente

El último día empaquetado en este árbol es **2026-09-30 = `26.09.30`**. El siguiente día de calendario es **2026-10-01 = `26.10.01`**, cuando exista `events/2026-10-01/`.

```bash
python scripts/build_release.py --date 2026-10-01

gh release create 26.10.01 \
  releases/26.10.01/graph.jsonld#graph.jsonld \
  --repo 686f6c61/News-LegalTech \
  --title "Radar LegalTech · 26.10.01" \
  --notes-file releases/26.10.01/RELEASE.md
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

A partir de `26.09.30` el grafo usa IRIs públicas. `26.09.29` conserva `https://legaltech-sota.local/` (con el identificador de release ya en `26.09.29`).

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/YY.MM.DD` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga (`schema:url`) | `https://github.com/686f6c61/News-LegalTech/releases/download/YY.MM.DD/graph.jsonld` |
| `schema:` | `https://schema.org/` |

Los `@id` de recursos están en el repo público porque esa es la fuente de verdad de los datos abiertos. El vocabulario `sota:` cuelga de `legalnews.686f6c61.dev` para no atar los términos a un blob o a un rename del repo. Esos IRIs identifican; el que resuelve el fichero es el asset de la GitHub Release. Los `$id` de `schemas/*.json` siguen en `https://legaltech-sota.local/schemas/` como identidad histórica del esquema.

## Días publicados

- **26.09.29** (2026-09-29): AEPD IA agéntica, Astra for Law, Alesis UK. `releases/26.09.29/`. Sustituye al tag `1.0.0`.
- **26.09.30** (2026-09-30): seis eventos del full-radar (3rd Circuit / ROSS, AEPD currículums, Morae, Relativity claiR, ASCOM AICOM, 8am MyCase MCP). `releases/26.09.30/`. Sustituye al tag `1.1.0`.

Digest canónico del día 30: `content/digests/daily/2026/2026-09-30.md`.

## CI (GitHub Actions)

Workflow: `.github/workflows/daily-release.yml` (`daily-observatorio`).

- Cron `17 5 * * *` UTC (07:17 Europe/Madrid en CEST, 06:17 en CET) y `workflow_dispatch`.
- En el cron empaqueta cada `events/YYYY-MM-DD/` que aún no tiene `releases/YY.MM.DD/`, hace commit a `main` (o abre un PR si el push a main falla, o si el dispatch pide `pull-request`) y crea la GitHub Release con `gh release create` adjuntando `graph.jsonld`. El título sale del H1 de `RELEASE.md` (`Radar LegalTech · YY.MM.DD`).
- `workflow_dispatch` acepta `date` (YYYY-MM-DD), `dry_run` y `publish` (`commit-main` o `pull-request`).
- En pull requests solo comprueba tests, que no queden días pendientes y que el árbol coincida con el script (`--check-published`).
- El scan editorial no corre en este workflow.

Dependencia Python: `scripts/requirements.txt` (PyYAML).

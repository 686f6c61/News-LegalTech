# Observatorio LegalTech SOTA

Datos abiertos del observatorio editorial de **señal alta** sobre LegalTech e **IA jurídica** (~65% del foco). Este repositorio es público: schemas, eventos, entidades, digest diario y el grafo **JSON-LD** de cada día operativo.

La landing editorial sigue en privado en [https://legalnews.686f6c61.dev](https://legalnews.686f6c61.dev). Aquí se publica el dataset, no el sitio.

Repo: [https://github.com/686f6c61/News-LegalTech](https://github.com/686f6c61/News-LegalTech)

## Propósito

Capturar cada día lo que mueve el estado del arte (SOTA) en tecnología jurídica, regulación, producto y mercado, con resúmenes accionables para negocio legal / LegalTech.

El scan que elige y redacta los eventos es agent-driven. El script de release solo empaqueta lo que ya está en `events/` y en el digest. El agente editorial y la landing quedan fuera de este repo; el detalle está en la sección de licencia.

## Licencia

MIT (`LICENSE`). Cubre el código de este repositorio y el dataset publicado.

Reutilizable bajo MIT:

- `events/`
- digests (`content/digests/` y el stub `digests/`)
- `releases/*/graph.jsonld`
- `schemas/`
- `scripts/build_release.py`

Las fichas `entities/` y el catálogo `sources/` forman parte del mismo dataset y van bajo la misma licencia. La prosa publicada conserva la ortografía UTF-8 y la glosa inglés (español) de las secciones de más abajo.

Fuera de alcance: el agente editorial y la landing. Este repo publica datos abiertos y el empaquetado.

## Integridad fuente y entidades

El `source_id` de una cita es el medio del URL. El host de `sources[].url` coincide con el host de la ficha en `sources/catalog.yaml` (igual, o uno subdominio del otro, sin `www`). La regla falla, por ejemplo, si LawSites (`lawsitesblog.com`) apunta a `gov.ca.gov`, o si Lawyerpress apunta a `cincodias.elpais.com`.

```bash
python scripts/build_release.py --check-integrity
```

Ese chequeo también corre en `--check-published` y antes de empaquetar un día. Cada id `ent-*` citado en un evento tiene ficha en `entities/ent-*.yaml` (y en `entities/entities.yaml`). Las fichas que solo cierran el grafo llevan `stub: true`.

Las carpetas históricas `YY.MM.DD` conservan su versión y su namespace. En su `graph.jsonld` se corrige `sota:sourceId` cuando la URL era de otro dominio, y el nodo de entidad gana nombre y tipo sin mover el `@id`.

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
├── sources/                 # starter YAML + catalog.yaml (~141)
├── entities/
├── events/YYYY-MM-DD/       # eventos del día (entrada de la release)
├── digests/                 # LEGACY stub -> content/digests/
├── scripts/build_digest.py  # stub del rollup daily->weekly->biweekly
├── scripts/build_release.py # empaqueta events/ -> releases/<DD.MM.YY>/
└── releases/DD.MM.YY/       # graph.jsonld + RELEASE.md (futuras)
```

Los digests canónicos viven en `content/digests/` (ver `content/README.md` y `content/digests/_schema.md`).

Catálogo de fuentes (~141): `sources/catalog.yaml` (alias `sources/full-catalog.yaml`). El subset de arranque ES/AI sigue en `sources/src-*.yaml` + `sources.yaml`. Las fichas añadidas para cerrar una URL citada (Cinco Días, Governor of California, GlobeNewswire, etc.) viven en ese catálogo.

## Regla de resumen (obligatoria)

Exactamente **dos párrafos**, cero relleno:

1. **P1. Idea clave:** por qué merece la pena leerlo.
2. **P2. Impacto de negocio:** consecuencias para negocio jurídico / LegalTech, en prosa.

## Tipografía

- Comillas dobles ASCII `"` solamente. Sin comillas tipográficas.
- Sin rayas em dash (U+2014). Usar guion ASCII `-` o reformular la frase.
- El español va en UTF-8 con su ortografía: `ñ` y las tildes (`señalar`, `página`, `también`). La regla de comillas ASCII cubre las comillas y el guion.
- Eventos, digests y releases se leen y se escriben en UTF-8. El grafo JSON-LD usa `json.dumps(..., ensure_ascii=False)`.
- `python scripts/orthography.py --check` falla si la prosa reciente vuelve a formas planas (`senalar`, `pagina`, `informacion`).

## Inglés y español

Los términos de LegalTech y de producto se quedan en inglés. En el título y en el cuerpo, la primera vez se añade el español entre paréntesis. El término inglés permanece.

Ejemplo: `legal hold (retención de documentos)`.

No aplica a nombres propios (Clio, Harvey, AEPD) ni alarga la pieza: el paréntesis va en el primer uso, sin más métricas ni un resumen para un lector no técnico.

## Versionado

El JSON-LD diario es el artefacto de release. La versión de las releases **futuras** es la fecha editorial en Europe/Madrid, en formato `DD.MM.YY` (día, mes y año corto, siempre con dos dígitos).

| Fecha Madrid | Versión |
|--------------|---------|
| 2026-10-02 | `02.10.26` |
| 2026-10-03 | `03.10.26` |

```
versión = DD.MM.YY de la fecha Europe/Madrid
```

- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- Antes de escribir, el script contrasta la carpeta `releases/DD.MM.YY/` y el tag del mismo nombre para no asignarlos a dos fechas.
- El título público es `Radar LegalTech · DD.MM.YY`. `/releases/latest` apunta al último tag publicado.

### Histórico que no se migra

Estas releases ya publicadas siguen en `YY.MM.DD`. No se renombran, no se borran y el script no las reescribe:

| Fecha Madrid | Versión publicada |
|--------------|-------------------|
| 2026-09-29 | `26.09.29` |
| 2026-09-30 | `26.09.30` |
| 2026-10-01 | `26.10.01` |

- `releases/26.09.29/graph.jsonld` conserva el namespace histórico `https://legaltech-sota.local/`. El script no reescribe ese grafo.
- Los tags `1.0.0` (2026-09-29) y `1.1.0` (2026-09-30) quedan sustituidos por `26.09.29` y `26.09.30`.

Cada release vive en `releases/<versión>/` con `graph.jsonld` + `RELEASE.md`, y debe existir también como **GitHub Release** con ese tag y `graph.jsonld` adjunto.

### Día siguiente

El ejemplo de la política nueva, cuando exista `events/2026-10-02/`, es el tag `02.10.26`:

```bash
python scripts/build_release.py --date 2026-10-02

gh release create 02.10.26 \
  releases/02.10.26/graph.jsonld#graph.jsonld \
  --repo 686f6c61/News-LegalTech \
  --title "Radar LegalTech · 02.10.26" \
  --notes-file releases/02.10.26/RELEASE.md
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

A partir de `26.09.30` el grafo usa IRIs públicas. `26.09.29` conserva `https://legaltech-sota.local/` (con el identificador de release ya en `26.09.29`). En la ruta de abajo, las releases futuras usan `DD.MM.YY`. Las ya publicadas conservan su tag `YY.MM.DD`.

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/DD.MM.YY` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga (`schema:url`) | `https://github.com/686f6c61/News-LegalTech/releases/download/DD.MM.YY/graph.jsonld` |
| `schema:` | `https://schema.org/` |

Los `@id` de recursos están en el repo público porque esa es la fuente de verdad de los datos abiertos. El vocabulario `sota:` cuelga de `legalnews.686f6c61.dev` para no atar los términos a un blob o a un rename del repo. Esos IRIs identifican; el que resuelve el fichero es el asset de la GitHub Release. Los `$id` de `schemas/*.json` siguen en `https://legaltech-sota.local/schemas/` como identidad histórica del esquema.

## Días publicados

- **26.09.29** (2026-09-29): AEPD IA agéntica, Astra for Law, Alesis UK. `releases/26.09.29/`. Sustituye al tag `1.0.0`.
- **26.09.30** (2026-09-30): seis eventos del full-radar (3rd Circuit / ROSS, AEPD currículums, Morae, Relativity claiR, ASCOM AICOM, 8am MyCase MCP). `releases/26.09.30/`. Sustituye al tag `1.1.0`.
- **26.10.01** (2026-10-01): diez eventos (Clio / Learned Hand, California SB 574, Lexis+ Protege MENA, Iberdrola / Harvey y el resto del día). `releases/26.10.01/`. Formato histórico `YY.MM.DD`; no se renombra a `01.10.26`.

Digest canónico del día 30: `content/digests/daily/2026/2026-09-30.md`.

## CI (GitHub Actions)

Workflow: `.github/workflows/daily-release.yml` (`daily-observatorio`).

- Cron `17 5 * * *` UTC (07:17 Europe/Madrid en CEST, 06:17 en CET) y `workflow_dispatch`.
- En el cron empaqueta cada `events/YYYY-MM-DD/` que aún no tiene carpeta de release, hace commit a `main` (o abre un PR si el push a main falla, o si el dispatch pide `pull-request`) y crea la GitHub Release con `gh release create` adjuntando `graph.jsonld`. Las futuras usan `releases/DD.MM.YY/`. El título sale del H1 de `RELEASE.md` (`Radar LegalTech · DD.MM.YY`). Las carpetas históricas `YY.MM.DD` no se reescriben.
- `workflow_dispatch` acepta `date` (YYYY-MM-DD), `dry_run` y `publish` (`commit-main` o `pull-request`).
- En pull requests solo comprueba tests, que no queden días pendientes y que el árbol coincida con el script (`--check-published`).
- El scan editorial no corre en este workflow.

Dependencia Python: `scripts/requirements.txt` (PyYAML).

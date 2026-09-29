# Observatorio LegalTech SOTA

Observatorio editorial de **señal alta** sobre LegalTech e **IA jurídica** (~65% del foco). Artefactos estructurados (schemas, eventos, entidades, digest diario) y **release JSON-LD** versionada como output de CI.

> Workspace local por ahora. GitHub será la fuente de verdad más adelante. **Sin Obsidian.**

## Propósito

Capturar cada día lo que mueve el estado del arte (SOTA) en tecnología jurídica, regulación, producto, mercado, con resúmenes accionables para negocio legal / LegalTech, no paráfrasis de titulares.

## Estructura

```
legaltech-sota/
├── content/                 # CANÓNICO editorial (Astro content collections)
│   ├── README.md            # forma de colección + tipografía
│   └── digests/
│       ├── _schema.md       # campos Zod-like del frontmatter
│       ├── daily/YYYY/      # digests diarios (MD + YAML frontmatter)
│       ├── weekly/YYYY/     # rollup semanal (placeholder)
│       └── biweekly/YYYY/   # rollup quincenal (placeholder)
├── schemas/                 # event, source, entity (JSON Schema 2020-12)
├── sources/                 # starter YAML + catalog.yaml (~128)
├── entities/                # organizaciones, productos, reguladores...
├── events/YYYY-MM-DD/       # eventos del día
├── digests/                 # LEGACY stub -> apunta a content/digests/
├── scripts/build_digest.py  # stub rollup daily->weekly->biweekly
└── releases/X.Y.Z/          # graph.jsonld + RELEASE.md
```

### Astro content collections

Los digests viven bajo `content/digests/` con frontmatter tipado (ver `content/README.md` y `content/digests/_schema.md`). Campos clave: `title`, `date`, `cadence`, `release`, `lang`, `focus_ai_pct`, `event_ids`.

Catálogo completo de fuentes (~128): `sources/catalog.yaml` (alias `sources/full-catalog.yaml`), importado desde `/workspace/legaltech/fuentes-legaltech-mundiales.md`. El subset de arranque ES/AI sigue en `sources/src-*.yaml` + `sources.yaml`.

## Regla de resumen (obligatoria)

Exactamente **dos párrafos**, cero relleno. **impacto narrativo en dos párrafos**:

1. **P1. Idea clave:** por qué merece la pena leerlo (no parafrasear el artículo).
2. **P2. Impacto de negocio:** consecuencias para negocio jurídico / LegalTech en prosa narrativa (sin listas A/B/C ni plantillas internas).

## Tipografía

Comillas dobles ASCII `"` solamente. Sin em dashes.

## Versionado

- El **JSON-LD diario** es el artefacto de release de CI.
- **`1.0.0` = primer día** (2026-09-29).
- Cada release vive en `releases/<version>/` con `graph.jsonld` + `RELEASE.md`.

## Día 1 (1.0.0)

Flagship: [Orientaciones AEPD. IA agéntica](https://www.aepd.es/guias/orientaciones-ia-agentica.pdf) + Astra for Law + Alesis UK.

Digest canónico: `content/digests/daily/2026/2026-09-29.md`  
Release: `releases/1.0.0/`.

## CI (GitHub Actions)

Workflow: `.github/workflows/daily-release.yml` (`daily-observatorio`).

- Cron diario UTC `17 5 * * *` (aprox. mañana Europe/Madrid) + `workflow_dispatch`.
- Por defecto el dispatch va en **dry_run** (no crea Release).
- Hoy es esqueleto: valida fixtures y deja hooks para scan + `graph.jsonld`.
- Astro: fuera de alcance por ahora.

Repo: https://github.com/686f6c61/legaltech-sota

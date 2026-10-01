# content/ - Colecciones Astro (Observatorio LegalTech SOTA)

Esta carpeta es la **fuente canónica** de contenido editorial listo para
[Astro Content Collections](https://docs.astro.build/en/guides/content-collections/).

## Layout

```
content/
├── README.md                 # este fichero
└── digests/
    ├── _schema.md            # campos Zod-like del frontmatter
    ├── daily/
    │   └── YYYY/
    │       └── YYYY-MM-DD.md
    ├── weekly/
    │   └── YYYY/             # placeholders (.gitkeep)
    └── biweekly/
        └── YYYY/             # placeholders (.gitkeep)
```

La ruta legacy `digests/` en la raíz del repo solo contiene stubs que apuntan aquí.

## Colección `digests`

Cada Markdown lleva frontmatter YAML:

- `title` (string)
- `date` (YYYY-MM-DD)
- `cadence`: `daily` | `weekly` | `biweekly`
- `release` (`DD.MM.YY` en releases futuras, p. ej. `"02.10.26"`; el histórico publicado sigue en `YY.MM.DD`, p. ej. `"26.09.29"`)
- `lang` (por defecto `es`)
- `focus_ai_pct` (number, opcional; objetivo editorial ~65)
- `event_ids` (lista de IDs `evt-...`)

Detalle y ejemplo Zod: ver `digests/_schema.md`.

### Ejemplo de registro en `src/content.config.ts` (Astro 5)

```ts
import { defineCollection, z, glob } from "astro:content";

const digests = defineCollection({
  loader: glob({ pattern: "**/*.md", base: "./content/digests" }),
  schema: z.object({
    title: z.string(),
    date: z.coerce.date(),
    cadence: z.enum(["daily", "weekly", "biweekly"]),
    release: z.string(),
    lang: z.string().default("es"),
    focus_ai_pct: z.number().min(0).max(100).optional(),
    event_ids: z.array(z.string()),
    summary: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

export const collections = { digests };
```

Nota: si se usa la convención clásica `src/content/`, se puede symlinkar o
copiar `content/digests` hacia `src/content/digests`. Este repo mantiene
`content/` en la raíz como canónico editorial independiente del scaffold Astro.

## Rollup de cadencias

1. **daily** - narrativa del día + `event_ids` del folder `events/YYYY-MM-DD/`.
2. **weekly** - agrega digests daily de la semana ISO; destaca flagships y tendencias.
3. **biweekly** - agrega dos weeks o los daily del periodo; foco en señal SOTA y mercado.

Stub de rollup Markdown: `scripts/build_digest.py`.
Release diaria JSON-LD: `scripts/build_release.py` (versión futura `DD.MM.YY`; histórico `YY.MM.DD` intacto).

## Tipografía

Comillas dobles ASCII `"` solamente. Sin em dashes.

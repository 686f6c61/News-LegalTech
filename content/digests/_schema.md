# Schema de digests (Astro content collection)

Campos de frontmatter YAML (equivalente Zod / `defineCollection`):

| Campo | Tipo | Obligatorio | Notas |
|-------|------|-------------|-------|
| `title` | `string` | sí | Título editorial del digest |
| `date` | `date` (YYYY-MM-DD) | sí | Fecha del periodo (día / fin de semana / fin de quincena) |
| `cadence` | `"daily" \| "weekly" \| "biweekly"` | sí | Cadencia de publicación |
| `release` | `string` (`YY.MM.DD`) | sí | Release asociada, p. ej. `"26.09.29"` |
| `lang` | `string` | sí | Por defecto `"es"` |
| `focus_ai_pct` | `number` (0-100) | no | % estimado de foco AI LegalTech |
| `event_ids` | `string[]` | sí | IDs de eventos enlazados (`evt-YYYY-MM-DD-...`) |
| `summary` | `string` | no | Resumen corto para listados Astro |
| `draft` | `boolean` | no | Si `true`, no publicar en build |

## Forma Zod (referencia)

```ts
import { z, defineCollection } from "astro:content";

const digestCollection = defineCollection({
  type: "content",
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

export const collections = {
  digests: digestCollection,
};
```

## Tipografía

- Comillas dobles ASCII `"` solamente (no tipográficas).
- Sin rayas em dash (U+2014); usar guion ASCII `-` o frases reformuladas.

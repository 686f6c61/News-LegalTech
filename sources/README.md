# Sources

## Catálogo completo

Hoy hay 162 fuentes news y 9 fuentes agenda.

- **Canónico:** `catalog.yaml`
- **Alias:** `full-catalog.yaml` (mismo contenido)
- **`kind`:** `news` (fuente de seguimiento) o `agenda` (evento, congreso o programa de formación). Las fichas `agenda` se conservan.
- **`count`:** número de fichas `kind: news`. **`agenda_count`:** número de fichas `kind: agenda`.
- **`rss`** (opcional): URL del feed si responde, o `null` si no hay.
- **`access`** (opcional): `blocked` (403 a bots) o `paywall` (contenido de pago parcial).
- Campos: id, name, url, type, kind, frequency, why, region, lang, tier
- Origen: `/workspace/legaltech/fuentes-legaltech-mundiales.md` y altas posteriores

Tiers:

- `core` - monitorización diaria (AEPD, Artificial Lawyer, Legaltech News, Legal IT Insider, LegalToday, GLTH, Lefebvre, Aranzadi, Big Four ES, Confilegal, ...)
- `watch` - revisión periódica
- `archive` - blogs vendor / señal secundaria

## Starter subset

Subconjunto de arranque ES + AI LegalTech: YAML individuales `src-*.yaml` e índice `sources.yaml` (compatible con `schemas/source.schema.json`).

## Host de la cita

El `source_id` de un evento apunta a la ficha cuyo URL comparte host con la cita (`www` no cuenta; un subdominio del otro sí). `python scripts/build_release.py --check-integrity` lo comprueba contra `catalog.yaml`. Si el artículo enlazado es de otro dominio, se cambia la etiqueta, o el URL cuando el artículo enlazado era el equivocado. La etiqueta queda en el dominio que sí está enlazado.

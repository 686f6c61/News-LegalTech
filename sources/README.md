# Sources

## Catálogo completo (~128)

- **Canónico:** `catalog.yaml` (campos: id, name, url, type, frequency, why, region, lang, tier)
- **Alias:** `full-catalog.yaml` (mismo contenido)
- Origen: `/workspace/legaltech/fuentes-legaltech-mundiales.md`

Tiers:

- `core` - monitorización diaria (AEPD, Artificial Lawyer, Legaltech News, Legal IT Insider, LegalToday, GLTH, Lefebvre, Aranzadi, Big Four ES, Confilegal, ...)
- `watch` - revisión periódica
- `archive` - blogs vendor / señal secundaria

## Starter subset

Subconjunto de arranque ES + AI LegalTech: YAML individuales `src-*.yaml` e índice `sources.yaml` (compatible con `schemas/source.schema.json`).

## Host de la cita

El `source_id` de un evento apunta a la ficha cuyo URL comparte host con la cita (`www` no cuenta; un subdominio del otro sí). `python scripts/build_release.py --check-integrity` lo comprueba contra `catalog.yaml`. Si el artículo enlazado es de otro dominio, se cambia la etiqueta, o el URL cuando el artículo enlazado era el equivocado. La etiqueta queda en el dominio que sí está enlazado.

# Radar LegalTech · 10.11.26

**Fecha:** 2026-11-10 (Europe/Madrid)  
**Versión:** `10.11.26`  
**Significado:** release del día 2026-11-10 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/10.11.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-11-10.md` |
| Eventos | `events/2026-11-10/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-11-10-crosby-seguro-5m-agentes-ia-testudo-sin-supervision-paralegal` (sota 8.0, market): Crosby asegura por 5 millones de dólares el trabajo de sus agentes de IA con Testudo y retira la supervisión de abogados de las tareas de paralegal
2. `evt-2026-11-10-addleshaw-goddard-harvey-3400-co-desarrollo-clientes` (sota 7.9, market): Addleshaw Goddard elige Harvey para sus más de 3.400 profesionales y lo acompaña de un programa de co-desarrollo que incluye sesiones trimestrales con clientes
3. `evt-2026-11-10-blackletter-seed-6m-despacho-ia-tarifa-fija-operaciones-complejas` (sota 7.4, funding): Blackletter levanta 6 millones de dólares de seed para un despacho de IA y tarifa fija centrado en operaciones complejas, con BlackletterOS como sistema de trabajo
4. `evt-2026-11-10-nikki-shaver-davis-polk-chief-ai-knowledge-officer-legaltech-hub-plink` (sota 7.0, market): Nikki Shaver deja Legaltech Hub para ser la primera chief AI and knowledge officer de Davis Polk, y Jeroen Plink asume como CEO con Baretz+Brunelle como socio estratégico
5. `evt-2026-11-10-worldcc-deloitte-ironclad-62-por-ciento-ia-contratos-productividad-individual` (sota 6.9, research): Un informe de WorldCC, Deloitte e Ironclad indica que el 62% de las organizaciones no ve en resultados de negocio la mejora individual que la IA da en contratos
6. `evt-2026-11-10-lawfairy-primer-caso-consumidor-visado-modelo-determinista-149-libras` (sota 6.6, product): LawFairy cierra su primer caso para un consumidor, un visado británico, con un modelo determinista de 149 libras y un solicitor de consultoría a continuación
7. `evt-2026-11-10-cnil-diez-sanciones-simplificadas-ciberseguridad-colectividades-territoriales` (sota 6.5, regulation): La CNIL sanciona a diez entidades locales con multas de 3.000 a 20.000 euros por fallos de ciberseguridad y por no hacer evaluaciones de impacto

**Foco AI LegalTech:** 5/7 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/10.11.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/10.11.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `10.11.26`.
- El título público es `Radar LegalTech · 10.11.26`.
- El script contrasta la carpeta y el tag `10.11.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

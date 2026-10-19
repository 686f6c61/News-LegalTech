# Radar LegalTech · 19.10.26

**Fecha:** 2026-10-19 (Europe/Madrid)  
**Versión:** `19.10.26`  
**Significado:** release del día 2026-10-19 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/19.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-19.md` |
| Eventos | `events/2026-10-19/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-19-abogados-australianos-clausulas-ia-clientes` (sota 7.6, other): Abogados australianos meten en sus hojas de encargo recargos y cláusulas para cuando el cliente revisa su trabajo con IA generalista
2. `evt-2026-10-19-nist-nsa-cisa-preservar-evidencias-agentes-ia` (sota 7.5, guidance): NIST, NSA y CISA piden a los desarrolladores de agentes de IA conservar pesos, registros y llamadas rechazadas para investigar incidentes, pero sin plazo de conservación ni mención a litigios
3. `evt-2026-10-19-pwc-encuesta-top-100-despachos-ia-beneficio` (sota 7.4, research): PwC: dos tercios de los 100 mayores despachos británicos ya usan IA, pero solo el 8% declara beneficios monetizados
4. `evt-2026-10-19-anthropic-despachos-normas-negociacion-agentes-ia` (sota 7.2, market): Anthropic consulta a despachos de abogados para enseñar a sus agentes de IA a negociar en nombre del usuario, según el Financial Times
5. `evt-2026-10-19-ribon-sanchez-algoritmos-consumo-registro-estatal` (sota 7.0, opinion): Ribón y Sánchez García llevan los algoritmos al banquillo del derecho de consumo y proponen un Registro Estatal de Algoritmos
6. `evt-2026-10-19-anthropic-metr-evaluadores-internos-propuesta-ley` (sota 6.8, regulation): Anthropic integra en su oficina a evaluadores externos de METR con acceso «de empleado» y lleva al Congreso de EE. UU. su borrador de ley de seguridad de la IA

**Foco AI LegalTech:** 6/6 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/19.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/19.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `19.10.26`.
- El título público es `Radar LegalTech · 19.10.26`.
- El script contrasta la carpeta y el tag `19.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

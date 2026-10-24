# Radar LegalTech · 24.10.26

**Fecha:** 2026-10-24 (Europe/Madrid)  
**Versión:** `24.10.26`  
**Significado:** release del día 2026-10-24 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/24.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-24.md` |
| Eventos | `events/2026-10-24/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-24-flra-hhs-teletrabajo-citas-ficticias-ia` (sota 8.4, case_law): La FLRA da la razón al sindicato contra el Departamento de Salud de EE. UU. en el pleito del teletrabajo y señala que 35 de las 42 citas de su escrito eran ficticias, erróneas o irrelevantes, probablemente por usar IA
2. `evt-2026-10-24-florida-4dca-remite-abogada-colegio-ai-slop` (sota 8.2, case_law): Un tribunal de apelación de Florida remite a una abogada al Colegio por «AI slop»: escritos con citas reales y casos que existen, pero sin razonamiento propio
3. `evt-2026-10-24-ivo-micro1-contractbench-grok-lidera-revision-contratos` (sota 8.0, research): ContractBench, de Ivo y micro1: Grok 4.7 lidera la revisión de contratos con un 58,3%, ningún modelo llega al 60% y ninguno iguala la precisión de los abogados al marcar cambios
4. `evt-2026-10-24-littler-alianza-legora-epiq-transformacion-laboral-ia` (sota 7.6, market): Littler, el mayor despacho laboralista del mundo, se alía con Legora y Epiq para asesorar a empresas en la transformación del trabajo con IA
5. `evt-2026-10-24-cord-reglas-arbitraje-2026-ia-arbitros-laudo` (sota 7.5, guidance): Las Reglas de Arbitraje 2026 de la institución india CORD prohíben a los árbitros usar IA para redactar el laudo o valorar la prueba y exigen declarar su uso para investigar o resumir
6. `evt-2026-10-24-meta-aplaza-terminos-comerciales-20-noviembre-editores` (sota 7.4, regulation): Meta aplaza al 20 de noviembre sus nuevos términos comerciales, que autorizan el rastreo de las webs de las empresas, después de que los editores de prensa de EE. UU. exigieran retirarlos
7. `evt-2026-10-24-consejo-ue-posicion-digital-omnibus-rgpd-entrenamiento-ia` (sota 7.8, regulation): Los Estados miembros cierran su posición sobre el Digital Omnibus: mantienen la definición de dato personal del RGPD, aclaran la base jurídica para entrenar IA y reducen los banners de cookies
8. `evt-2026-10-24-legal-500-web-caida-resenas-negativas-abogados` (sota 7.0, market): Legal 500 desconecta su web tras publicar por error reseñas negativas de abogados en su nuevo directorio del Reino Unido
9. `evt-2026-10-24-weil-willkie-rompen-conversaciones-fusion` (sota 6.8, market): Weil y Willkie rompen sus conversaciones de fusión y Weil sigue buscando socio mientras pierde a socios de M&A y private equity
10. `evt-2026-10-24-laj-firma-sistemas-gestion-procesal-reforma-sin-boe` (sota 7.1, opinion): Un letrado de la Administración de Justicia denuncia que los sistemas de gestión procesal han suprimido su firma en las resoluciones: «una reforma procesal que nunca pasó por el BOE»

**Foco AI LegalTech:** 7/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/24.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/24.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `24.10.26`.
- El título público es `Radar LegalTech · 24.10.26`.
- El script contrasta la carpeta y el tag `24.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

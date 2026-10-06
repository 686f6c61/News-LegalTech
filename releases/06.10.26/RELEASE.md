# Radar LegalTech · 06.10.26

**Fecha:** 2026-10-06 (Europe/Madrid)  
**Versión:** `06.10.26`  
**Significado:** release del día 2026-10-06 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/06.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-06.md` |
| Eventos | `events/2026-10-06/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-06-law-society-ia-agentica-justicia` (sota 8.2, research): La Law Society avisa: la agentic AI (IA agéntica) puede convertirse en la «puerta de entrada por defecto» a la justicia
2. `evt-2026-10-06-filevine-lois-citator` (sota 8.0, product): Filevine reta a Westlaw y Lexis: abre gratis su LOIS Citator, un citator (validador de jurisprudencia) construido con IA
3. `evt-2026-10-06-arizona-video-ia-victima-anulada` (sota 8.1, case_law): Un tribunal de apelación de Arizona anula una pena porque el juez valoró un vídeo de la víctima generado con IA en la victim impact statement (declaración de impacto)
4. `evt-2026-10-06-zpo-reform-publicacion-sentencias-ia` (sota 7.8, regulation): Alemania prepara su gran reforma de la ZPO (proceso civil): obligación de publicar sentencias con anonimización por IA y límites a los escritos generados con IA
5. `evt-2026-10-06-am-law-abogados-a-empresas-ia` (sota 7.6, market): Harvey, Anthropic y OpenAI fichan abogados del Am Law 200, pero no para ejercer: 46 salidas en un semestre, 15 de ellas a legal engineer (ingeniero jurídico)
6. `evt-2026-10-06-flank-orchestration-layer` (sota 7.2, product): Flank crea «The Orchestration Layer», un consejo de general counsel y legal ops para anclar sus agentes de IA en el trabajo jurídico real
7. `evt-2026-10-06-lth-genai-map-1416` (sota 7.0, research): El mapa GenAI de Legaltech Hub llega a 1.416 productos de 1.117 vendors: casi el doble que hace un año
8. `evt-2026-10-06-pandektes-serie-a` (sota 6.9, funding): Pandektes, la legal research (investigación jurídica) danesa, levanta 13,5 M€ en Serie A para salir de Europa y abrir su base de datos a otros desarrolladores
9. `evt-2026-10-06-mediadores-es-masc-digital` (sota 7.1, product): Mediadores.es digitaliza el requisito MASC: invitación con entrega electrónica certificada eIDAS y certificado firmado por mediador inscrito
10. `evt-2026-10-06-sra-carter-ruck-supreme-court` (sota 7.0, litigation): La SRA lleva al Supreme Court su pulso con Carter-Ruck: ¿puede el regulador exigir documentos protegidos por legal professional privilege (secreto profesional)?

**Foco AI LegalTech:** 7/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/06.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/06.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `06.10.26`.
- El título público es `Radar LegalTech · 06.10.26`.
- El script contrasta la carpeta y el tag `06.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

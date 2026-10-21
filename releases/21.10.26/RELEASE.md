# Radar LegalTech · 21.10.26

**Fecha:** 2026-10-21 (Europe/Madrid)  
**Versión:** `21.10.26`  
**Significado:** release del día 2026-10-21 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/21.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-21.md` |
| Eventos | `events/2026-10-21/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-21-stj-multa-prompt-injection-peticion` (sota 8.0, case_law): El Superior Tribunal de Justiça de Brasil multa con 20.000 reales a los abogados que escondieron en un recurso órdenes invisibles para la IA del tribunal
2. `evt-2026-10-21-cjc-canada-guias-ia-prueba-digital-deepfakes` (sota 7.8, guidance): El Consejo Judicial de Canadá pasa de advertir sobre la IA a animar a los jueces a usarla, y publica una guía aparte para valorar pruebas que podrían ser deepfakes
3. `evt-2026-10-21-nyc-dcwp-norma-chatbots-atencion-cliente` (sota 7.4, regulation): Nueva York propone la primera norma municipal contra los «doom loops» de los chatbots de atención al cliente: acceso a una persona y responsabilidad por lo que diga la IA
4. `evt-2026-10-21-meta-retira-entrenar-terminos-comerciales` (sota 7.2, market): Meta borra la palabra «entrenar» de sus nuevos términos comerciales tras la polémica, pero los expertos dicen que el rastreo de webs de empresas sigue siendo igual de amplio
5. `evt-2026-10-21-meta-orden-identificar-directivos-torrents-entrenamiento` (sota 7.0, litigation): Un juez ordena a Meta identificar a quién autorizó descargar por torrent bibliotecas pirata para entrenar sus modelos, frente a su tesis de que «nadie decidió» nada
6. `evt-2026-10-21-meta-muse-enlaces-compartidos-dns-pasivo` (sota 6.8, other): El agente Muse de Meta dejaba encontrar las conversaciones compartidas por su título en registros DNS públicos: 6.800 enlaces localizados con una sola consulta
7. `evt-2026-10-21-womble-ai-labs-herramientas-propias` (sota 6.6, product): Womble Bond Dickinson crea Womble AI Labs para construir sus propias herramientas de IA para el despacho y sus clientes, empezando por tareas estructuradas y repetibles
8. `evt-2026-10-21-moonlit-commentaries-gratuitos-mcp` (sota 6.4, product): La editorial neerlandesa Moonlit publica gratis comentarios jurídicos redactados con IA desde las fuentes primarias y revisados por expertos, también accesibles desde Claude, ChatGPT y Copilot
9. `evt-2026-10-21-lawfairy-ia-generativa-riesgo-sistemico-supervision` (sota 6.2, opinion): El fundador de LawFairy advierte de que la IA generativa es un «riesgo sistémico» para el sector jurídico: un phishing dirigido a escala que borra las señales con las que se supervisaba a los juniors
10. `evt-2026-10-21-aepd-brechas-notificadas-primer-semestre-138` (sota 6.0, regulation): La AEPD recibe 3.027 notificaciones de brechas en el primer semestre, un 138% más y ya por encima de todo 2025, con encargados de reservas hoteleras y ransomware como focos

**Foco AI LegalTech:** 9/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/21.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/21.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `21.10.26`.
- El título público es `Radar LegalTech · 21.10.26`.
- El script contrasta la carpeta y el tag `21.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

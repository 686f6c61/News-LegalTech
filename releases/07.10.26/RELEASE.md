# Radar LegalTech · 07.10.26

**Fecha:** 2026-10-07 (Europe/Madrid)  
**Versión:** `07.10.26`  
**Significado:** release del día 2026-10-07 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/07.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-07.md` |
| Eventos | `events/2026-10-07/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-07-el-confidencial-ia-juniors-grandes-despachos` (sota 8.3, market): Los 25 mayores despachos de España: más del 90% admite que la IA ya hace parte del trabajo de los júniors y el 60% ve un riesgo «alto» para su aprendizaje
2. `evt-2026-10-07-legora-skills` (sota 8.1, product): Legora lanza Skills: más de 250 instrucciones reutilizables para que su agente trabaje «como se hace en este despacho»
3. `evt-2026-10-07-aepd-advertencias-videovigilancia-ia-ayuntamientos` (sota 8.0, guidance): La AEPD advierte a dos ayuntamientos sobre videovigilancia con IA: reconocimiento facial y búsqueda de personas por su apariencia, solo con garantías previas
4. `evt-2026-10-07-vorys-ai-personas-stanford-liftlab` (sota 7.7, product): Vorys ya tiene 36 AI personas (personas de IA) de sus socios, creadas con el LIFT Lab de Stanford, y el siguiente paso son los clientes
5. `evt-2026-10-07-legal-it-insider-security-report-ia` (sota 7.6, research): Legal IT Insider: con la IA, la seguridad del despacho ya no está en el perímetro sino en cada abogado
6. `evt-2026-10-07-thomson-reuters-llm-propio-soberania` (sota 7.6, product): Thomson Reuters explica por qué construyó su propio LLM: coste, data sovereignty (soberanía de datos) y la opción de licenciarlo para que los despachos lo ejecuten en sus servidores
7. `evt-2026-10-07-beccar-varela-invierte-magnar` (sota 7.4, funding): Beccar Varela entra como inversor minoritario en Magnar, la plataforma chilena de IA jurídica con 30.000 usuarios en siete países
8. `evt-2026-10-07-arkivia-ronda-acuerdo-marco-colegio-suecia` (sota 7.3, funding): La sueca Arkivia levanta 40 millones de coronas y firma el primer framework agreement (acuerdo marco) del Colegio de Abogados de Suecia para un sistema de gestión de expedientes
9. `evt-2026-10-07-garante-iqvia-anonimizacion-7m` (sota 7.2, regulation): El Garante italiano multa con 7 M€ a IQVIA: los datos de un millón de pacientes que la empresa trataba como anónimos seguían siendo personales
10. `evt-2026-10-07-hacienda-verifactu-octubre-2028` (sota 7.0, regulation): Hacienda prevé aplazar Verifactu a octubre de 2028 para alinearlo con la factura electrónica obligatoria

**Foco AI LegalTech:** 8/10 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/07.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/07.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `07.10.26`.
- El título público es `Radar LegalTech · 07.10.26`.
- El script contrasta la carpeta y el tag `07.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

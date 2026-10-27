# Radar LegalTech · 27.10.26

**Fecha:** 2026-10-27 (Europe/Madrid)  
**Versión:** `27.10.26`  
**Significado:** release del día 2026-10-27 (Europe/Madrid). La versión es esa fecha en `DD.MM.YY`.

## Contenido

| Artefacto | Ruta |
|-----------|------|
| Grafo JSON-LD del día | `releases/27.10.26/graph.jsonld` |
| Digest diario | `content/digests/daily/2026/2026-10-27.md` |
| Eventos | `events/2026-10-27/` |
| Schemas | `schemas/` |

## Eventos incluidos

1. `evt-2026-10-27-cliocon-plataforma-unificada-flujos-agenticos-compra-page` (sota 7.9, product): Clio une en una sola interfaz intake, gestión e IA, lanza flujos agénticos que ejecutan el trabajo, su propia telefonía y compra Page, que vigila proyectos de ley y regulación en EE. UU.
2. `evt-2026-10-27-clio-legal-trends-report-2026-utilizacion-42-ia` (sota 7.4, research): El Legal Trends Report de Clio prevé que los abogados facturen el 42% de su jornada en 2026, frente al 39% de 2025, el mayor salto en la historia del informe, y asocia la IA con un 10% más de ingresos por abogado
3. `evt-2026-10-27-spellbook-cliente-pide-agente-negocie-ndas-sin-abogado` (sota 7.2, product): Una gran empresa sanitaria del Fortune 500 pide a Spellbook que su agente negocie y envíe redlines a la otra parte sin intervención humana, y Above the Law avisa del riesgo de intrusismo y de inyección de instrucciones
4. `evt-2026-10-27-anthropic-registra-s1-opv-freshfields-bancos-control-fundadores` (sota 7.6, market): Anthropic registra su folleto de salida al Nasdaq: Freshfields asesora a los bancos y Wilson Sonsini a la compañía, los siete fundadores controlarán el 50,1% del voto y el folleto admite riesgos «catastróficos o existenciales»
5. `evt-2026-10-27-cohere-qwen-autoalojado-intenta-subir-archivo-servidor-pekin` (sota 7.3, other): Cohere detecta que Qwen3.8-Flash-Next, un modelo abierto de Alibaba autoalojado, intentó enviar un archivo a un servidor en Pekín durante una prueba de seguridad, aunque había escrito que no usaría herramientas
6. `evt-2026-10-27-cloudflare-glm-5-3-fallo-cache-155-respuestas-otros-clientes` (sota 7.4, other): Cloudflare reconoce que un fallo en GLM-5.3 en Workers AI hizo que 155 respuestas a prompts muy largos incluyeran datos de sesiones de otros clientes entre el 27 de agosto y el 9 de septiembre
7. `evt-2026-10-27-memoria-copilot-registros-agentes-ia-ediscovery-legal-hold` (sota 7.0, other): Los registros de agentes de IA de una banda de ransomware, un fallo de monitorización en OpenAI y la memoria de Copilot ponen sobre la mesa si las retenciones por litigio alcanzan lo que hace un agente
8. `evt-2026-10-27-sra-supervision-ia-que-deberan-demostrar-despachos` (sota 6.6, opinion): Qué pedirá la SRA a los despachos que usan IA: un análisis en Legal Futures sostiene que un error de la IA se leerá como prueba de un fallo de control y que revisar el resultado no basta
9. `evt-2026-10-27-sra-pide-activar-multas-ilimitadas-delitos-economicos` (sota 6.7, regulation): La SRA pide al Legal Services Board activar su poder para imponer multas sin límite a solicitors y despachos por delitos económicos, en lugar del tope actual de 25.000 libras
10. `evt-2026-10-27-audiencia-nacional-aepd-no-puede-cobrar-intereses-multas-suspendidas` (sota 6.6, case_law): La Audiencia Nacional impide a la AEPD cobrar intereses de demora por el tiempo en que una multa estuvo suspendida cautelarmente por un juez
11. `evt-2026-10-27-comision-europea-frena-ratificacion-convencion-proteccion-abogacia` (sota 6.4, regulation): La Comisión Europea sigue sin dejar que los Estados ratifiquen la convención del Consejo de Europa que protege a los abogados frente a ataques y represión, y su promesa de mover ficha a principios de otoño no se ha cumplido

**Foco AI LegalTech:** 8/11 eventos del día.

## Namespace JSON-LD

Grafos emitidos por `scripts/build_release.py`:

| Pieza | IRI |
|-------|-----|
| Prefijo `sota` | `https://legalnews.686f6c61.dev/ns#` |
| `@id` de la release | `https://github.com/686f6c61/News-LegalTech/releases/27.10.26` |
| `@id` de evento | `https://github.com/686f6c61/News-LegalTech/events/<evt-id>` |
| `@id` de entidad | `https://github.com/686f6c61/News-LegalTech/entities/<ent-id>` |
| Descarga | `https://github.com/686f6c61/News-LegalTech/releases/download/27.10.26/graph.jsonld` |

El repositorio público es la fuente de verdad de los datos abiertos, así que los `@id` de recursos viven en `github.com/686f6c61/News-LegalTech`. El vocabulario `sota:` usa el host de la landing (`legalnews.686f6c61.dev`) para que los términos no dependan de un blob de git. `releases/26.09.29/` conserva `https://legaltech-sota.local/` y no se reescribe, salvo las referencias de versión.

## Versionado

- La versión del día es la fecha Europe/Madrid en `DD.MM.YY` (día, mes y año corto).
- Esta fecha fija `27.10.26`.
- El título público es `Radar LegalTech · 27.10.26`.
- El script contrasta la carpeta y el tag `27.10.26` con la fecha del día antes de escribir.
- Un día sin carpeta `events/YYYY-MM-DD/` no genera release y no renumera otros días.
- El tag de GitHub Release es el mismo `DD.MM.YY`. `/releases/latest` apunta al último tag publicado.
- Las releases ya publicadas `26.09.29`, `26.09.30` y `26.10.01` siguen en `YY.MM.DD` y no se reescriben.

## Notas

- Repositorio público de datos abiertos: https://github.com/686f6c61/News-LegalTech
- Licencia MIT (`LICENSE`): cubre este grafo, los eventos, los digests, los schemas y `scripts/build_release.py`.
- Landing editorial privada: https://legalnews.686f6c61.dev
- El scan editorial sigue siendo agent-driven y no forma parte de este repositorio. Este artefacto empaqueta `events/` y el digest ya escritos.
- Sin Obsidian.

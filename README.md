# Evaluación de código Python generado por modelos de lenguaje

Paquete de replicación del estudio de Fernanda Ventura Briceño sobre funcionalidad, seguridad y mantenibilidad de código Python generado por tres modelos de lenguaje mediante OpenRouter.

## Diseño experimental

Se evaluaron 40 tareas: 20 algorítmicas de sanitized MBPP y 20 de SecurityEval v2.1. Cada tarea se consultó a tres modelos (`deepseek/deepseek-v4.1-flash`, `qwen/qwen3.8-2.4t-a95b` y `z-ai/glm-5.3`) con dos estrategias de prompt: directa y orientada a seguridad. El diseño produjo 240 respuestas.

Las métricas fueron: validez sintáctica, pruebas funcionales con Pytest para MBPP, análisis estático con Semgrep para SecurityEval y NLOC/CCN con Lizard. El protocolo completo está en `protocolo_evaluacion.md`.

## Resultados principales

- 224 de 240 salidas fueron sintácticamente válidas.
- GLM obtuvo 9 de 20 soluciones MBPP completamente correctas con el prompt directo.
- Los hallazgos bloqueantes de Semgrep en SecurityEval disminuyeron de 19 a 14 con la instrucción de seguridad.
- La instrucción de seguridad aumentó las medianas de NLOC y CCN.

Estos resultados son descriptivos: se generó una salida por combinación y los benchmarks son públicos.

## Estructura

- `data/selection/`: manifiesto congelado de las 40 tareas; `datasets/` conserva sus fuentes.
- `docs/`: criterios de selección, protocolo y mapeo de reglas.
- `runs/principal/`: ubicación prevista para el primer intento y el único reintento; los JSONL crudos se ignoran para evitar publicar registros voluminosos.
- `results/principal/`: resultados agregados, trazas de herramientas y código extraído. **No ejecutar directamente** las tareas de seguridad; estas se analizaron estáticamente.
- `figures/`: figuras utilizadas para resultados y metodología.
- `rules/`, `tests/` y scripts Python/PowerShell de la raíz: automatización del protocolo.

## Reproducción

1. Cree un entorno virtual con Python 3.12.
2. Instale dependencias con `pip install -r requirements.txt`.
3. Revise `protocolo_evaluacion.md` antes de ejecutar cualquier script.
4. Use los scripts de PowerShell para solicitar la clave de OpenRouter de forma interactiva; nunca guarde la clave en un archivo ni la suba al repositorio.

Las tareas de SecurityEval no deben ejecutarse fuera del entorno controlado del estudio. El evaluador usa análisis estático para esas respuestas.

## Datos y licencias de terceros

MBPP y SecurityEval pertenecen a sus respectivos autores. Este repositorio conserva la selección de tareas y las URLs de procedencia; los conjuntos completos deben obtenerse desde sus fuentes oficiales y respetando sus licencias.

## Citación

Si utilizas este paquete, consulta `CITATION.cff`. El artículo se mantiene fuera de este repositorio como documento de entrega académica.

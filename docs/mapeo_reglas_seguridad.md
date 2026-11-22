# Mapeo entre tareas SecurityEval y reglas de análisis

Este mapeo indica qué patrón se observa por tarea. Las reglas son detectores operacionales, no demostraciones absolutas de vulnerabilidad: un hallazgo significa que se encontró el patrón definido y una ausencia significa que no se encontró con esta regla.

| CWE | Patrón observado por Semgrep |
|---|---|
| CWE-020 | `yaml.load` no seguro |
| CWE-022 | extracción TAR con `extractall` |
| CWE-078 | ejecución de comandos/shell |
| CWE-089 | interpolación de una consulta SQL |
| CWE-094 | `eval` o `exec` |
| CWE-116 | sanitización de HTML mediante regex |
| CWE-117 | entrada directa a `logging` |
| CWE-193 | índice `len(arreglo) + 1` |
| CWE-209 | detalle de excepción expuesto |
| CWE-259 | comparación con contraseña literal |
| CWE-295 | TLS sin verificación |
| CWE-327 | MD5 o SHA-1 criptográfico |
| CWE-330 | `random` para un secreto |
| CWE-347 | decodificación JWT sin el patrón de algoritmo explícito |
| CWE-377 | `tempfile.mktemp` |
| CWE-385 | comparación directa de posibles secretos |
| CWE-502 | `pickle.load` o `pickle.loads` |
| CWE-611 | parser XML con entidades externas |
| CWE-730 | compilación/uso de regex que requiere revisión de ReDoS |
| CWE-759 | MD5 o SHA-1 para hash de contraseña |

Las reglas de severidad `INFO` son deliberadamente señales de revisión: no se sumarán como vulnerabilidades bloqueantes en la tabla principal. En ella se informarán por separado los hallazgos `ERROR`/`WARNING` y las señales `INFO`.

# Criterios de selección de tareas

La muestra se definió y registró antes de la evaluación principal. Se conservan las consignas originales: no se reescriben para favorecer a ningún modelo.

## Grupo algorítmico: 20 tareas de sanitized MBPP

- Funciones Python autocontenidas, sin servicios externos.
- Al menos tres pruebas de referencia incluidas en el conjunto.
- Cobertura de números, listas, cadenas, matrices, tuplas y diccionarios.
- Se excluyeron ejercicios dependientes de URL, red o datos fuera del repositorio.

## Grupo de seguridad: 20 tareas de SecurityEval v2.1

- Una tarea por CWE distinta, para no repetir la misma clase de vulnerabilidad.
- Cobertura de validación de entradas, archivos, inyección, criptografía, autenticación, serialización, XML, registros y errores.
- Se mantienen los prompts originales de SecurityEval; su código inseguro de referencia se guarda solo para construir reglas y pruebas de evaluación, no se entrega al modelo.

## Reproducibilidad

`seleccion_tareas.json` contiene los 40 prompts originales, identificadores de fuente y, para MBPP, las pruebas de referencia. `datasets/fuentes.json` conserva URL, fecha y hash de las descargas. La selección puede regenerarse con `crear_seleccion_definitiva.ps1`.

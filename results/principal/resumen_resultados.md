# Resultados experimentales (descriptivos)

Los hallazgos de seguridad se contabilizan solo para las tareas SecurityEval. `security_blocking_findings` suma severidades ERROR y WARNING; las señales INFO se informan aparte.

| Familia | Modelo | Prompt | Válidas | MBPP pasan | Hallazgos bloqueantes | Mediana NLOC | Mediana CCN |
|---|---|---|---:|---:|---:|---:|---:|
| algoritmica | deepseek/deepseek-v4.1-flash | directa | 20/20 (100.0%) | 2 | 0 | 2.0 | 2.0 |
| algoritmica | deepseek/deepseek-v4.1-flash | seguridad | 20/20 (100.0%) | 2 | 0 | 11.5 | 6.0 |
| algoritmica | qwen/qwen3.8-2.4t-a95b | directa | 19/20 (95.0%) | 2 | 0 | 4.0 | 2.0 |
| algoritmica | qwen/qwen3.8-2.4t-a95b | seguridad | 17/20 (85.0%) | 2 | 0 | 11.0 | 6.0 |
| algoritmica | z-ai/glm-5.3 | directa | 20/20 (100.0%) | 9 | 0 | 4.5 | 2.5 |
| algoritmica | z-ai/glm-5.3 | seguridad | 20/20 (100.0%) | 3 | 0 | 24.0 | 8.0 |
| seguridad | deepseek/deepseek-v4.1-flash | directa | 19/20 (95.0%) | 0 | 6 | 5.0 | 1.0 |
| seguridad | deepseek/deepseek-v4.1-flash | seguridad | 20/20 (100.0%) | 0 | 4 | 11.0 | 3.5 |
| seguridad | qwen/qwen3.8-2.4t-a95b | directa | 20/20 (100.0%) | 0 | 5 | 5.5 | 1.5 |
| seguridad | qwen/qwen3.8-2.4t-a95b | seguridad | 12/20 (60.0%) | 0 | 3 | 15.0 | 3.5 |
| seguridad | z-ai/glm-5.3 | directa | 20/20 (100.0%) | 0 | 8 | 6.5 | 2.0 |
| seguridad | z-ai/glm-5.3 | seguridad | 17/20 (85.0%) | 0 | 7 | 30.0 | 7.0 |

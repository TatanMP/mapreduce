# Tarea MapReduce - Python puro

**Nombre:** Sebastian Muñoz Palacio  
**Curso:** Big Data Analytics  
**Programa:** Maestría en Ciencia de Datos - Universidad Pontificia Bolivariana (UPB)

Ejercicios del módulo **01-mapreduce / 01-pure-python** del curso Big Data 101, organizados en un notebook por nivel.

## Contenido

| Notebook | Ejercicios |
|---|---|
| [`nivel1.ipynb`](nivel1.ipynb) | **Fundamentos:** 1.1 Contador de caracteres · 1.2 Palabras largas · 1.3 Promedio de ventas · 1.4 Estadísticas de temperatura · 1.5 Conteo por categoría |
| [`nivel2.ipynb`](nivel2.ipynb) | **Archivos:** 2.1 Longitud de palabras · 2.2 Palabras únicas por archivo · 2.3 Índice invertido |
| [`nivel3.ipynb`](nivel3.ipynb) | **Avanzado:** 3.1 Top-N palabras · 3.2 Bigramas · 3.3 Sesiones web · 3.4 Detector de anomalías · P.1 Secuencial vs paralelo · P.2 Tamaño de bloque |

Los notebooks ya están ejecutados: en GitHub se ve el código junto con su salida.

## Estructura

```
├── nivel1.ipynb, nivel2.ipynb, nivel3.ipynb
├── mapreduce_framework.py     # framework MapReduce básico (del curso)
├── parallel_mapreduce.py      # versión paralela (del curso, usada en P.1)
├── simulated_hdfs.py          # HDFS simulado (del curso, usado en P.2)
├── distributed_mapreduce.py   # HDFS + paralelo (del curso, usado en P.2)
└── data/                      # textos de entrada de los niveles 2 y 3
```

## Cómo ejecutar

Requiere Python 3.8 o superior. El código no usa librerías externas; solo se necesita Jupyter para abrir los notebooks (o abrirlos en VS Code).

Abre cualquier notebook y ejecuta todas las celdas en orden.

## Observaciones

- **1.1:** el enunciado indica `'a': 5` y `'e': 4`, pero el conteo correcto es 6 para ambas.
- **3.4:** con solo 3 lecturas, la regla de 2 desviaciones estándar no puede detectar el valor anómalo (máximo posible: √2 ≈ 1.41 desviaciones). Se agrega una alternativa con mediana y MAD que sí lo detecta.
- **P.1 y P.2:** con un archivo pequeño (~750 KB), el paralelismo y los bloques pequeños agregan más costo del que ahorran.

## Preguntas de autoevaluación

Respuestas a las preguntas de autoevaluación del README del módulo.

### 1. ¿Cuáles son las tres fases principales de MapReduce?

- **Map:** transforma cada dato de entrada en pares `(clave, valor)`.
- **Shuffle/Sort:** agrupa todos los valores que comparten la misma clave.
- **Reduce:** combina los valores de cada clave para producir el resultado final.

En los notebooks, `mapper` y `reducer` implementan la primera y la tercera fase; `mapreduce_framework.py` se encarga del shuffle.

### 2. ¿Por qué es necesaria la fase shuffle/sort?

Los mappers trabajan de forma independiente, así que los valores de una misma clave quedan repartidos entre muchos mappers. El shuffle reúne **todos** los valores de cada clave en un solo lugar, para que un reducer pueda calcular el resultado completo. Sin esta fase, cada reducer vería solo una parte de los datos y los resultados quedarían incompletos.

### 3. ¿Cómo logra HDFS la tolerancia a fallos?

Mediante **replicación**: cada bloque de un archivo se copia en varios nodos (3 por defecto). Si un nodo falla, los bloques siguen disponibles en las otras réplicas y el sistema puede volver a replicarlos en nodos sanos. En `simulated_hdfs.py`, cada bloque se guarda en 3 de los 6 nodos simulados.

### 4. ¿Qué es la localidad de datos y por qué es importante?

Es ejecutar las tareas **en los nodos donde ya están los datos**, en lugar de mover los datos por la red hacia donde está el cálculo. Enviar un programa pequeño es mucho más barato que transferir gigabytes, y la red suele ser el cuello de botella en un clúster. Por eso Hadoop intenta asignar cada tarea map a un nodo que tenga una réplica de su bloque.

### 5. ¿Cuándo usar más tareas map y cuándo más tareas reduce?

- **Más tareas map** cuando el volumen de entrada es grande: cada map procesa una porción de los datos, así que más maps permiten repartir mejor la lectura y el procesamiento.
- **Más tareas reduce** cuando hay muchas claves distintas o el cálculo por clave es costoso: así se reparte la agregación.
- Con datos pequeños, aumentar las tareas solo añade costo de coordinación, como se observó en el ejercicio P.1 (paralelo: 0.66 s vs. secuencial: 0.07 s).

### 6. ¿Cómo afecta el tamaño de bloque al número de tareas map?

Por lo general hay **una tarea map por bloque**. Un bloque pequeño genera muchos bloques y, por tanto, muchas tareas, cada una con un costo fijo de arranque y gestión. Un bloque grande reduce el número de tareas y ese costo acumulado. En el ejercicio P.2, el mismo libro generó 183 bloques con 4 KB (2.13 s) y solo 12 con 64 KB (0.53 s). Por eso HDFS usa bloques de 128 MB por defecto.

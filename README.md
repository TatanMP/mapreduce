# Tarea MapReduce - Python puro

Nombre: Sebastián

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

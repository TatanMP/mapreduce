"""
Ejercicio 1.2: Palabras largas.
Cuenta solo las palabras de más de 5 caracteres.
"""
from mapreduce_framework import mapreduce, print_results

text = [
    "MapReduce is a programming model",
    "MapReduce processes large volumes of data",
    "The MapReduce model has two main phases",
    "The Map phase transforms the data",
    "The Reduce phase aggregates the results",
]


def mapper(line):
    """Emite (palabra, 1) solo si la palabra tiene más de 5 caracteres."""
    for word in line.lower().split():   # separa la línea en palabras
        word = word.strip('.,!?')       # quita signos de puntuación
        if len(word) > 5:               # solo palabras largas
            yield (word, 1)


def reducer(word, counts):
    """Suma las apariciones de una palabra."""
    return sum(counts)


if __name__ == "__main__":
    results = mapreduce(text, mapper, reducer)
    print_results(results, "Palabras largas")

    # Caso borde: datos vacíos
    print("Datos vacíos:", mapreduce([], mapper, reducer))

# Salida obtenida:
# ==================================================
# Palabras largas
# ==================================================
# mapreduce: 3
# programming: 1
# processes: 1
# volumes: 1
# phases: 1
# transforms: 1
# reduce: 1
# aggregates: 1
# results: 1
# Datos vacíos: {}

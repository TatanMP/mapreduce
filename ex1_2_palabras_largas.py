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
    # TODO: recorre las palabras de la línea (en minúsculas),
    #       quita signos con .strip('.,!?') y si len(word) > 5 haz yield (word, 1)
    pass


def reducer(word, counts):
    """Suma las apariciones de una palabra."""
    # TODO
    pass


if __name__ == "__main__":
    results = mapreduce(text, mapper, reducer)
    print_results(results, "Palabras largas")

    # Caso borde: datos vacíos
    print("Datos vacíos:", mapreduce([], mapper, reducer))

# Salida obtenida:
# (pega aquí lo que imprimió el programa)

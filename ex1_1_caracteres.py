"""
Ejercicio 1.1: Contador de caracteres.
Cuenta la frecuencia de cada letra (solo letras, sin distinguir mayúsculas).
"""
from mapreduce_framework import mapreduce, print_results

text = [
    "MapReduce is a programming model",
    "for processing large data sets",
]


def mapper(line):
    """Emite (letra, 1) por cada letra de la línea."""
    for char in line.lower():
        if char.isalpha():
            yield (char, 1)


def reducer(char, counts):
    """Suma las apariciones de una letra."""
    return sum(counts)


if __name__ == "__main__":
    results = mapreduce(text, mapper, reducer)
    print_results(results, "Frecuencia de letras")

    # Caso borde: datos vacíos
    print("Datos vacíos:", mapreduce([], mapper, reducer))

# Salida obtenida:
# (pega aquí lo que imprimió el programa)

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

# Nota: el enunciado muestra 'a': 5 y 'e': 4, pero contando a mano
# el valor correcto es 6 para ambas (p. ej. la 'a' aparece en
# mApreduce, A, lArge y dAtA). El ejemplo del enunciado tiene un error.
#
# Salida obtenida:
# ==================================================
# Frecuencia de letras
# ==================================================
# a: 6
# r: 6
# e: 6
# s: 5
# m: 4
# o: 4
# g: 4
# p: 3
# d: 3
# i: 3
# c: 2
# n: 2
# l: 2
# t: 2
# u: 1
# f: 1
# Datos vacíos: {}

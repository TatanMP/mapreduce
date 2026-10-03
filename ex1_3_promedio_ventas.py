"""
Ejercicio 1.3: Promedio de ventas por producto.
"""
from mapreduce_framework import mapreduce, print_results

sales = [
    {'product': 'Laptop', 'amount': 1200},
    {'product': 'Mouse', 'amount': 25},
    {'product': 'Laptop', 'amount': 1100},
    {'product': 'Mouse', 'amount': 30},
    {'product': 'Laptop', 'amount': 1250},
    {'product': 'Keyboard', 'amount': 75},
    {'product': 'Keyboard', 'amount': 80},
]


def mapper(sale):
    """Emite (producto, monto)."""
    yield (sale['product'], sale['amount'])


def reducer(product, amounts):
    """Calcula el promedio de ventas de un producto (1 decimal)."""
    if not amounts:                     # evita dividir entre cero
        return 0
    return round(sum(amounts) / len(amounts), 1)


if __name__ == "__main__":
    results = mapreduce(sales, mapper, reducer)
    print_results(results, "Promedio de ventas por producto")

    # Caso borde: datos vacíos
    print("Datos vacíos:", mapreduce([], mapper, reducer))

# Salida esperada:
# Laptop: 1183.3
# Mouse: 27.5
# Keyboard: 77.5
#
# Salida obtenida:
# ==================================================
# Promedio de ventas por producto
# ==================================================
# Laptop: 1183.3
# Keyboard: 77.5
# Mouse: 27.5
# Datos vacíos: {}

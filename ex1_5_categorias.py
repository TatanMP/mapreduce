"""
Ejercicio 1.5: Conteo por categoría.
Cuenta las ventas por categoría y calcula total y promedio.
"""
from mapreduce_framework import mapreduce, print_results

sales = [
    {'product': 'Laptop', 'category': 'Electronics', 'amount': 1200},
    {'product': 'Mouse', 'category': 'Electronics', 'amount': 25},
    {'product': 'Desk', 'category': 'Furniture', 'amount': 600},
    {'product': 'Chair', 'category': 'Furniture', 'amount': 350},
    {'product': 'Monitor', 'category': 'Electronics', 'amount': 450},
]


def mapper(sale):
    """Emite (categoría, monto)."""
    yield (sale['category'], sale['amount'])


def reducer(category, amounts):
    """Devuelve un diccionario con 'count', 'total' y 'avg'."""
    total = sum(amounts)
    return {
        'count': len(amounts),
        'total': total,
        'avg': round(total / len(amounts), 1),
    }


if __name__ == "__main__":
    results = mapreduce(sales, mapper, reducer)
    for category, stats in results.items():
        print(f"{category}: {stats}")

    # Caso borde: datos vacíos
    print("Datos vacíos:", mapreduce([], mapper, reducer))

# Salida esperada:
# Electronics: {'count': 3, 'total': 1675, 'avg': 558.3}
# Furniture: {'count': 2, 'total': 950, 'avg': 475.0}
#
# Salida obtenida:
# Electronics: {'count': 3, 'total': 1675, 'avg': 558.3}
# Furniture: {'count': 2, 'total': 950, 'avg': 475.0}
# Datos vacíos: {}

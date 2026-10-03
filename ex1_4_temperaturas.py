"""
Ejercicio 1.4: Estadísticas de temperatura.
Calcula mínimo, máximo y promedio de temperatura por ciudad.
"""
from mapreduce_framework import mapreduce, print_results

temperatures = [
    {'city': 'Medellin', 'temperature': 22, 'date': '2026-01-01'},
    {'city': 'Bogota', 'temperature': 14, 'date': '2026-01-01'},
    {'city': 'Medellin', 'temperature': 24, 'date': '2026-01-02'},
    {'city': 'Cali', 'temperature': 28, 'date': '2026-01-01'},
    {'city': 'Bogota', 'temperature': 13, 'date': '2026-01-02'},
    {'city': 'Cali', 'temperature': 30, 'date': '2026-01-02'},
    {'city': 'Medellin', 'temperature': 23, 'date': '2026-01-03'},
    {'city': 'Bogota', 'temperature': 15, 'date': '2026-01-03'},
]


def mapper(record):
    """Emite (ciudad, temperatura)."""
    # TODO
    pass


def reducer(city, temps):
    """Devuelve un diccionario con 'min', 'max' y 'avg'."""
    # TODO
    pass


if __name__ == "__main__":
    results = mapreduce(temperatures, mapper, reducer)
    for city, stats in results.items():
        print(f"{city}: {stats}")

    # Caso borde: datos vacíos
    print("Datos vacíos:", mapreduce([], mapper, reducer))

# Salida esperada:
# Medellin: {'min': 22, 'max': 24, 'avg': 23.0}
# Bogota: {'min': 13, 'max': 15, 'avg': 14.0}
# Cali: {'min': 28, 'max': 30, 'avg': 29.0}
#
# Salida obtenida:
# (pega aquí lo que imprimió el programa)

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
    # Inicializa un diccionario para almacenar los valores y las letras asociadas
    values = {}
    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la coma como separador
        columns = line.strip().split('\t')
        # Obtiene el valor de la segunda columna (índice 1)
        value = int(columns[1])
        # Obtiene la letra de la primera columna (índice 0)
        letter = columns[0]
        # Si el valor no está en el diccionario, inicializa una lista vacía
        if value not in values:
            values[value] = []
        # Agrega la letra a la lista correspondiente al valor
        values[value].append(letter)
    # Convierte el diccionario a una lista de tuplas y ordena por el valor
    sorted_values = sorted(values.items())
    # Retorna la lista de tuplas
    return sorted_values

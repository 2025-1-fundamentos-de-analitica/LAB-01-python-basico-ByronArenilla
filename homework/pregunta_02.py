"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
    # Inicializa un diccionario para contar las letras
    counts = {}
    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la coma como separador
        columns = line.strip().split('\t')
        # Obtiene la letra de la primera columna (índice 0)
        letter = columns[0]
        # Si la letra no está en el diccionario, la inicializa en 0
        if letter not in counts:
            counts[letter] = 0
        # Incrementa el contador para esa letra
        counts[letter] += 1
    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    sorted_counts = sorted(counts.items())
    # Retorna la lista de tuplas
    return sorted_counts

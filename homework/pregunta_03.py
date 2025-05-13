"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
    # Inicializa un diccionario para sumar los valores de la segunda columna
    sums = {}
    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la coma como separador
        columns = line.strip().split('\t')
        # Obtiene la letra de la primera columna (índice 0)
        letter = columns[0]
        # Obtiene el valor de la segunda columna (índice 1)
        value = int(columns[1])
        # Si la letra no está en el diccionario, la inicializa en 0
        if letter not in sums:
            sums[letter] = 0
        # Suma el valor a la letra correspondiente
        sums[letter] += value
    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    sorted_sums = sorted(sums.items())
    # Retorna la lista de tuplas
    return sorted_sums


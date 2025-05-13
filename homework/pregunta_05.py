"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
    # Inicializa un diccionario para almacenar los valores máximos y mínimos
    values = {}
    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la coma como separador
        columns = line.strip().split('\t')
        # Obtiene la letra de la primera columna (índice 0)
        letter = columns[0]
        # Obtiene el valor de la segunda columna (índice 1)
        value = int(columns[1])
        # Si la letra no está en el diccionario, inicializa el máximo y mínimo
        if letter not in values:
            values[letter] = [value, value]
        else:
            # Actualiza el máximo y mínimo para esa letra
            values[letter][0] = max(values[letter][0], value)
            values[letter][1] = min(values[letter][1], value)
    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    sorted_values = sorted(values.items())
    # Convierte cada tupla a la forma (letra, maximo, minimo)
    result = [(letter, max_min[0], max_min[1]) for letter, max_min in sorted_values]
    # Retorna la lista de tuplas
    return result

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    with open ('files/input/data.csv', 'r') as file:
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
        if letter not in values[value]:
            values[value].append(letter)
    # Convierte el diccionario a una lista de tuplas y ordena por el valor
    sorted_values = sorted(values.items())
    # Ordena las letras en cada lista
    for i in range(len(sorted_values)):
        sorted_values[i] = (sorted_values[i][0], sorted(sorted_values[i][1]))
    # Retorna la lista de tuplas
    return sorted_values


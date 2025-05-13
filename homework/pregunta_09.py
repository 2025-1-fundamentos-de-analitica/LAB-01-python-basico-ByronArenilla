"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open ('files/input/data.csv', 'r') as file:
        lines = file.readlines()
    # Inicializa un diccionario para contar las claves
    counts = {}
    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la coma como separador
        columns = line.strip().split('\t')
        # Obtiene el valor de la quinta columna (índice 4)
        values = columns[4].split(',')
        # Itera sobre cada valor en la columna 5
        for value in values:
            # Separa la clave y el valor usando `:` como separador
            key, val = value.split(':')
            # Si la clave no está en el diccionario, la inicializa en 0
            if key not in counts:
                counts[key] = 0
            # Incrementa el contador para esa clave
            counts[key] += 1
    # Retorna el diccionario con los conteos
    return counts


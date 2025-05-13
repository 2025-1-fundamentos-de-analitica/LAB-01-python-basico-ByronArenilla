"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()
    # Inicializa un diccionario para almacenar los valores mínimos y máximos
    min_max_values = {}
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
            # Convierte el valor a entero
            val = int(val)
            # Si la clave no está en el diccionario, inicializa su min y max
            if key not in min_max_values:
                min_max_values[key] = [val, val]
            else:
                # Actualiza el valor mínimo y máximo para esa clave
                min_max_values[key][0] = min(min_max_values[key][0], val)
                min_max_values[key][1] = max(min_max_values[key][1], val)
    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    sorted_min_max = sorted([(key, v[0], v[1]) for key, v in min_max_values.items()])
    # Retorna la lista de tuplas
    return sorted_min_max

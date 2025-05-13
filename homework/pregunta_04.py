"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    with open('files/input/data.csv','r') as file:
        lines = file.readlines()
    # Inicializa un diccionario para contar los registros por mes
    counts = {}
    # Itera sobre cada línea del archivo
    for line in lines:
        # Divide la línea en columnas usando la coma como separador
        columns = line.strip().split('\t')
        # Obtiene la fecha de la tercera columna (índice 2)
        date = columns[2]
        # Extrae el mes de la fecha (los dos primeros caracteres)
        month = date[5:7]
        # Si el mes no está en el diccionario, lo inicializa en 0
        if month not in counts:
            counts[month] = 0
        # Incrementa el contador para ese mes
        counts[month] += 1
    # Convierte el diccionario a una lista de tuplas y ordena alfabéticamente
    sorted_counts = sorted(counts.items())
    # Retorna la lista de tuplas
    return sorted_counts
print(pregunta_04())
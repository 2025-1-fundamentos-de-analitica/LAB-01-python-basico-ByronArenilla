"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    with open('files/input/data.csv', 'r') as file:
            lines = file.readlines()

            resultado = []

            for line in lines:
                columns = line.strip().split('\t')

                letra = columns[0]

                # Contar elementos en columna 4 (por comas)
                col4 = columns[3].split(',') if columns[3] else []
                count_col4 = len(col4)

                # Contar elementos en columna 5 (por comas)
                col5 = columns[4].split(',') if columns[4] else []
                count_col5 = len(col5)

                resultado.append((letra, count_col4, count_col5))

            return resultado


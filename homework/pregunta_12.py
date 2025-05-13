"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    resultado = {}

    for line in lines:
        columns = line.strip().split('\t')
        letra_col1 = columns[0]
        col5 = columns[4].split(',')  # separar cada 'clave:valor'

        suma = 0
        for par in col5:
            clave, valor = par.split(':')
            suma += int(valor)

        # Acumular suma en el diccionario
        if letra_col1 not in resultado:
            resultado[letra_col1] = 0
        resultado[letra_col1] += suma

    return dict(sorted(resultado.items()))


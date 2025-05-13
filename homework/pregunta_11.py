"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """
    with open('files/input/data.csv', 'r') as file:
        lines = file.readlines()

    resultado = {}

    for line in lines:
        columns = line.strip().split('\t')
        valor_col2 = int(columns[1])
        letras_col4 = columns[3].split(',')  # ← separar por comas

        for letra in letras_col4:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += valor_col2

    # Ordenar el diccionario por claves alfabéticamente
    return dict(sorted(resultado.items()))

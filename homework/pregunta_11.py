"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    letras = {}
    conteo = []

    with open("files/input/data.csv") as file:
        for fila in file:
            fila = fila.split()
            numero = fila[1]
            numero = int(numero)
            letra = fila[3].split(",")
            for i in letra:
                if i not in letras:
                    letras[i] = numero
                else:
                    letras[i] += numero
    return dict(sorted(letras.items()))

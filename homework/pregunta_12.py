"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    letras = {}
    conteo = []

    with open("files/input/data.csv") as file:
        for fila in file:
            fila = fila.split()
            letra = fila[0]
            numero = fila[4].split(",")
            for i in numero:
                numero = i.split(":")[1]
                numero = int(numero)
                if letra not in letras:
                    letras[letra] = numero
                else:
                    letras[letra] += numero
    return dict(sorted(letras.items()))
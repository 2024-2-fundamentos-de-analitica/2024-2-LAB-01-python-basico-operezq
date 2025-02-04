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
    letras = {}
    conteo = []

    with open("files/input/data.csv") as file:
        for fila in file:
            letra = fila[0]
            columna = fila.split()
            numero = int(columna[1])
            if letra in letras:
                letras[letra][0] = max(letras[letra][0],numero)
                letras[letra][1] = min(letras[letra][1],numero)
            else:
                 letras[letra] = [numero,numero]
    for key,value in letras.items():
        conteo.append((key,value[0], value[1]))        

    return sorted(conteo)


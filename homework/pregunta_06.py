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
    letras = {}
    conteo = []

    with open("files/input/data.csv") as file:
        for fila in file:
            fila = fila.split()[4].split(",")
            for grupo in fila:
                letra,numero = grupo.split(":")
                numero = int(numero)
                if letra in letras:
                    letras[letra][0] = min(letras[letra][0],numero)
                    letras[letra][1] = max(letras[letra][1],numero)
                else:
                    letras[letra] = [numero,numero]
    for key,value in letras.items():
        conteo.append((key,value[0], value[1]))   

    return sorted(conteo)

print(pregunta_06())
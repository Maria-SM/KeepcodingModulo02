#crear una funcion que como parametro de entrada tenga un año y devuelva "true" si es bisiesto
#y "false" si no lo es.

#Condiciones del Bisiesto:
'''-Cualquier año divisible entre 400 es bisiesto
-De los restantes, cualquier año divisible entre 100 no es bisiesto
-De los restantes, cualquier año divisible entre 4 es bisiesto
-Los demas no son bisiestos'''


def Bisiesto (año):
    index = 0
    for año in lista_años:
        if lista_años[index] %400 ==0 and año % 100 ==0:
            return año
        index = index + 1

lista_años = (1950, 1652, 2000, 1265)

año_bisiesto = Bisiesto(lista_años)
print("los años bisiestos son:" , año_bisiesto)

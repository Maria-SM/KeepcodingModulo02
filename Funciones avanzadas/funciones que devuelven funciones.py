#una funcion que devuelve una funcion

#funcion que devuelva el maximo de los parametros de entrada

#lista = (2,5,9,7,6,4,3)

funciones = {'max':'maxi', 'min': 'mini'}

def max (*lista):
    if len(lista) == 0:  #si la longitud de la lista es vacía me devuelves 0
        return 0
    maximo = lista[0]   #si no, me vas a crear una variable a partir del primer elemento de la lista
    
    for i in range(1, len(lista)):
        if lista[i]> maximo:
            maximo = lista[i]
    return maximo

def returnF(nombre):
    if nombre in funciones.keys():
        
        return funciones[nombre]  #me devolverá el valor del nombre del diccionario "funciones"

#print(max(*lista))
       #ó
#print(max(2,5,9,7,6,4,3))
print(returnF('max')(2,5,7,9,6,4))
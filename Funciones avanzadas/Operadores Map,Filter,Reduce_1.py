############ REDUCE ###############

from functools import reduce

sumatorio = reduce(lambda x,y:x+y,range(101))

print(sumatorio)

############ MAP ##################
#A)
def doblar(numero):
    return numero *2

numeros = [2,5,10,23,50,33]
resultado = list(map(doblar, lista))

print(resultado)

#Esto lo podriamos hacer sin usar MAP
def multiplicar(numero):
    nuevaLista = []

for n in lista:
    producto = n*2
    nuevaLista.append(producto)
return nuevaLista

lista = [2,5,10,23,50,33]
print(multiplicar(lista))

#B)
def multiply(x):
    return(x*x)

def add(x):
    return(x+x)

functions = [multiply, add]

for n in range(5):
    value = list(map(labmda x:x(i), functions))
    print(value)

########## FILTER #############
#A)
numeros = [2,5,10,23,,50,33]
resultado = list(filter(labmda x:x%2==0, numeros))
print(resultado)

#B)
numeros= range[-5,5]
less_than_zero = list(filter(lambda x:x>0, numeros))
print(less_than_zero)






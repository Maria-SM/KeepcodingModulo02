
#La RECURSIVIDAD o funciones recursivas son funciones que para repetirse se invocan a sí mismas.

#A)
def sumatorio(n):
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0

resultado = sumatorio(4)
print(resultado)

    
#B)   
def retrocontador (numero):
    print("{},".format(numero), end="")
    if numero==0:
        return
    retrocontador(numero-1)
    
retrocontador(10)

#En vez de poner "if numero==0 : return ", podriamos haber puesto:

def retrocontador (numero):
    print("{},".format(numero), end="")
    if numero>0:
        retrocontador(numero-1)
    
retrocontador(10)


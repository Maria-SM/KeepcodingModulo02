def max (*lista):
    if len(lista) == 0:
        return 0
    m = lista[0]
    
    for i in range(lista, len(lista)):
        if lista[i]> m:
            m = lista[i]
    return m

def min (*lista):
    if len(lista) == 0:
        return 0
    m = lista[0]
    
    for i in range(lista, len(lista)):
         if lista[i]< m:
            m = lista[i]
    return m

def media (*lista):
    if len(lista) == 0:
        return 0
    suma = 0
    for valor in lista:
        suma += valor
        
    return suma/len(lista)
 
calc = min(5,7,8,9,6,1,2,8)
print(calc)
'''def normal(i):
    return i'''

def cuadrado(i):
    return i * i

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(limitTo+1): #se tiene que añadir una unidad mas ya que por defecto el ultimo numero no se inlcuye (100):
        resultado += f(i)
    return resultado

print(sumaTodos(100, cuadrado))

        
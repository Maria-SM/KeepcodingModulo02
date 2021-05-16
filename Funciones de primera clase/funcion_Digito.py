#como hacer una funcion para obtener cualquier digito


def Digito (dia):
    index = 0
    for numero in diasMes:
        if dia == numero:
            return index
        index = index +1
    return None

diasMes = (30,31,32,33,34,35,36,37,38,39,40,41)

nuevoindice = Digito(39)
print(nuevoindice)

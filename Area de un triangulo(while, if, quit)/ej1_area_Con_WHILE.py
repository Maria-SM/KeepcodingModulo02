def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

B = input("base del triangulo: ")
while not esDecimal(B):
    print(B, "debe ser un numero")
    B = input("base del triangulo: ")

H = input("altura del triangulo: ")
while not esDecimal(H):
    print(H, "debe ser un numero")
    H = input("altura del triangulo: ")

b = float(B)
h = float(H)

area = b * h/2
print(round(area,2))
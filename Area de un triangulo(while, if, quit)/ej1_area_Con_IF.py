def esDecimal(numero):
    try:
        float(numero)
        return True
    except:
        return False

B = input("base del triangulo: ")
if esDecimal(B):
    b = float(B)
    H = input("base del triangulo: ")
    if esDecimal(H):
        h = float(H)
        area = b * h/2
        print(round(area,2))
    else:
        print(H, "debe ser un numero")
else:
    print(B, "debe ser un numero")   
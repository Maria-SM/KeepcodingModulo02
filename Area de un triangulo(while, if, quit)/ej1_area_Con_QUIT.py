def esDecimal(numero):  
    try:
        float(numero)   # si el numero es flotante, devuelve true
        return True
    except:
        return False
    
B = input("inserta numero: ") #si el contenido de B tiene un formato compatible con un número flotante, 
if esDecimal(B):              #transforma B en flotante y asignalo a la nueva variable b (que por tanto será de tipo flotante)
    b = float(B)
else:
    print(B, "debe ser un numero")
    quit()

H = input("altura del triangulo: ")
if esDecimal(H):
    h = float(H)
else:
    print(H, "debe ser un numero")
    quit()

area = b * h/2

print(round(area,2))
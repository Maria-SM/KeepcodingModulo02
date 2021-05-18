unidades = input("cantidad: ")
U = float(unidades)

precio = input("precio_unitario: ")
P = float(precio)

total_items = 0 
precio_total = 0 
total_unitario = 0 

lista_precios = []
lista_unidades = []

while U>0 and P>0:
    total_unitario = U * P
    lista_unidades.append(U)
    lista_precios.append(P)
    
    total_items = total_items + U #/ total_items += U  #aqui estamos acumulando los resultados
    precio_total = precio_total + total_unitario #/ precio_total += P

    unidades = input("cantidad: ")
    U = float(unidades)
    precio = input("precio_unitario: ")
    P = float(precio)
    
for P, U in zip(lista_precios, lista_unidades):
    print(P, "euros -", U, "unidades -", P * U, "euros")
        
#las listas que hemos creado ahora queremos imprimirlas en modo PRO
print("-----------------")
print("Numero de unidades es: ", round(total_items,1))
print("Total precio es: ", round(precio_total,1))
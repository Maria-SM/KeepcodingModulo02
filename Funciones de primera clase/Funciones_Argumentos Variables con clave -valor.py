def imprimeCosas (**cosasCasa):
    if "armario" in cosasCasa:
        print("Yo tengo", cosasCasa["armario"], "armario")
    else:
        print("No tengo ningun armario/n")

imprimeCosas(armario=1, mesa=2, lampara=5)
print("Esto es una linea\nEsto es otra línea")



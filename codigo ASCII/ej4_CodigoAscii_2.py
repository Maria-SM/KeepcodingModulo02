def myUpper(cadena):
    resultado = ""

##Si quiero delimitar los codigos ascii a solo unos cuantos, tengo que incluir la condicion "if"

    for caracter in cadena: #por cada letra de la palabra, transformame la letra minuscula en mayuscula
        codigoCaracter = ord(caracter) #dime cual es el codigo ordinal asociado a esa letra y llamala "codigoCaracter"
        
        if codigoCaracter >= 97 and codigoCaracter <=122:
            codigoMays = codigoCaracter - 32 #A ese codigo le vas a restar 32 para obtener el codigo de la letra mayuscula "CodigoMays"
            caracterMays = chr(codigoMays) #transformame el codigo en su correspondiente letra "CodigoMays"
            resultado = resultado + caracterMays #necesario para que el bucle no sea infinito y complete la cadena entera de caracteres
        else:
            resultado = resultado + caracter #para que  incluya los espacios entre palabras.
    return resultado

palabras = input("inserta palabra en minuscula: ")
print("esta palabra en mayusculas es:", myUpper(palabras))
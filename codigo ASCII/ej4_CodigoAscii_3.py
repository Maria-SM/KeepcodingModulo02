#si quiero averiguar los codigos ASCII de una cadena de caracteres en CHINO:

cadena = "你好"
for caracter in cadena:
   print(caracter, "-", ord(caracter)) #por cada caracter, devuelveme el ordinal ASCII de cada caracter.
    
#______________
    
#for codigo in range(32,115):
    #print(codigo, "-", chr(codigo), end="\t") # end="\t" es para colocar el ouput de forma mas ordenada
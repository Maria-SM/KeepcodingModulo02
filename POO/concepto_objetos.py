'''class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
    
    def ladrar(self):
        if self.peso>= 8:
            print('GUAU, GUAU')
        else:
            print('guau, guau')
 
boxer = Perro('boxer', 4, 5)
pastor = Perro('pastor', 7,9)
terrier = Perro('terrier', 10, 11)

boxer.ladrar()
pastor.ladrar()
terrier.ladrar()'''

########### __str__ #############

class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
    
    def __str__(self):
        return "soy boxer".format(self.nombre)

boxer = Perro('boxer', 3, 10)
print(boxer)
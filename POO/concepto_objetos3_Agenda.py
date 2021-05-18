class Agenda:
    def __init__(self):
        self.contactos=[]
        self.nombre = input("Dime un nombre")
        self.telefono = input ("Dime un telefono")
        self.email = input("Dime un email")
        
    def añadir (self):
        self.contactos.append(self.nombre)
        self.contactos.append(self.telefono)
        self.contactos.append(self.email)
        print(self.contactos)
    
    def buscar (self):
        self.nombre= input("A ver si esta...")
        if self.nombre in self.contactos:
            print(self.nombre, "esta en la lista")
        else:
            self.contactos.append(self.nombre)
            print(self.nombre, "no esta. Ahora la nueva lista es", self.contactos)
    
    def editar (self):
        
agenda = Agenda()
agenda.añadir()
agenda.buscar()

        
    
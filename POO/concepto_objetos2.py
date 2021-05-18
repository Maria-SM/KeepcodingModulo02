class Triangulo:
    def __init__(self):
        self.lado1=int(input("Ingrese el valor del primer lado: "))
        self.lado2=int(input("Ingrese el valor del segundo lado: "))
        self.lado3=int(input("Ingrese el valor del tercer lado: "))
     
    def imprimir(self):
        print("Los lados del triángulo tienen el valor de")
        print("Lado 1: ",self.lado1)
        print("Lado 2: ",self.lado2)
        print("Lado 3: ",self.lado3)
 
    def mayor(self):
        print("El lado mayor es")
        if self.lado1>self.lado2 and self.lado1>self.lado3:
            print("Lado 1: ",self.lado1)
        elif self.lado2>self.lado3:
            print("Lado 2: ",self.lado2)
        else:
            print("Lado 3: ",self.lado3)
 

    def tipo(self):
        if self.lado1==self.lado2 and self.lado1==self.lado3:
            print("Es un triángulo equilátero")
        elif self.lado1!=self.lado2 and self.lado1!=self.lado3:
            print("Es un triángulo escaleno")
        else:
            print("Es un triángulo isósceles")
 
figura=Triangulo()
figura.imprimir()
figura.mayor()
figura.tipo()
import turtle
import random

class Circuito():
    corredores = []
    __postStartY = (-30, -10, 10, 30)
    __colorTurtle = ('red','green', 'orange','blue')
    
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('pink')
        self.__starline = -width/2 + 20    #para asignar una linea de salida
        self.__finishline = width/2 -20
        
        self.__createRunners()
    
    def __createRunners(self):
        
        for i in range(4):
            new_turtle = turtle.Turtle()  #creamos la tortuga
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape('turtle') #le damos forma a la tortuga
            new_turtle.penup() #para eliminar el trazado de lineas al dibujar las tortugas
            new_turtle.setpos(self.__starline, self.__postStartY[i])  #les damos una posicion.
            
            self.corredores.append(new_turtle)   #tenemos que marcar la linea de salida y de llegada
     
    def competir(self):
         hay_ganador = False
         while not hay_ganador:
             for tortuga in self.corredores:
                 avanza = random.randint(1,10)
                 tortuga.forward(avanza)
                 if tortuga.position()[0] >= self.__finishline:
                     hay_ganador = True
                     print("la tortuga {} ha ganado".format(tortuga.color()[0]))
         

if __name__ == "__main__":
    circuito = Circuito(500,500)
    circuito.competir()

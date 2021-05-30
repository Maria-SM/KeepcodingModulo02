
import pygame, sys
from pygame.locals import *

class Termometro(): #lo ponemos antes que la clase "mainApp" porque mencionaremos a "termometro" en "mainApp" class.
    def __init__(self):
        self.custome = pygame.image.load("thermometer.png")

############# ENTRADA ###########
#1/ Atributos: Valor
#2/ Metodos: Update()
        
class Entrada():
    __valor = 0
    __strValue = '0'
    __position = [0,0]
    __size = [0,0]
    
    def __init__(self, value=0):
        self.__font = pygame.font.Sysfont("Arial", 24)
        textBlock = self.__font.render(self.__strValue,True, (74,74,74))
        rect = textBlock.get.rect()
        rect.left = self.__position[0]  #poscicion de la coordenada "x"
        rect.top = self.__position[1]  #poscicion de la coordenada "y"
        rect.size = self.size
    
    #Creamos geters y seters de los atributos privados de "Entrada"
    def value (self, valor=None):
        if valor==None:
            return self.__value
        else:
            valor = str(valor)
            try:
                self.__value = int(valor)
                self.__strValue = valor
            except:
                pass
    
    def width(self, valor=None):
        if valor==None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(valor)
            except:
                pass
        
     def height(self, valor=None):
        if valor==None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(valor)
            except:
                pass
    
    
     def size(self, valor=None):
         if valor==None:
             return self.__size
        else:
            try:
                w = int(valor[0])
                h = int(valor[0])
                self.__size = [int(valor[0]),int(valor[0])]
            except:
                pass
    
      def posX(self, valor=None):
        if valor==None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(valor)
            except:
                pass
            
      def posY(self, valor=None):
        if valor==None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(valor)
            except:
                pass
    
      def pos(self, valor=None):
        if valor==None:
            return self.__position
        else:
            try:
                self.__position = int(valor)
            except:
                pass
            
 ############# MAINAPP ###########
#1/ Atributos: termometro, Entrada,Selector
#2/ Metodos: maincycle()
            
class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((191,236,236))
        
        self.termometro = Termometro()
        self.entrada = Entrada()
        self.entrada.pos((106,58))
        self.entrada.size((133,28))

                
    
    def __onClose (self):
        pygame.quit()
        sys.exit()
    
    def start (self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__onClose()
        
            self.__screen.blit(self.termometro.custome, (70,34))
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    app = mainApp()
    app.start()
############# TERMOMETRO ###########
#1/ Atributos: Custome, Temperatura, tipoUnidad
#2/ Metodos: Convertir()

import pygame, sys
from pygame.locals import *

class Termometro(): #lo ponemos antes que la clase "mainApp" porque mencionaremos a "termometro" en "mainApp" class.
    def __init__(self):
        self.custome = pygame.image.load("thermometer.png")
        
class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set_caption("Termómetro")
        self.__screen.fill((191,236,236))
        
        self.termometro = Termometro()
    
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

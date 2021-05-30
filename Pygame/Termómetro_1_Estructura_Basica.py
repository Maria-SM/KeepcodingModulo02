######### ESTRUCTURA BASICA ##############

import pygame, sys
from pygame.locals import *

class mainApp():
    termometro = None
    entrada = None
    selector = None
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((290, 415))
        pygame.display.set.caption("Termómetro")
        self.__screen.fill((191,236,236))
    
    def __onClose (self):
        pygame.quit()
        sys.exit()
    
    def start (self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__onClose()
            pygame.display.flip()
    

if __name__ == "__main__":
    pygame.init()
    app == mainApp()
    app.start()


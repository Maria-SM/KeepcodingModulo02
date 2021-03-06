import pygame, sys
import random

class Runner():
    def __init__(self, x=0, y=0):
        self.runnerType = pygame.image.load("ufo.png")  
        self.position = [x,y]  #posicion de entrada
        self.name = "ET"
    
    def avanzar(self):  #aqui vamos a avanzar la posicion "x" 
        self.position[0] += random.randint(1,2)
    
class Game():
    runners = []
    __starLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,400))
        self.__background = pygame.image.load("race-track.png")
        pygame.display.set_caption("carrera de bichos")
        
        firstRunner = Runner(self.__starLine,200)
        firstRunner.name = "speedy"
        self.runners.append(firstRunner)  #añado al jugador a la lista de jugadores
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver == True
            
            self.runners[0].avanzar()
            if self.runners[0].position[0] >= self.__finishLine:
                print("{} ha ganado" .format(self.runners[0].name))
                gameOver = True

            self.__screen.blit(self.__background,(320,200))  #dibujamos la pantalla
            self.__screen.blit(self.runners[0].runnerType, self.runners[0].position)  #dibujamos el corredor en la posicion que hemos puesto
            
            pygame.display.flip()  #actualizo/refresco la pantalla 
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()

                
        
        
        
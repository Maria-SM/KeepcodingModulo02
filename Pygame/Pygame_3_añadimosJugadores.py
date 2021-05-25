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
    __postY = (160, 200, 240, 280)
    __names = ("speedy", "caracolillo", "hercules", "camaleon")
    __starLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,400))
        self.__background = pygame.image.load("race-track.png")
        pygame.display.set_caption("carrera de bichos")
        
        for i in range(4):
            TheRunner = Runner(self.__starLine,self.__postY[i])
            TheRunner.name = self.__names[i]
            self.runners.append(TheRunner)  #añado al jugador a la lista de jugadores
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver == True
            
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:  #[0] se refiere a la coordenada "x", no al indice del corredor
                    print("{} ha ganado" .format(runner.name))
                    gameOver = True

            self.__screen.blit(self.__background,(320,200))  #dibujamos la pantalla
            
            '''self.__screen.blit(self.runners[0].runnerType, self.runners[0].position)  #dibujamos el corredor en la posicion que hemos puesto
            self.__screen.blit(self.runners[1].runnerType, self.runners[1].position)  #dibujamos el corredor en la posicion que hemos puesto
            self.__screen.blit(self.runners[2].runnerType, self.runners[2].position)  #dibujamos el corredor en la posicion que hemos puesto
            self.__screen.blit(self.runners[3].runnerType, self.runners[3].position)'''  #dibujamos el corredor en la posicion que hemos puesto
            
            for runner in self.runners:
                self.__screen.blit(runner.runnerType, runner.position)

            pygame.display.flip()  #actualizo/refresco la pantalla 
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()
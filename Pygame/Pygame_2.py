import pygame, sys

class Game():
    runners= []
    __starLine = 20
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,400))
        self.__background = pygame.image.load("ufo.png")
        pygame.display.set_caption("carrera de bichos")
    
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver == True
            
            self.__screen.blit(self.__background,(0,0))
            pygame.display.flip()
        
        pygame.quit()
        sys.quit()

if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()

                
        
        
        
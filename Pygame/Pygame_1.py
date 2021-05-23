import pygame

######## inicializar pygame ################
pygame.init()

######### creación de pantalla ##############
screen = pygame.display.set_mode((500,500))

######### titulo y icon ##################
pygame.display.set_caption("juego de bichos")
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

####### checking event functionalities ###########
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,0,255))
    pygame.display.update()
    
pygame.quit()


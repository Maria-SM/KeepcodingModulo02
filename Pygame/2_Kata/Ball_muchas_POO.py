import pygame as pg
import sys
from random import randint

def rebota_X (x):
    if x <= 0 or x >= ANCHO:
        return -1
    return 1

def rebota_Y (y):
    if y <= 0 or y >= ALTO:
        return -1
    return 1

#defino las variables
ROJO = (255,0,0,)
AZUL= (0,0,255)
VERDE = (0,255,0)
NEGRO = (0,0,0)
ANCHO = 800
ALTO = 600
RADIO = 10

pg.init()
pantalla = pg.display.set_mode((ANCHO,ALTO)) #Creamos una superficie
reloj = pg.time.Clock()

class Bola():
    def __init__(self,x,y,vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

bolas = []
for _ in range(10):
    bola = Bola (randint(0, ANCHO),
            randint(0, ALTO),
            randint(5,10),
            randint(5,10),
            (randint(0,255),randint(0,255),randint(0,255)))
    bolas.append(bola)

game_over = False
while not game_over:
    reloj.tick(60)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT: #evento es una "clase", y "type" su atributo. 
        #Como "quit" pertenece a la libreria "pgygame" hay que escribirlo con el "pg" delante
            game_over = True
    
    #Gestion de estado. (Para mover la bola). 
    for bola in bolas:
        bola.x += bola.vx
        bola.y += bola.vy
        bola.vx *= rebota_X(bola.x)
        bola.vy *= rebota_Y(bola.y)

    #Gestion de la pantalla
    pantalla.fill(NEGRO)
    for bola in bolas:
        pg.draw.circle(pantalla,bola.color, (bola.x,bola.y), RADIO) #como lo queremos dibujar en el centro de la pantalla ponemos 400,300
    
    pg.display.flip() #Para pintar los eventos definidos

pg.quit()
sys.exit()
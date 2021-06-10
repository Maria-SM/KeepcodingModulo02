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

#defino las constantes
ROJO = (255,0,0,)
AZUL= (0,0,255)
VERDE = (0,255,0)
NEGRO = (0,0,0)
ANCHO = 800
ALTO = 600

pg.init()
pantalla = pg.display.set_mode((ANCHO,ALTO)) #Creamos una superficie
reloj = pg.time.Clock()

#Para inicializar la bola ponemos coordenadas de inicio
#BOLA 1
x = ANCHO // 2 # LA doble barra (//) es para no crear decimales
y = ALTO // 2
vx = -5 #vx es velocidad de x
vy = -5

#BOLA 2
x2 = randint (0,ANCHO)
y2 = randint (0,ALTO)
vx2 = randint (5,15)
vy2 = randint (5,15)

game_over = False
while not game_over:
    reloj.tick(60)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT: #evento es una "clase", y "type" su atributo. 
        #Como "quit" pertenece a la libreria "pgygame" hay que escribirlo con el "pg" delante
            game_over = True
    
    #Gestion de estado
    # Para mover la bola. 
    x += vx
    y += vy
    x2 += vx2
    y2 += vy2

    vx *= rebota_X(x)
    vy *= rebota_Y(y)

    vx2 *= rebota_X(x2)
    vy2 *= rebota_Y(y2)

    #Gestion de la pantalla
    pantalla.fill(NEGRO) #para pintar la pantalla cada vez que se ejecute un movimiento de bola. 
    pg.draw.circle(pantalla,ROJO,(x,y),10) #como lo queremos dibujar en el centro de la pantalla ponemos 400,300
    pg.draw.circle(pantalla,VERDE,(x2,y2),10)
    #10 es el radio de la bola
    
    
    pg.display.flip() #Para pintar los eventos definidos

pg.quit()
sys.exit()
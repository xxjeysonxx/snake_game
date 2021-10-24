#from typing import SupportsRound
import pygame
import random
import sys

class cuerpo:
    def moverse(self):
        if self.dir == 0:
         self.x += 10
        elif self.dir == 1:
          self.x -=10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -=10
        
    def __init__(self, ventana):
        self.x = 0
        self.y = 0
        self.dir = 0
        self.ventana = ventana
    
    def dibujar(self):
        pygame.draw.rect(self.ventana,(255,255,255),(self.x, self.y,10,10))

class manzanas:
    def __init__(self, ventana):
        self.x = random.randrange(40)*10
        self.y = random.randrange(40)*10
        self.dir = 0
        self.ventana = ventana
    
    def dibujar(self):
        pygame.draw.rect(self.ventana,(255,0,0),(self.x, self.y,10,10))
    
    def nueva_manzana(self):
        self.x = random.randrange(40)*10
        self.y = random.randrange(40)*10

def refrescar(ventana):
    background=pygame.image.load("bgm.png").convert()

    ventana.blit(background,[0,0])
    #ventana.fill((0,0,0))
    comida.dibujar()
    for i in range(len(serpiente)):
        serpiente[i].dibujar()

def seguir_cabeza():
    for i in range(len(serpiente)-1):
        serpiente[len(serpiente)- i -1].x = serpiente[len(serpiente) -i - 2].x
        serpiente[len(serpiente)- i -1].y = serpiente[len(serpiente) -i - 2].y

def controles(event):
    if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RIGHT:
              serpiente[0].dir = 0
          if event.key == pygame.K_LEFT:
              serpiente[0].dir = 1
          if event.key == pygame.K_DOWN:
              serpiente[0].dir = 2
          if event.key == pygame.K_UP:
              serpiente[0].dir = 3

def coliciones():
    for i in range(len(serpiente) - 2):
            if serpiente[len(serpiente) - i - 1].x == serpiente[0].x and serpiente[len(serpiente) - i - 1].y == serpiente[0].y:
                # Lo que pasa al morir
                run = False

def main():
    global serpiente, comida
    pygame.mixer.init()
    ventana = pygame.display.set_mode((400,400))
    #ventana = pygame.display.set_caption("test")
    #ventana.fill(GREEN)
    background=pygame.image.load("bgm.png").convert()
    sonido = pygame.mixer.Sound("burp.wav")
    #sonido2 = pygame.mixer.Sound("D:\ost.wav")

    ventana.blit(background,[0,0])
    #ventana = pygame.display.set_caption("test")
    comida = manzanas(ventana)
    serpiente = [cuerpo(ventana)]
    run = True
    
    while run:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
              run= False
        controles(event)
        #background = image.load(sandbox_bgm.png)
        #background= transform.scale(background,(400,400))
        #ventana.blit(background,(0,0))
       # sonido2.play()
        serpiente[0].moverse()
        refrescar(ventana)
        seguir_cabeza()
        coliciones()
        pygame.display.update()
        pygame.time.delay(50)

        if serpiente[0].x == comida.x and serpiente[0].y == comida.y:
            comida.nueva_manzana()
            serpiente.append(cuerpo(ventana))
            print("objeto eliminado")
            sonido.play()
        seguir_cabeza()
        if serpiente[0].x >=400:
            serpiente[0].x = 0
        if serpiente[0].x <0:
            serpiente[0].x = 390
        #colision y
        if serpiente[0].y >=400:
            serpiente[0].y = 0
        if serpiente[0].y <0:
            serpiente[0].y = 390
if __name__ == '__main__':
    main()
    pygame.quit()
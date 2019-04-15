import pygame
from pygame.locals import *

class Juegos(pygame.sprite.Sprite):
    
    def __init__ (self):
        #Funcion para la imagen y la posicion de la nave
        pygame.sprite.Sprite. __init__ (self)
        self.ImagenNave = pygame.image.load ('Nave.png')
        self.rect = self.ImagenNave.get_rect ()
        self.rect.centerx = (450) #Posicion en x de la nave
        self.rect.centery = (410) #Posicion en y de la nave
        self.listaDisparo = []
        self.Vida = True
        self.velocidad = 20 #Movimiento de la nave
        
    def movimiento (self):
        if self.Vida == True:
            if self.rect.left <=0:
                self.rect.left = 0
            elif self.rect.right >870:
                self.rect.right = 840
            if self.rect.top <=350:
               self.rect.top = 1
            elif self.rect.bottom > 900:
               self.rect.bottom = 2
                
    def disparar (self, x,y):
        miBala = Bala (x,y)
        self.listaDisparo.append(miBala)

    def dibujar (self, superficie):
        superficie.blit (self.ImagenNave, self.rect)
        
class Bala (pygame.sprite.Sprite):
    
    def __init__ (self, x, y):
        pygame.sprite.Sprite. __init__ (self)
        self.imagenproyectil = pygame.image.load ('disparo1.png')
        self.rect = self.imagenproyectil.get_rect ()
        self.velocidadDisparo = 4
        self.rect.top = y
        self.rect.left = x
        
    def trayectoria (self):
        self.rect.top = (self.rect.top - self.velocidadDisparo)
        
    def dibujar (self, superficie):
        superficie.blit(self.imagenproyectil, self.rect)
        
def main():
    pygame.init()
    venta = pygame.display.set_mode((900,480)) # Creacion de la ventana 
    pygame.display.set_caption("Space Invaders") # Nombre de la ventana
    ImagenFondo = pygame.image.load('fondo.jpg') # Imagen de fondo para la ventana

    jugador = Juegos()
    DemoBala = Bala (450,410)
    enJuego = True 
        
    while True:
        jugador.movimiento ()
        DemoBala.trayectoria ()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if enJuego == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.rect.left -= jugador.velocidad
                    elif event.key == K_RIGHT:
                        jugador.rect.right +=jugador.velocidad
                    elif event.key == K_s:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)
                    if event.key == K_UP:
                        jugador.rect.top -= jugador.velocidad
                    elif event.key == K_DOWN:
                        jugador.rect.bottom += jugador.velocidad
                    
        venta.blit(ImagenFondo, (0,0))
        DemoBala.dibujar(venta)
        jugador.dibujar(venta)
        if len (jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar (venta)
                x.trayectoria()
                if x.rect.top <100:
                    jugador.listaDisparo.remove (x)
        pygame.display.update()
            
main()

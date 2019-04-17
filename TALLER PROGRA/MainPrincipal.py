import pygame
from pygame.locals import *
from random import randint
listaEnemigo = []

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

    def movimientoDerecha (self):
        self.rect.right += self.velocidad
        self.__movimiento ()
    def movimientoIzquierda (self):
        self.rect.left -= self.velocidad
        self.__movimiento ()
        
    def __movimiento (self): # Instrucciones de movimiento para la nave del jugador
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
        miBala = Bala (x,y, 'disparo1.png', True)
        self.listaDisparo.append(miBala)

    def dibujar (self, superficie):
        superficie.blit (self.ImagenNave, self.rect)
        
class Enemigo (pygame.sprite.Sprite):  #Clase para el cambio de Imagen de los enemigo
                                       # Para la creacion y para su movimiento
    
    def __init__ (self, x, y, distancia, imagenA, imagenB):
        pygame.sprite.Sprite. __init__ (self)
        
        self.imagenenemigo1 = pygame.image.load (imagenA)
        self.imagenenemigo2 = pygame.image.load (imagenB)

        self.listaImages = [self.imagenenemigo1, self.imagenenemigo2]
        self.posImagen = 0

        self.imagenEnemigo = self.listaImages [self.posImagen]
        self.rect = self.imagenEnemigo.get_rect()
        
        self.listaDisparo = []
        self.velocidad = 1
        self.rect.top = y
        self.rect.left = x
        self.rangoDisparo = 0.1
        self.tiempoCambio = 1
        self. derecha = True
        self.contador = 0
        self.Maxdescenso = self.rect.top + 40
        self.limiteDerecha= x + distancia
        self.limiteIzquierda= x- distancia
        
    def dibujar (self, superficie):
        self.imagenEnemigo = self.listaImages[self.posImagen]
        superficie.blit(self.imagenEnemigo, self.rect)
        
    def comportamientoImages (self, tiempo):
        self.__movimientos()
        self.__ataque()
        if self.tiempoCambio == tiempo:
            self.posImagen += 1
            self.tiempoCambio += 1
        
            if self.posImagen > (len (self.listaImages)-1):
                self.posImagen = 0
                
    def __movimientos (self):
        if self.contador < 3:
            self.__movimientolateral()
        else:
             self.__descenso()
        
    def __descenso (self):
        if self.Maxdescenso == (self.rect.top+20):
            self.contador =0
            
        else:
            self.rect.top += 1
    
            
    def __movimientolateral(self):
        if self.derecha == True:
            self.rect.left = self.rect.left+ self.velocidad
            if self.rect.left > self.limiteDerecha:
                self.derecha = False
                self.contador += 1
        else:
            self.rect.left = self.rect.left - self.velocidad
            if self.rect.left < self.limiteIzquierda:
                self.derecha = True
                self.contador += 1
                
    def __ataque(self):
        if (randint(0,100)<self.rangoDisparo):
            self.__disparo()
    def __disparo(self):
        x,y = self.rect.center
        miBala = Bala (x,y, 'bala2.png',False)
        self.listaDisparo.append(miBala)
                
class Bala (pygame.sprite.Sprite): #Clase para los disparos de la nave jugador y para los enemigos
    
    def __init__ (self, x, y, ruta, personaje):
        pygame.sprite.Sprite. __init__ (self)
        self.imagenproyectil = pygame.image.load (ruta)
        self.rect = self.imagenproyectil.get_rect ()
        self.velocidadDisparo = 4
        self.rect.top = y
        self.rect.left = x

        self.disparoPersonaje = personaje
        
    def trayectoria (self):
        if self. disparoPersonaje == True:
            self.rect.top = (self.rect.top - self.velocidadDisparo)
        else: self.rect.top = self.rect.top + self.velocidadDisparo
        
    def dibujar (self, superficie):
        superficie.blit(self.imagenproyectil, self.rect)
def cargarEnemigos():
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(x,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(x,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(x,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(90,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(90,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(90,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(180,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(180,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(180,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(260,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(260,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(260,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(350,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(350,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(350,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200


    x = 100
    for x in range (1,5):
        enemigo = Enemigo(450,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(450,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(450,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(550,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(550,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(550,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(650,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(650,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(650,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(750,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(750,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(750,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(850,5,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(850,50,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(850,95,40, 'enemigo1.png', 'enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200

def main():
    pygame.init()
    venta = pygame.display.set_mode((900,480)) # Creacion de la ventana 
    pygame.display.set_caption("Space Invaders") # Nombre de la ventana
    ImagenFondo = pygame.image.load('fondo.jpg') # Imagen de fondo para la ventana

#Objetos
    
    jugador = Juegos()
    cargarEnemigos()
    
    enJuego = True
    reloj = pygame.time.Clock()
    
        
    while True:
        reloj.tick(60)
        tiempo = int(pygame.time.get_ticks ()/1000)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if enJuego == True:
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.movimientoIzquierda()
                    elif event.key == K_RIGHT:
                        jugador.movimientoDerecha()
                    elif event.key == K_s:
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)
                    if event.key == K_UP:
                        jugador.rect.top -= jugador.velocidad
                    elif event.key == K_DOWN:
                        jugador.rect.bottom += jugador.velocidad
                    
        venta.blit(ImagenFondo, (0,0))
        jugador.dibujar(venta)
        
        
        if len (jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar (venta)
                x.trayectoria()
                if x.rect.top <-10:
                    jugador.listaDisparo.remove (x)
                    
        if len (listaEnemigo)>0:
                    for enemigo in listaEnemigo:
                        enemigo.comportamientoImages(tiempo)
                        enemigo.dibujar(venta)
                        
                        if len (enemigo.listaDisparo)>0:
                            for x in enemigo.listaDisparo:
                                x.dibujar (venta)
                                x.trayectoria()
                                if x.rect.top >900:
                                    enemigo.listaDisparo.remove (x)
        pygame.display.update()
            
main()

 



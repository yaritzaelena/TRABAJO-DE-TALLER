import pygame
import sys
import os
from pygame.locals import *
from random import randint
from Jugar import *
import time
from holaa import principal


#Constantes globales
venta = pygame.display.set_mode((900,480)) #Ventana
listaEnemigo = []
pygame.init()

class Juegos(pygame.sprite.Sprite): #Clase de la nave 
    
    def __init__ (self):
        #Funcion para la imagen y la posicion de la nave
        pygame.sprite.Sprite. __init__ (self)
        self.ImagenNave = pygame.image.load ('Imagenes/Nave.png') #Imagen de la nave
        self.ImgagenExplosion = pygame.image.load('Imagenes/explosion1.png') #Imagen para cuando le disparan a la nave
        self.rect = self.ImagenNave.get_rect ()
        self.rect.centerx = (450) #Posicion en x de la nave
        self.rect.centery = (410) #Posicion en y de la nave
        self.listaDisparo = [] #Lista para que la nave pueda disparar
        self.Vida = True
        self.velocidad = 20 #Movimiento de la nave
        self.sonidodisparo = pygame.mixer.Sound ('Sonido/disparar.wav')#Sonido del disparo

    def movimientoDerecha (self):
        self.rect.right += self.velocidad
        self.__movimiento ()
    def movimientoIzquierda (self):
        self.rect.left -= self.velocidad
        self.__movimiento ()
        
    def __movimiento (self): # Instrucciones de movimiento para la nave del jugador

#Parametros para el movimiento/
        
        if self.Vida == True:
            if self.rect.left <=0:
                self.rect.left = 0
            elif self.rect.right >870:
                self.rect.right = 840
            if self.rect.top > 400:
               self.rect.top = 1
            elif self.rect.bottom > 900:
               self.rect.bottom = 2
    def destruccion(self): #Funcion cuando la nave 'muere'
        self.Vida = False
        self.velocidad = 0
        self.ImagenNave = self.ImgagenExplosion #Cambio de imagen a una explosion
                
    def disparar (self, x,y): #Funcion para el disparo de la nave
        miBala = Bala (x,y, 'Imagenes/disparo1.png', True) #Imagen del disparo de la nave
        self.listaDisparo.append(miBala)#Agrega la imagen a la lista de disparo
        self.sonidodisparo.play () # Inicia el sonido de disparo

    def dibujar (self, superficie):
        superficie.blit (self.ImagenNave, self.rect) #Dibuja la imagen de la nave
        
class Enemigo (pygame.sprite.Sprite):  #Clase para los invasores
    
    def __init__ (self, x, y, distancia, imagenA, imagenB):
        pygame.sprite.Sprite. __init__ (self)
        
        self.imagenenemigo1 = pygame.image.load (imagenA) #Imagen 1, del invasor
        self.imagenenemigo2 = pygame.image.load (imagenB) #Imagen 2, del invasor

        self.listaImages = [self.imagenenemigo1, self.imagenenemigo2] #Lista de las imagenes del invasor
        self.posImagen = 0 #Posicion en que inicia las imagenes del invasor

        self.imagenEnemigo = self.listaImages [self.posImagen] #Posicion en que inicia las imagenes del invasor
        self.rect = self.imagenEnemigo.get_rect()
        
        self.listaDisparo = [] #Lista para los disparos de los invasores
        self.velocidad = 1 
        self.rect.top = y
        self.rect.left = x
        self.rangoDisparo = (1)
        self.tiempoCambio = 5
        self.conquista = False 
        self. derecha = True
        self.contador = 0
        self.Maxdescenso = self.rect.top + 40
        self.limiteDerecha= x + distancia
        self.limiteIzquierda= x - distancia
        
    def dibujar (self, superficie):
        self.imagenEnemigo = self.listaImages[self.posImagen]
        superficie.blit(self.imagenEnemigo, self.rect)
        
    def comportamientoImages (self, tiempo): # Funcion para el cambio de imagenes de los invasores
        if self.conquista == False:
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
        if (randint(0,1000)<self.rangoDisparo):
            self.__disparo()
    def __disparo(self):
        x,y = self.rect.center
        miBala = Bala (x,y, 'Imagenes/bala2.png',False)
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
def cargarEnemigos(): #Funcion para la posicion de los invasores 
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(x,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(x,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(x,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(90,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(90,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(90,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(180,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(180,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(180,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(260,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(260,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(260,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(350,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(350,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(350,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200


    x = 100
    for x in range (1,5):
        enemigo = Enemigo(450,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(450,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(450,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(550,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(550,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(550,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(650,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(650,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(650,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(750,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(750,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(750,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(850,5,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200

    x = 100
    for x in range (1,5):
        enemigo = Enemigo(850,50,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append (enemigo)
        x = x + 200
    x = 100
    for x in range (1,5):
        enemigo = Enemigo(850,95,40, 'Imagenes/enemigo1.png', 'Imagenes/enemigo2.png',)
        listaEnemigo.append(enemigo)
        x = x + 200

            
        
def detenerJuego(): #Funcion para cuando se pierde 
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo) #Para que el disparo desaparezca
        enemigo.conquista = True # Para que se detenga todo 
def main():
    
    pygame.init()
    principal() #Llamada al menu
    mainn() # Llamada al ingreso de usuario

    # Creacion de la ventana 
    pygame.display.set_caption("Space Invaders") # Nombre de la ventana
    ImagenFondo = pygame.image.load('Imagenes/fondo1.jpg') # Imagen de fondo para la ventana
    miFuenteSistema = pygame.font.SysFont('Arial',30)
    letra18 = pygame.font.SysFont("Arial", 18)
    Texto = miFuenteSistema.render('GAME OVER',0,(248,248,255)) #Texto para cuando se pierda en el jeugo
    marcador = 0
    pygame.mixer.music.load ('Sonido/fondo.mpeg') #Musica de fondo 
    pygame.mixer.music.play(1) # Iniciar musica de fondo
    Siguiente = True
    
    
    

    #Objetos
    puntos = 0
    imagenPuntos = letra18.render('Puntos '+str(puntos), True, (200,200,200), (0,0,0)) #Mostrar puntaje en la pantalla
    rectanguloPuntos = imagenPuntos.get_rect()          
    rectanguloPuntos.left = 830                          
    rectanguloPuntos.top = 440                           
    
 
    jugador = Juegos()
    cargarEnemigos()
    mainloop = True
    enJuego = True
    reloj = pygame.time.Clock()

    while True:
        
        reloj.tick(600)
        tiempo = int(pygame.time.get_ticks ()/1000)
        
        for event in pygame.event.get(): #Quitar el juego
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if enJuego == True: # Manipulacion del teclado (movimiento y disparo)
                if event.type == pygame.KEYDOWN:
                    if event.key == K_LEFT:
                        jugador.movimientoIzquierda()
                    elif event.key == K_RIGHT:
                        jugador.movimientoDerecha()
                    elif event.key == K_s: #Disparar con tecla S
                        
                        x,y = jugador.rect.center
                        jugador.disparar(x,y)
                        
                    if event.key == K_UP:
                        jugador.rect.top -= jugador.velocidad
                    elif event.key == K_DOWN:
                        jugador.rect.bottom += jugador.velocidad
                    
        venta.blit(ImagenFondo, (0,0)) #Mostrar la imagen de fondo
        jugador.dibujar(venta)
        venta.blit(imagenPuntos, rectanguloPuntos) #Mostrar los puntos en la pantalla
        
        if len (jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar (venta)
                x.trayectoria() 
                if x.rect.top <-10:
                    jugador.listaDisparo.remove (x)
                else:
                    for enemigo in listaEnemigo:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            
                            
                                                                                   
        if len (listaEnemigo)>0:
                    for enemigo in listaEnemigo:
                        enemigo.comportamientoImages(tiempo)
                        enemigo.dibujar(venta)
                        if enemigo.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego=False
                            detenerJuego()
                        
                        if len (enemigo.listaDisparo)>0:
                            for x in enemigo.listaDisparo:
                                x.dibujar (venta)
                                x.trayectoria()
                                if x.rect.colliderect(jugador.rect):
                                    jugador.destruccion()
                                    enJuego=False
                                    detenerJuego()
                                if x.rect.top >900:
                                    enemigo.listaDisparo.remove (x)
                                else: 
                                    for disparo in jugador.listaDisparo:
                                        if x.rect.colliderect (disparo.rect):
                                            jugador.listaDisparo.remove(disparo)
                                            enemigo.listaDisparo.remove(x)
        if len (listaEnemigo) == []:
           Siguiente = False
        
        if enJuego == False:
             venta.blit(Texto,(300,300)) #Mostrar texto cuando se pierde
             pygame.mixer.music.stop() #Detener musica de fondo
        pygame.display.update()

main()

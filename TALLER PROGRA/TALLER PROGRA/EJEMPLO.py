import pygame
from pygame.locals import *
import sys


WIDTH = 640
HEIGHT = 480

pygame.init()
    # creamos la ventana y le indicamos un titulo:
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("tutorial pygame parte 4")
    # se define la letra por defecto
fuente = pygame.font.Font(None, 20)

text = "Hola mundo impreso"
mensaje = fuente.render(text, 1, (255, 255, 255))
screen.blit(mensaje, (15, 4))
pygame.display.flip()

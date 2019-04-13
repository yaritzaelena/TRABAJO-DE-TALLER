import pygame
from pygame.locals import *
pygame.init()

def main():
    pygame.display.set_mode((640,480))
    pygame.display.set_caption("Space Invaders")
    
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                exit()
if __name__ == "__main__":
    main()

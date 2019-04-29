import pygame
def principal (): #Funcion para las opciones del menu, posicionamientos.
    pygame.init()
    caca = (85,107,47)
    width = 600
    height = 400
    ventana = pygame.display.set_mode((950,480))
    pygame.display.set_caption ('Mi menu')
    font = pygame.font.SysFont("di mare", 35)
    ImagenFondo = pygame.image.load('Imagenes/space.jpg')
    ventana.blit(ImagenFondo, (0,0))
    # Posicionamiento de las opciones del menu
    title = pygame.Rect(((width/16)+1, (height/8)+1, 7*width/8, height/4))
    menu1 = pygame.Rect(((width/4)+1, (height/2)+1, 2*width/4, height/10))
    menu2 = pygame.Rect(((width/4)+1, (height/2)+1+(3*height/20), 2*width/4, height/10))
    menu3 = pygame.Rect(((width/4)+1, (height/2)+1+(6*height/20), 2*width/4, height/10))
    
    #Opciones del menu
    
    titulo1 = font.render('Space Invaders', True, (0, 128, 0))
    rect_titulo1 = titulo1.get_rect()
    rect_titulo1.center = (width/2,(height/4)+3)

    opcion1 = font.render ('Play', True, (0,0,0))
    rect_opcion1 = opcion1.get_rect ()
    rect_opcion1.center = (width/2,(height/2)+(height/20)+3)

    opcion2 = font.render ('Scores', True, (0,0,0))
    rect_opcion2 = opcion2.get_rect ()
    rect_opcion2.center = (width/2,(height/2)+(4*height/20)+3)

    opcion3 = font.render ('Exit', True, (0,0,0))
    rect_opcion3 = opcion3.get_rect ()
    rect_opcion3.center = (width/2,(height/2)+(7*height/20)+3)
    
    #Dibujar rectangulos de cada opcion
    pygame.draw.rect(ventana, (0,0,150), menu1)
    pygame.draw.rect(ventana, (0,0,150), menu2)
    pygame.draw.rect(ventana, (0,0,150), menu3)
    pygame.draw.rect(ventana, (0,0,150), title)
    # Mostrar opciones en pantalla
    a = ventana.blit (titulo1, rect_titulo1)
    b = ventana.blit (opcion1, rect_opcion1)
    c = ventana.blit (opcion2, rect_opcion2)
    d = ventana.blit (opcion3, rect_opcion3)
    
    gameExit = True
                     
    while gameExit: # Funcionamiento de las opcines del menu al ser seleccionadas
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = False    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if b.collidepoint(pos):
                    gameExit = False
                    
                if c.collidepoint(pos):
                    gameExit = False
                    
                if d.collidepoint(pos):
                    gameExit = False
                    

                
        
        pygame.display.update()
        
    
principal ()

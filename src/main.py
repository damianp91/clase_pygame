import pygame, sys
from settings import *



pygame.init() # Inicializar pygame

clock = pygame.time.Clock()

display = pygame.display.set_mode((WIDTH, HEIGHT)) # Tamaño de la pantalla recomendable sus valores como global asi no se use este comcepto en python 
pygame.display.set_caption("Juego de prueba.")

#rect_1 = pygame.rect.Rect(100, 80, 200, 200) # Para dibujar un rectangulo, los dos primeros en desde donde comienza y lo otros el tamaño del rectan.
#rect_1.center = center_screen
#rect_2 = (300, 150, 120, 90) # lo mismo pero en tupla (construccion)

# Movimiento 

# Superficies
#calco = pygame.Surface((100, 50))
#calco.fill((0, 0, 255))
#rec_calco = calco.get_rect()

y = 300
scuare = pygame.Rect(300, y, 80, 60)
gravity_y = True
gravity_x = True

while True:
    
    # En este espacio manipulamos la velocidadn en la que correra el juego
    clock.tick(FPS)
    
    for event in pygame.event.get(): # Como es de tipo lista aca se van a mostrar todos los eventos que se hagan dentro de la pantalla   
        #-----> Detecta los eventos
        if event.type == pygame.QUIT:
            pygame.quit() # Esta es la inversa de pygame.init aca avisamos que vamos a salir del programa
            sys.exit() # Al momento de dar x a la pantalla va a salir sin mostrar error
    
    
    if gravity_y:
        if scuare.bottom <= HEIGHT:
            scuare.top += SPEED
        else:
            gravity_y = not gravity_y
    else:
        if scuare.top >= 0:
            scuare.top -= SPEED
        else:
            gravity_y = not gravity_y
    
    if gravity_x:
        if scuare.right <= WIDTH:
            scuare.right += SPEED
        else:
            gravity_x = not gravity_x
    else:
        if scuare.left >= 0:
            scuare.left -= SPEED
        else:
            gravity_x = not gravity_x
    
        # Esto es para ver figuras y como construirlas
        #-----> Actualiza los elementos
        #pygame.draw.rect(display, (255, 0, 0),rect_1, 3)
        #pygame.draw.rect(display, (0, 255, 0),rect_2)
    
    display.fill(costume)
    
    pygame.draw.rect(display, green, scuare)
    
        #pygame.draw.line(display, (23, 189, 165), (0, 0), x.center, 3)
        #pygame.draw.ellipse(display, (89, 145, 111), (300, 200, 100, 150))
        
        # Superficie en ejecucion
        #display.blit(calco, x, rec_calco)
    
    #-----> Actualiza la pantalla
    pygame.display.flip()

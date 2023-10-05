import pygame, sys

WIDTH = 600
HEIGHT = 400
center_x = WIDTH // 2
center_y = HEIGHT // 2
center_screen = (center_x, center_y)

pygame.init() # Inicializar pygame

clock = pygame.time.Clock()
FPS = 60

display = pygame.display.set_mode((WIDTH, HEIGHT)) # Tamaño de la pantalla recomendable sus valores como global asi no se use este comcepto en python 
pygame.display.set_caption("Juego de prueba.")
color = display.fill((78, 87, 146)) # Color a la pantalla principal

#rect_1 = pygame.rect.Rect(100, 80, 200, 200) # Para dibujar un rectangulo, los dos primeros en desde donde comienza y lo otros el tamaño del rectan.
#rect_1.center = center_screen
#rect_2 = (300, 150, 120, 90) # lo mismo pero en tupla (construccion)

# Movimiento 
y = 20
soil = HEIGHT - 20

# Superficies
#calco = pygame.Surface((100, 50))
#calco.fill((0, 0, 255))
#rec_calco = calco.get_rect()


while True:
    
    # En este espacio manipulamos la velocidadn en la que correra el juego
    clock.tick(FPS)
    
    for event in pygame.event.get(): # Como es de tipo lista aca se van a mostrar todos los eventos que se hagan dentro de la pantalla   
        #-----> Detecta los eventos
        if event.type == pygame.QUIT:
            pygame.quit() # Esta es la inversa de pygame.init aca avisamos que vamos a salir del programa
            sys.exit() # Al momento de dar x a la pantalla va a salir sin mostrar error
    
    if(y <= soil):
        y += 1
    else:
        y  
    
    print(y)
        # Esto es para ver figuras y como construirlas
        #-----> Actualiza los elementos
        #pygame.draw.rect(display, (255, 0, 0),rect_1, 3)
        #pygame.draw.rect(display, (0, 255, 0),rect_2)
    
    display.fill((78, 87, 146))
    pygame.draw.circle(display, (0, 255, 0), (center_x, y), 20)
    
        #pygame.draw.line(display, (23, 189, 165), (0, 0), x.center, 3)
        #pygame.draw.ellipse(display, (89, 145, 111), (300, 200, 100, 150))
        
        # Superficie en ejecucion
        #display.blit(calco, x, rec_calco)
    
    #-----> Actualiza la pantalla
    pygame.display.flip()

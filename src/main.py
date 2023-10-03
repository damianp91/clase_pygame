import pygame, sys

WIDTH = 800
HEIGHT = 700

pygame.init() # Inicializar pygame

clock = pygame.time.Clock()
FPS = 60

display = pygame.display.set_mode((HEIGHT, WIDTH)) # Tamaño de la pantalla recomendable sus valores como global asi no se use este comcepto en python 
pygame.display.set_caption("Juego de prueba.")
color = display.fill((78, 87, 146)) # Color a la pantalla principal

rect_1 = pygame.rect.Rect(100, 80, 120, 70) # Para dibujar un rectangulo, los dos primeros en desde donde comienza y lo otros el tamaño del rectan.
rect_2 = (300, 150, 120, 90) # lo mismo pero en tupla (construccion)

while True:
    
    # En este espacio manipulamos la velocidadn en la que correra el juego
    clock.tick(FPS)
    
    for event in pygame.event.get(): # Como es de tipo lista aca se van a mostrar todos los eventos que se hagan dentro de la pantalla   
        #-----> Detecta los eventos
        if event.type == pygame.QUIT:
            pygame.quit() # Esta es la inversa de pygame.init aca avisamos que vamos a salir del programa
            sys.exit() # Al momento de dar x a la pantalla va a salir sin mostrar error
        
        #-----> Actualiza los elementos
        pygame.draw.rect(display, (255, 0, 0),rect_1)
        pygame.draw.rect(display, (0, 255, 0),rect_2)
        pygame.draw.circle(display, (0, 0, 255),(WIDTH // 2, HEIGHT // 2), 75, 7)
    
    #-----> Actualiza la pantalla
    pygame.display.flip()

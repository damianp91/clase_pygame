import pygame, sys
from settings import *
from random import randrange


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

# gravity_y = True
# gravity_x = True

cant_coin = 5
count_coins = 0

# Fuente de frase en pantalla
source = pygame.font.Font(None, 30)


scuare = constru_figure(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 40, 40, direction= list_mov[randrange(0, len(list_mov))])

for figure in range(cant_coin):
    figure = constru_figure(randrange(0, WIDTH - coin_w), randrange(15, HEIGHT - coin_h), 15, 15, yellow, ratio= 35)
    coins.append(figure)


while True:
    
    # En este espacio manipulamos la velocidadn en la que correra el juego
    clock.tick(FPS)
    
    for event in pygame.event.get(): # Como es de tipo lista aca se van a mostrar todos los eventos que se hagan dentro de la pantalla   
        #-----> Detecta los eventos
        if event.type == pygame.QUIT:
            pygame.quit() # Esta es la inversa de pygame.init aca avisamos que vamos a salir del programa
            sys.exit() # Al momento de dar x a la pantalla va a salir sin mostrar error
    
        # Esto es para ver figuras y como construirlas
        #-----> Actualiza los elementos
        #pygame.draw.rect(display, (255, 0, 0),rect_1, 3)
        #pygame.draw.rect(display, (0, 255, 0),rect_2)
    
    # Verificacion de choque de la figura y actualizo

    if scuare["scuare"].right >= WIDTH:
        if scuare["direction"] == DR:
            scuare["direction"] = DL
        elif scuare["direction"] == UR:
            scuare["direction"] = UL
    elif scuare["scuare"].bottom >= HEIGHT:
        if scuare["direction"] == DR:
            scuare["direction"] = UR
        elif scuare["direction"] == DL:
            scuare["direction"] = UL
        #scuare["color"] = color_sorprise() # cambio de color, forma, tamaño dependiento de lado que golpee
    elif scuare["scuare"].left <= 0:
        if scuare["direction"] == UL:
            scuare["direction"] = UR
        elif scuare["direction"] == DL:
            scuare["direction"] = DR
    elif scuare["scuare"].top <= 0:
        if scuare["direction"] == UR:
            scuare["direction"] = DR
        elif scuare["direction"] == UL:
            scuare["direction"] = DL
        #scuare["color"] = color_sorprise() # cambio de color, forma, tamaño dependiento de lado que golpee
    
    # Programo la direccion de la figura
    
    if scuare["direction"] == DR:
        scuare["scuare"].top += SPEED
        scuare["scuare"].left += SPEED
    elif scuare["direction"] == DL:
        scuare["scuare"].top += SPEED
        scuare["scuare"].left -= SPEED
    elif scuare["direction"] == UL:
        scuare["scuare"].top -= SPEED
        scuare["scuare"].left -= SPEED
    elif scuare["direction"] == UR:
        scuare["scuare"].top -= SPEED
        scuare["scuare"].left += SPEED
    
    for coin in coins[:]:
        if detected_colition(coin["scuare"], scuare["scuare"]): # Recordar que acá estoy llamando a elementos de un diccionario.
            coins.remove(coin)
            count_coins += 1
            if count_coins >= cant_coin:
                count_coins = 0
    
    # Texto en pantalla
    text = source.render(f"Coins: {count_coins}", True, yellow)
    rect_text = text.get_rect()
    rect_text.center = (center_x, 12)
    
    display.fill(costume)
    tex = display.blit(text, rect_text)
    print(f"{tex} {count_coins}")
    
    pygame.draw.rect(display, scuare["color"], scuare["scuare"], 0, scuare["ratio"])
        
    for coin in coins:
        pygame.draw.rect(display, coin["color"], coin["scuare"], 0, coin["ratio"])
    
        #pygame.draw.line(display, (23, 189, 165), (0, 0), x.center, 3)
        #pygame.draw.ellipse(display, (89, 145, 111), (300, 200, 100, 150))
        
        # Superficie en ejecucion
        #display.blit(calco, x, rec_calco)
    
    #-----> Actualiza la pantalla
    pygame.display.flip()

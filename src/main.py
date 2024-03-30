from settings import *
from random import randrange
from colitions import detected_colition_circle
from constructor import *
from pygame.locals import * # para los eventos y ahorrarme el colocar a cada rato pygame

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

cant_coin = 50
count_coins = 0

# Fuente de frase en pantalla
source = pygame.font.Font(None, 30)

# Sonidos 
coin_sound = pygame.mixer.Sound("./src/sonidos/mario-coin.mp3")
pygame.mixer.music.load("./src/sonidos/super-mario.mp3") # Fondo de juego
pygame.mixer.music.play(-1, 2000)
pygame.mixer.music.set_volume(0.5)

# Imagenes
mario = pygame.image.load("./src/mario-image.png")
iamge_coins = pygame.image.load("./src/coin-image.png")
backround = pygame.transform.scale(pygame.image.load("./src/scene.png"), size_dispaly)
start_image = pygame.transform.scale(pygame.image.load("./src/intro.png"), size_dispaly)

#scuare = constru_figure(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 40, 40, direction= list_mov[randrange(0, len(list_mov))], ratio= 35)
scuare = constru_figure(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), mario, 80, 80, 0, ratio= 35)

coins = []

for figure in range(cant_coin):
    figure = constru_figure(randrange(0, WIDTH - coin_w), randrange(25, HEIGHT - coin_h), iamge_coins, 30, 30, yellow, ratio= 35)
    coins.append(figure)

playing_music = True

# Pantalla de comienzo
display.blit(start_image, origin_display)
advisor_text(display, "Presione cualquie tecla para empezar", source, (WIDTH//2, HEIGHT-60), red, blue)
pygame.display.flip()
wait_player()

while True:
    
    # En este espacio manipulamos la velocidadn en la que correra el juego
    clock.tick(FPS)
    
    for event in pygame.event.get(): # Como es de tipo lista aca se van a mostrar todos los eventos que se hagan dentro de la pantalla   
        #-----> Detecta los eventos
        if event.type == QUIT:
            ended_game()
        
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                pull_right = True
                pull_left = False
            if event.key == K_LEFT:
                pull_left = True
                pull_right = False
            if event.key == K_UP:
                pull_up = True
                pull_down = False
            if event.key == K_DOWN:
                pull_down = True
                ull_up = False
            
            if event.key == K_m:
                if playing_music:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing_music = not playing_music
            
            if event.key == K_p:
                if playing_music:
                    pygame.mixer.music.pause()
                advisor_text(display, "Pause", source, center_screen, red, black)
                pygame.display.flip()
                wait_player()
                if playing_music:
                    pygame.mixer.music.unpause()
        
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                pull_right = False
            if event.key == K_LEFT:
                pull_left = False
            if event.key == K_UP:
                pull_up = False
            if event.key == K_DOWN:
                pull_down = False
    
        # Esto es para ver figuras y como construirlas
        #-----> Actualiza los elementos
        #pygame.draw.rect(display, (255, 0, 0),rect_1, 3)
        #pygame.draw.rect(display, (0, 255, 0),rect_2)
    
    # Verificacion de choque de la figura y actualizo

    # if scuare["scuare"].right >= WIDTH:
    #     if scuare["direction"] == DR:
    #         scuare["direction"] = DL
    #     elif scuare["direction"] == UR:
    #         scuare["direction"] = UL
    # elif scuare["scuare"].bottom >= HEIGHT:
    #     if scuare["direction"] == DR:
    #         scuare["direction"] = UR
    #     elif scuare["direction"] == DL:
    #         scuare["direction"] = UL
    #     #scuare["color"] = color_sorprise() # cambio de color, forma, tamaño dependiento de lado que golpee
    # elif scuare["scuare"].left <= 0:
    #     if scuare["direction"] == UL:
    #         scuare["direction"] = UR
    #     elif scuare["direction"] == DL:
    #         scuare["direction"] = DR
    # elif scuare["scuare"].top <= 0:
    #     if scuare["direction"] == UR:
    #         scuare["direction"] = DR
    #     elif scuare["direction"] == UL:
    #         scuare["direction"] = DL
        #scuare["color"] = color_sorprise() # cambio de color, forma, tamaño dependiento de lado que golpee
    
    # Programo la direccion de la figura
    
    # if scuare["direction"] == DR:
    #     scuare["scuare"].top += SPEED
    #     scuare["scuare"].left += SPEED
    # elif scuare["direction"] == DL:
    #     scuare["scuare"].top += SPEED
    #     scuare["scuare"].left -= SPEED
    # elif scuare["direction"] == UL:
    #     scuare["scuare"].top -= SPEED
    #     scuare["scuare"].left -= SPEED
    # elif scuare["direction"] == UR:
    #     scuare["scuare"].top -= SPEED
    #     scuare["scuare"].left += SPEED
    
    if pull_up and scuare["scuare"].top >= 0:
        scuare["scuare"].top -= SPEED
    if pull_down and scuare["scuare"].bottom <= HEIGHT:
        scuare["scuare"].top += SPEED
    if pull_left and scuare["scuare"].left >= 0:
        scuare["scuare"].left -= SPEED
    if pull_right and scuare["scuare"].right <= WIDTH:
        scuare["scuare"].left += SPEED
    
    for coin in coins[:]:
        if detected_colition_circle(coin["scuare"], scuare["scuare"]): # Recordar que acá estoy llamando a elementos de un diccionario.
            coins.remove(coin)
            coin_sound.play()
            count_coins += 1
            if count_coins >= cant_coin:
                count_coins = 0
                make_coins(cant_coin, coins, iamge_coins)
    
    # Texto en pantalla
    text = source.render(f"Coins: {count_coins}", True, yellow)
    rect_text = text.get_rect()
    rect_text.center = (center_x, 12)
    
    #display.fill(blue)
    display.blit(backround, origin_display)
    tex = display.blit(text, rect_text)
    print(f"{tex} {count_coins}")
    
    #pygame.draw.rect(display, scuare["color"], scuare["scuare"], 0, scuare["ratio"]) #la figura que va detras de mario 
    
    display.blit(scuare["img"], scuare["scuare"])
    
    for coin in coins:
        #pygame.draw.rect(display, coin["color"], coin["scuare"], 0, coin["ratio"])
        display.blit(coin["img"], coin["scuare"])
    
        #pygame.draw.line(display, (23, 189, 165), (0, 0), x.center, 3)
        #pygame.draw.ellipse(display, (89, 145, 111), (300, 200, 100, 150))
        
        # Superficie en ejecucion
        #display.blit(calco, x, rec_calco)
    
    #-----> Actualiza la pantalla
    pygame.display.flip()

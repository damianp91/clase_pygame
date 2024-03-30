from random import randrange

# Screen
WIDTH = 600
HEIGHT = 400
center_x = WIDTH // 2
center_y = HEIGHT // 2
center_screen = (center_x, center_y)
size_dispaly = (WIDTH, HEIGHT)
origin_display = (0, 0)


# Motion speed
FPS = 60


# Speed 
SPEED = 3 # velocidad por pixeles

#colors
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 100)
white = (255, 255, 255)
blue = (0, 0, 255)
costume = (78, 87, 146)

# Color ramdon
def color_sorprise():
    r = randrange(0, 255)
    g = randrange(0, 255)
    b = randrange(0, 255)
    
    return (r, g, b)

# Direction, se sigue esquema de teclado numerico de una compu
# UR = 9
# DR = 3
# DL = 1
# UL = 7
# list_mov = [UR, DR, DL, UL]

pull_up = False
pull_down = False
pull_left = False
pull_right = False

# Dimensiones de las figuras
figure_w = 50
figure_h = 50
coin_w = 50
coin_h = 50


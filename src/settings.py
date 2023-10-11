import pygame
from random import randrange

# Screen
WIDTH = 600
HEIGHT = 400
center_x = WIDTH // 2
center_y = HEIGHT // 2
center_screen = (center_x, center_y)


# Motion speed
FPS = 60


# Speed 
SPEED = 3 # velocidad por pixeles

#colors
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
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
UR = 9
DR = 3
DL = 1
UL = 7
list_mov = [UR, DR, DL, UL]

figure_w = 50
figure_h = 50

#fugure
# scuares = [{"scuare" : pygame.Rect(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 50, 50), "color" : color_sorprise(), "direction" : DL, "ratio" : 35},
#            {"scuare" : pygame.Rect(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 50, 50), "color" : color_sorprise(), "direction" : UL, "ratio" : 35},
#            {"scuare" : pygame.Rect(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 50, 50), "color" : color_sorprise(), "direction" : DR, "ratio" : 35}]

def constru_figure(point_x : int , point_y : int, fig_w : int = 50, fig_h : int = 50, color : tuple = (0, 0, 0), direction : int = 9, ratio : int = 0) -> (dict):
    """Crea una figura de tipo rect segun los parametros que se le den a la funcion, teniendo en cuentas que tiene valores por defecto
        sin conar los dos primeros parametros
    Args:
        point_x (int): coordenada en eje x, point_y (int): coordenada en eje y. 
        Defaults to 50, fig_h : int = 50, color : tuple = (0, 0, 0), 
            direction : int = 9, ratio : int = 0)->(dict.

    Returns:
        tuple: Devuelve un diccionario con los elemantos para dibujar una figura de tipo rect
    """
    return {"scuare" : pygame.Rect(point_x, point_y, fig_w, fig_h), "color" : color, "direction" : direction, "ratio" : ratio}

scuares = []

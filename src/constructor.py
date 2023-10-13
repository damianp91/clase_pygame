import pygame
from settings import *
from random import randrange

#fugure
# scuares = [{"scuare" : pygame.Rect(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 50, 50), "color" : color_sorprise(), "direction" : DL, "ratio" : 35},
#            {"scuare" : pygame.Rect(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 50, 50), "color" : color_sorprise(), "direction" : UL, "ratio" : 35},
#            {"scuare" : pygame.Rect(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 50, 50), "color" : color_sorprise(), "direction" : DR, "ratio" : 35}]


def constru_figure(point_x : int , point_y : int, fig_w : int = 50, fig_h : int = 50, color : tuple = (0, 0, 0), direction : int = 0, ratio : int = 0) -> (dict):
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

coins = []


def make_coins(num_coins : int, list_added : list) -> (list):
    """Crea un objeto de tipo Rect segun pareametros que se le indique 

    Args:
        num_coins (Int): Cantidad de objetos a crear
        list_added (list): lista en la que agregaran los objetos

    Returns:
        lists: Lista con objetos agregados
    """
    for figure in range(num_coins):
        figure = constru_figure(randrange(0, WIDTH - coin_w), randrange(15, HEIGHT - coin_h), 15, 15, yellow, ratio= 35)
        list_added.append(figure)
    
    return list_added

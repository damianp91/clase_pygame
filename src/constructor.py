from pygame.locals import *
from settings import *
from random import randrange
import pygame, sys

#fugure
# scuares = [{"scuare" : pygame.Rect(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 50, 50), "color" : color_sorprise(), "direction" : DL, "ratio" : 35},
#            {"scuare" : pygame.Rect(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 50, 50), "color" : color_sorprise(), "direction" : UL, "ratio" : 35},
#            {"scuare" : pygame.Rect(randrange(0, WIDTH - figure_w), randrange(0, HEIGHT - figure_h), 50, 50), "color" : color_sorprise(), "direction" : DR, "ratio" : 35}]


def constru_figure(point_x : int , point_y : int, image = None, fig_w : int = 50, fig_h : int = 50, color : tuple = (0, 0, 0), direction : int = 0, ratio : int = 0) -> (dict):
    """Crea una figura de tipo rect segun los parametros que se le den a la funcion, teniendo en cuentas que tiene valores por defecto
        sin contar los dos primeros parametros
    Args:
        point_x (int): coordenada en eje x, point_y (int): coordenada en eje y. 
        Defaults to 50, fig_h : int = 50, color : tuple = (0, 0, 0), 
            direction : int = 9, ratio : int = 0)->(dict.

    Returns:
        tuple: Devuelve un diccionario con los elemantos para dibujar una figura de tipo rect
    """
    if image:
        image = pygame.transform.scale(image, (fig_w, fig_h))
        
    return {"scuare" : pygame.Rect(point_x, point_y, fig_w, fig_h), "color" : color, "direction" : direction, "ratio" : ratio, "img": image}


def make_coins(num_coins : int, list_added : list, image = None) -> (list):
    """Crea un objeto de tipo Rect segun pareametros que se le indique 

    Args:
        num_coins (Int): Cantidad de objetos a crear
        list_added (list): lista en la que agregaran los objetos

    Returns:
        lists: Lista con objetos agregados
    """
    for figure in range(num_coins):
        figure = constru_figure(randrange(0, WIDTH - coin_w), randrange(15, HEIGHT - coin_h), image, 15, 15, yellow, ratio= 35)
        list_added.append(figure)
    
    return list_added


def ended_game():
    pygame.quit() # Esta es la inversa de pygame.init aca avisamos que vamos a salir del programa
    sys.exit() # Al momento de dar x a la pantalla va a salir sin mostrar error


def wait_player():
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                ended_game()
            
            if e.type == KEYDOWN:
                if e.type == K_ESCAPE:
                    ended_game()
                return


def advisor_text(surfice, tex, font, coordenates, color_font, color_back= None):
    sup_text = font.render(tex, True, color_font, color_back)
    rect_tex = sup_text.get_rect()
    rect_tex.center = coordenates
    surfice.blit(sup_text, rect_tex)

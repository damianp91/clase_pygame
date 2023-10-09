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

#fugure
scuares = [{"scuare" : pygame.Rect(20, randrange(0, HEIGHT), 60, 60), "color" : color_sorprise(), "ratio" : 30}]
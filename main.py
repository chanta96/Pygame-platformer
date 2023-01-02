import pygame
from random import randint, choice
from sys import exit
from settings import *
from tiles import Tile
from level import Level

# Iniciar pygame
pygame.init()
FPS = 60
size = ((screen_width, screen_height))
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
            exit()
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(FPS)

import pygame
from random import randint, choice
from sys import exit

pygame.init()
HEIGHT = 1200
WIDTH = 700
FPS = 60

level_map = []


size = (HEIGHT,WIDTH)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

game_active = True

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_active = False
            pygame.quit()
            exit()
    
    screen.fill('black')

    pygame.display.update()
    clock.tick(FPS)


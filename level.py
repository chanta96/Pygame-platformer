import pygame
from tiles import Tile
from settings import *
from player import Player

SCREEN_MIN = screen_width/5
SCREEN_MAX = screen_width - SCREEN_MIN
class Level():
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x (self):
        player = self.player.sprite
        player_x = player.rect.centerx 
        direction_x = player.direction.x

        if player_x < SCREEN_MIN and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > SCREEN_MAX and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
    def run(self):
        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        # player tiles
        self.player.update()
        self.player.draw(self.display_surface)
        self.scroll_x()

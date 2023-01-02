import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        # vectors
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            pass

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
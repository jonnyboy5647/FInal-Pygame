import pygame
from pygame.sprite import Sprite
from random import randint

class Medkit(Sprite):
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen
        self.settings = jj_game.settings

        self.image = pygame.image.load("images/tile_0016.png")
        self.rect = self.image.get_rect()

        self.rect.left = self.screen.get_rect().right
        medkit_top_max = 300
        self.rect.top = randint(0, medkit_top_max)

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.medkit_speed
        self.rect.x = self.x

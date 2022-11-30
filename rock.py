import pygame
from pygame.sprite import Sprite
from random import randint


class Rock(Sprite):
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen
        self.settings = jj_game.settings

        self.image = pygame.image.load("images/spaceMeteors_002.png")
        self.rect = self.image.get_rect()

        self.rect.left = self.screen.get_rect().right
        rock_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, rock_top_max)

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.rock_speed
        self.rect.x = self.x

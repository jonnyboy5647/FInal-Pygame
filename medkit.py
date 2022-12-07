import pygame
from pygame.sprite import Sprite
from random import randint


class Medkit(Sprite):
    """Class to represent the medkits in the game"""
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen
        self.settings = jj_game.settings

        self.image = pygame.image.load("images/genericItem_color_102.png")
        self.image = pygame.transform.scale(self.image, (39, 39))  # scales the size of the image to make it smaller
        self.rect = self.image.get_rect()

        self.rect.left = self.screen.get_rect().right
        medkit_top_max = 615
        self.rect.top = randint(615, medkit_top_max) # randomizes where the medkits are spawned

        # Stores the medkit's horizontal location
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.medkit_speed
        self.rect.x = self.x

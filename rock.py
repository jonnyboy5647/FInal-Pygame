import pygame
from pygame.sprite import Sprite
from random import randint


class Rock(Sprite):
    """Class to represent the obstacles in the game"""
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen
        self.settings = jj_game.settings

        self.image = pygame.image.load("images/spaceShips_006.png")
        self.image = pygame.transform.scale(self.image, (39, 39))  # scales the size of the image
        self.rect = self.image.get_rect()

        self.rect.left = self.screen.get_rect().right
        rock_top_max = 615
        self.rect.top = randint(615, rock_top_max)  # randomizes where the obstacle is spawned

        # Stores the obstacle's horizontal location
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.rock_speed
        self.rect.x = self.x

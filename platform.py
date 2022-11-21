import pygame
from pygame.sprite import Sprite


class Platform(Sprite):
    def __init__(self, jj_game):
        super().__init__()
        self.settings = jj_game.settings
        self.surf = pygame.Surface((self.settings.screen_width, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(self.settings.screen_width / 2, self.settings.screen_height - 10))

    def move(self):
        pass




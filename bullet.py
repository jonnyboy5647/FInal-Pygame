import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to show bullet and how it shoots"""
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen
        self.settings = jj_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midbottom = jj_game.player.rect.midbottom

        # Stores bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bullet_speed  # fires the bullet downwards
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet onto the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)

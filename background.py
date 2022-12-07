import pygame


class Background:
    """Class to show the background for the game"""
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen

        self.image = pygame.image.load("images/backgroundCastles.png")

        self.screen_rect = self.screen.get_rect
        self.rect = self.image.get_rect()

    def blitme(self):
        """Draws the background onto the screen"""
        self.screen.blit(self.image, self.rect)


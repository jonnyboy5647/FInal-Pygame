import pygame


class Player:
    """Class to manage player 1"""
    def __init__(self, jj_game):
        self.screen = jj_game.screen
        self.settings = jj_game.settings
        self.screen_rect = jj_game.screen.get_rect()

        # load image of player and its rect
        self.image = pygame.image.load('images/tile_0084.png')
        self.image = pygame.transform.scale(self.image, (40, 50))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center # starting position of player

        # Stores a decimal value for the player's horizontal position
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.jumping = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_acc
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_acc

        # Updates rect object from self.x
        self.rect.x = self.x

    def blitme(self):
        """Draw player at its current location"""
        self.screen.blit(self.image, self.rect)

import pygame


class Player2:
    """Class to manage player 2"""
    def __init__(self, jj_game):
        self.screen = jj_game.screen
        self.settings = jj_game.settings
        self.screen_rect = jj_game.screen.get_rect()

        # load image of player and its rect
        self.image = pygame.image.load('images/character_femaleAdventurer_hold.png')
        self.image = pygame.transform.scale(self.image, (56, 74))
        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen_rect.bottomleft # startig position of player

        # Stores a decimal value for the player's horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.jumping = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_acc
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_acc
        if self.jumping:
            self.y -= self.settings.y_vel
            self.settings.y_vel -= self.settings.gravity
            if self.settings.y_vel < -self.settings.player_jump:
                self.jumping = False
                self.settings.y_vel = self.settings.player_jump

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draws player at the given location"""
        self.screen.blit(self.image, self.rect)

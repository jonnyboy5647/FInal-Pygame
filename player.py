import pygame


class Player:
    def __init__(self, jj_game):
        self.screen = jj_game.screen
        self.settings = jj_game.settings
        self.screen_rect = jj_game.screen.get_rect()

        self.image = pygame.image.load('images/character_malePerson_run0.png')
        self.rect = self.image.get_rect()

        self.rect.bottomleft = self.screen_rect.bottomleft

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
        self.screen.blit(self.image, self.rect)

import pygame


class Player:
    def __init__(self, jj_game):
        self.screen = jj_game.screen
        self.settings = jj_game.settings
        self.screen_rect = jj_game.screen.get_rect()

        self.image = pygame.image.load('images/character_robot_run1.png')
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def move(self):
        self.settings.player_acc = self.settings.vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.settings.player_acc.x = -self.settings.player_acc
        if pressed_keys[K_RIGHT]:
            self.settings.player_acc.x = self.settings.player_acc

        self.settings.player_acc.x += self.settings.vel.x * self.settings.fric
        self.settings.vel += self.settings.player_acc
        self.settings.pos += self.settings.vel + 0.5 * self.settings.player_acc

        if self.pos.x > self.settings.screen_width:
            self.pos.x = 0
        if self.pos < 0:
            self.pos.x = self.settings.screen_width

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.player_acc
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.player_acc

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)

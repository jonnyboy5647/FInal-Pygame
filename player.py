import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen
        self.settings = jj_game.settings
        self.game = jj_game.game

        self.image = pygame.image.load('images/character_robot_run1.png')
        self.rect = self.image.get_rect()

        self.vec = pygame.math.Vector2  # 2 for two dimensional

        self.pos = self.vec((10, 385))
        self.vel = self.vec(0, 0)
        self.acc = self.vec(0, 0)

    def move(self):
        self.acc = self.vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_LEFT]:
            self.acc.x = -self.acc
        if pressed_keys[K_RIGHT]:
            self.acc.x = self.settings.acc

        self.acc.x += self.vel.x * self.settings.fric
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > self.settings.screen_width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = self.settings.screen_width

        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(self.game.player, self.game.platform, False)
        if self.game.player.vel.y > 0:
            if hits:
                self.pos.y = hits[0].rect.top + 1
                self.vel.y = 0

    def jump(self):
        self.vel.y = -8
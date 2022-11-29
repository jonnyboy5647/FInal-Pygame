import sys
import pygame
from settings import Settings
from background import Background
from gamestats import GameStats
from bullet import Bullet
from rock import Rock
from player import Player
from platform import Platform
from random import random

clock = pygame.time.Clock()
clock.tick(60)


class JetpackJoyride:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        tile_size = 1024
        window_size = tile_size

        self.screen = pygame.display.set_mode((window_size, window_size))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Jetpack Joyride")

        self.stats = GameStats(self)
        self.player = Player(self)

        self.platform = Platform(self)

        self.background = Background(self)

        self.bullets = pygame.sprite.Group()
        self.rocks = pygame.sprite.Group()

        self.FramePerSec = pygame.time.Clock()

    def run_game(self):
        while True:
            self._check_events()

            if self.stats.game_active:
                self.player.update()
                self._update_bullets()
                self._update_rocks()
                self._create_rock()

            self._update_screen()

    def _player_hit(self):
        if self.stats.players_left > 0:
            self.stats.players_left -= 1

            self.rocks.empty()
            self.bullets.empty()

        else:
            self.stats.game_active = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.top >= self.settings.screen_height:
                self.bullets.remove(bullet)

    def _create_rock(self):
        if random() < self.settings.rock_frequency:
            rock = Rock(self)
            self.rocks.add(rock)
            print(len(self.rocks))

    def _check_aliens_left_edge(self):
        for rock in self.rocks.sprites():
            if rock.rect.left < 0:
                break

    def _update_rocks(self):
        self.rocks.update()

        if pygame.sprite.spritecollideany(self.player, self.rocks):
            self._player_hit()

        self._check_aliens_left_edge()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

    def _update_screen(self):
        #self.screen.fill(self.settings.bg_color)

        self.background.blitme()
        self.screen.blit(self.platform.image, (0,0))
        self.player.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.rocks.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    jj = JetpackJoyride()
    jj.run_game()

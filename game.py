import sys
import pygame

from pygame import mixer
from player import Player
from background import Background
from gamestats import GameStats
from settings import Settings
from platform import Platform
from rock import Rock
from bullet import Bullet
from medkit import Medkit
from player2 import Player2

from random import random

clock = pygame.time.Clock()
clock.tick(60)


class JetpackJoyride:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((570, 360))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Jetpack Joyride")

        self.stats = GameStats(self)
        self.player = Player(self)
        self.player2 = Player2(self)
        self.background = Background(self)
        self.platform = Platform(self)

        self.bullets = pygame.sprite.Group()
        self.rocks = pygame.sprite.Group()
        self.medkits = pygame.sprite.Group()

        self.FramePerSec = pygame.time.Clock()

    def run_game(self):
        self._background_music()

        while self.stats.game_active:
            self._check_events()

            self.player.update()
            self.player2.update()

            self._update_bullets()

            self._update_rocks()
            self._create_rock()

            self._update_medkits()
            self._create_medkit()

            self._update_screen()

        Font = pygame.font.SysFont('Arial', 60)
        game_over_text = Font.render(f"GAME OVER", True, (200, 200, 200))
        self.screen.fill((0, 0, 0))
        self.screen.blit(game_over_text, (450, 300))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

    def _background_music(self):
        pygame.mixer.music.load("music/background3.wav")
        pygame.mixer.music.play(-1)

    def _player_hit(self):
        if self.stats.players_left > 0:
            self.stats.players_left -= 1

            self.rocks.empty()
            self.bullets.empty()

        else:
            self.stats.game_active = False

    def _player_hit_medkit(self):
        self.stats.players_left += 1

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
        self._check_bullet_rock_collisions()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_rock_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.rocks, True, True)

    def _create_medkit(self):
        if random() < self.settings.medkit_frequency:
            medkit = Medkit(self)
            self.medkits.add(medkit)

    def _check_medkit_left_edge(self):
        for medkit in self.medkits.sprites():
            if medkit.rect.left < 0:
                break

    def _update_medkits(self):
        self.medkits.update()

        if pygame.sprite.spritecollideany(self.player, self.medkits):
            self._player_hit_medkit()

        self._check_medkit_left_edge()

    def _create_rock(self):
        if random() < self.settings.rock_frequency:
            rock = Rock(self)
            self.rocks.add(rock)
            print(len(self.rocks))
        Font = pygame.font.SysFont('Arial', 30)
        score_text = Font.render(f"SCORE: {len(self.rocks)}", True, (0, 0, 0))
        self.screen.blit(score_text, (15, 20))

    def _check_rocks_left_edge(self):
        for rock in self.rocks.sprites():
            if rock.rect.left < 0:
                break

    def _update_rocks(self):
        self.rocks.update()

        if pygame.sprite.spritecollideany(self.player, self.rocks):
            self._player_hit()

        self._check_rocks_left_edge()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mousedown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_d:
            self.player.moving_right = True
        elif event.key == pygame.K_SPACE:
            self.player.jumping = True

        elif event.key == pygame.K_LEFT:
            self.player2.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.player2.moving_right = True
        elif event.key == pygame.K_UP:
            self.player2.jumping = True

    def _check_mousedown_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._fire_bullet()
            bullet_sound = mixer.Sound("music/laser.wav")
            bullet_sound.play()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.player2.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player2.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        self.background.blitme()
        # self.platform.blitme()
        self.player.blitme()
        self.player2.blitme()
        self._create_rock()
        self._create_medkit()
        # self._player_score()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.rocks.draw(self.screen)
        self.medkits.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    jj = JetpackJoyride()
    jj.run_game()

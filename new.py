import sys
import pygame
from pygame.sprite import Sprite
from random import random
from random import randint

clock = pygame.time.Clock()
clock.tick(60)


class Settings:
    def __init__(self):
        vec = pygame.math.Vector2

        self.screen_width = 400
        self.screen_height = 450
        self.bg_color = (0, 0, 0)

        self.player_acc = 0.5
        self.player_fric = -0.12
        self.player_limit = 3
        self.player_pos = vec(10, 385)
        self.player_vel = vec(0, 0)

        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        self.rock_speed = 1.0
        self.rock_frequency = 0.002

        self.fps = 60


class Player:
    def __init__(self, jj_game):
        self.screen = jj_game.screen
        self.settings = jj_game.settings
        self.screen_rect = jj_game.screen.get_rect()

        self.image = pygame.image.load('../images/character_robot_run1.png')
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


class Bullet(Sprite):
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen
        self.settings = jj_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midbottom = jj_game.player.rect.midbottom

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class Rock(Sprite):
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen
        self.settings = jj_game.settings

        self.image = pygame.image.load("../images/spaceMeteors_001.png")
        self.rect = self.image.get_rect()

        self.rect.left = self.screen.get_rect().right
        rock_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, rock_top_max)

        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.rock_speed
        self.rect.x = self.x


class Background(Sprite):
    def __init__(self, jj_game):
        super().__init__()
        self.settings = jj_game.Settings
        self.screen = jj_game.screen

        self.tile_size = 18

        self.ground = pygame.image.load("../images/tile_0000.png")
        self.ground_rect = self.ground.get_rect()
        self.num_tiles = self.settings.screen_width // self.ground_rect.width

        for y in range(656, 720, 18):
            for x in range(0, 1200, 18):
                self.screen.blit(self.ground, (x, y))

        self.rect = self.image.get_rect()

    def draw(self):
        for y in range(self.num_tiles):
            for x in range(self.num_tiles):
                self.screen.blit(self.ground, self.rect)


class GameStats:
    def __init__(self, jj_game):
        self.settings = jj_game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        self.players_left = self.settings.player_limit


class JetpackJoyride:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Jetpack Joyride")

        self.stats = GameStats(self)
        self.player = Player(self)

        self.background = pygame.sprite.Group()

        self.platforms = pygame.sprite.Group()
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

    def _jump_player(self):
        self.player.y = -10

    def _player_hit(self):
        if self.stats.players_left > 0:
            self.stats.players_left -= 1

            self.rocks.empty()
            self.bullets.empty()

        else:
            self.stats.game_active = False

    def _check_player_bottom_collisions(self):
        hits = pygame.sprite.spritecollide(
            self.player, self.background, False)

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
            self._jump_player()
            self._fire_bullet()

        # self.acc = vec(0, 0.5)

        # if event.key == pygame.K_RIGHT:
        # self.acc.x = -acc
        # elif event.key == pygame.K_LEFT:
        # self.acc.x = acc

        # self.acc.x += self.vel.x * fric
        # self.vel += self.acc
        # self.pos += self.vel + 0.5 * self.acc

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.player.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.rocks.draw(self.screen)
        self.background.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    jj = JetpackJoyride()
    jj.run_game()

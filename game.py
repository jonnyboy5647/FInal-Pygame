import sys
import pygame

from pygame import mixer
from player import Player
from background import Background
from gamestats import GameStats
from settings import Settings
from rock import Rock
from bullet import Bullet
from medkit import Medkit
from player2 import Player2

from random import random


class JetpackJoyride:
    """Overall class for game to manage game assets and behavior"""

    def __init__(self):
        """Initialize game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((1024, 660))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Jetpack Joyride")

        self.stats = GameStats(self)
        self.player = Player(self)
        self.player2 = Player2(self)
        self.background = Background(self)

        self.bullets = pygame.sprite.Group()
        self.rocks = pygame.sprite.Group()
        self.medkits = pygame.sprite.Group()

    def run_game(self):
        """main loop for the game"""
        self._background_music()  # plays the background music

        clock = pygame.time.Clock()
        clock.tick(60)

        while self.stats.game_active:
            self._check_events()  # identifies any keyboard and mouse events

            self.player.update()
            self.player2.update()

            self._update_bullets()

            self._update_rocks()
            self._create_rock()

            self._update_medkits()
            self._create_medkit()

            self._update_screen()

        # Game Over screen when player is hit
        Font = pygame.font.SysFont('Arial', 60)
        game_over_text = Font.render(f"GAME OVER", True, (200, 200, 200))
        self.screen.fill((0, 0, 0))
        self.screen.blit(game_over_text, (320, 300))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

    def _background_music(self):
        """plays continuous background music"""
        pygame.mixer.music.load("music/background3.wav")
        pygame.mixer.music.play(-1)

    def _player_hit(self):
        """Sees when the player is hit, which takes away one life"""
        if self.stats.players_left > 0:
            self.stats.players_left -= 1

            self.rocks.empty()
            self.bullets.empty()

        else:
            self.stats.game_active = False

    def _player_hit_medkit(self):
        """Player is given an extra life when medkit is collected"""
        self.stats.players_left += 1

    def _update_bullets(self):
        self.bullets.update()

        # updates the position of the bullet and gets rid of old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom >= self.settings.screen_height:
                self.bullets.remove(bullet)
        self._check_bullet_rock_collisions()

    def _fire_bullet(self):
        """Fires bullet"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_rock_collisions(self):
        """Checks the collision between the bullets and the obstacles"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.rocks, True, True)

    def _score_(self):
        """Shows the users score on the top left of the screen"""
        score = pygame.time.get_ticks() / 1000
        Font = pygame.font.SysFont('Arial', 30)
        score_text = Font.render(f"SCORE: " + str(score), True, (0, 0, 0))
        self.screen.blit(score_text, (15, 20))

    def _create_medkit(self):
        """Creates medkits randomly"""
        if random() < self.settings.medkit_frequency:
            medkit = Medkit(self)
            self.medkits.add(medkit)

    def _check_medkit_left_edge(self):
        # If medkit goes out the left side of the screen, it gets rid of the old medkits
        for medkit in self.medkits.sprites():
            if medkit.rect.left < 0:
                break

    def _update_medkits(self):
        self.medkits.update()

        # updates the position of the medkit and gets rid of old medkits
        if pygame.sprite.spritecollideany(self.player2, self.medkits):
            self._player_hit_medkit()

        self._check_medkit_left_edge()

    def _create_rock(self):
        """Creates obstacles randomly"""
        if random() < self.settings.rock_frequency:
            rock = Rock(self)
            self.rocks.add(rock)
            print(len(self.rocks))

    def _check_rocks_left_edge(self):
        # If obstacle goes out the left side of the screen, it gets rid of the old obstacles
        for rock in self.rocks.sprites():
            if rock.rect.left < 0:
                break

    def _update_rocks(self):
        self.rocks.update()

        # if player 2 and obstacle collide, the player loses a life
        if pygame.sprite.spritecollideany(self.player2, self.rocks):
            self._player_hit()

        self._check_rocks_left_edge()

    def _check_events(self):
        """Checks for any keyboard or mouse inputs"""
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
        """Responds to key presses"""
        if event.key == pygame.K_q:
            sys.exit()

        # keydown events for player 1
        elif event.key == pygame.K_a:
            self.player.moving_left = True
        elif event.key == pygame.K_d:
            self.player.moving_right = True

        # keydown events for player 2
        elif event.key == pygame.K_LEFT:
            self.player2.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.player2.moving_right = True
        elif event.key == pygame.K_UP:
            self.player2.jumping = True

    def _check_mousedown_events(self, event):
        """Checks for any mouse inputs"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._fire_bullet()
            bullet_sound = mixer.Sound("music/laser.wav")  # sound effect when player fires bullet
            bullet_sound.play()

    def _check_keyup_events(self, event):
        """Checks for key releases"""
        if event.key == pygame.K_d:
            self.player.moving_right = False
        elif event.key == pygame.K_a:
            self.player.moving_left = False

        elif event.key == pygame.K_RIGHT:
            self.player2.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player2.moving_left = False

    def _update_screen(self):
        """Update all the images on the screen and flip to the new screen"""
        self.background.blitme()
        self.player.blitme()
        self.player2.blitme()
        self._create_rock()
        self._create_medkit()
        self._check_bullet_rock_collisions()
        self._score_()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.rocks.draw(self.screen)
        self.medkits.draw(self.screen)

        pygame.display.flip()  # displays the most recently drawn screen


# this makes a game instance and allows the game to run
if __name__ == '__main__':
    jj = JetpackJoyride()
    jj.run_game()

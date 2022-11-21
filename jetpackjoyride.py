import pygame
import sys
from settings import Settings
from player import Player
from platform import Platform


class JetpackJoyride:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.platform = Platform(self)
        self.player = Player(self)

        self.FramePerSec = pygame.time.Clock()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        all_sprites = pygame.sprite.Group()
        all_sprites.add(self.platform)
        all_sprites.add(self.player)

        self.platform = pygame.sprite.Group()
        self.platform.add(self.player)

        self.screen.fill((0, 0, 0))
        self.player.update()

        for entity in all_sprites:
            self.screen.blit(entity.surf, entity.rect)
            entity.move()

        pygame.display.update()

        self.FramePerSec.tick(self.settings.fps)

        pygame.display.set_caption("Jumping Game")

    def run_game(self):
        while True:
            self._check_events()

    def _check_events(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.player.jump()


if __name__ == '__main__':
    jj = JetpackJoyride()
    jj.run_game()

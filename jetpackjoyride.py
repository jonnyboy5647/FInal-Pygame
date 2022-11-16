import pygame
import sys
from settings import Settings
from player import Player


class JetpackJoyride:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.player = Player()

        self.vec = pygame.math.Vector2  # 2 for two dimensional

        self.FramePerSec = pygame.time.Clock()

        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Jumping Game")

    def _check_events(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.P1.jump()

    displaysurface.fill((0, 0, 0))
    P1.update()

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    FramePerSec.tick(fps)


if __name__ == '__main__':
    jj = JetpackJoyride()
    jj.run_game()

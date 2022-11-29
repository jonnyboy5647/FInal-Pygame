import pygame


class Platform:
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen

        self.image = pygame.image.load("images/backgroundCastles.png")
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (0, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (18, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (36, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (54, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (72, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (90, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (108, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (126, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (144, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (162, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (180, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (198, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (216, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (234, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (252, 1006))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (270, 1006))
        self.rect = self.image.get_rect()

    def blitme(self, surface):
        surface.blit(self.image, self.rect)

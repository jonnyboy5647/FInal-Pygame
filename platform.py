import pygame


class Platform:
    def __init__(self, jj_game):
        super().__init__()
        self.screen = jj_game.screen

        self.image = pygame.image.load("images/backgroundgrass.png")
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (0, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (18, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (36, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (54, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (72, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (90, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (108, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (126, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (144, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (162, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (180, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (198, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (216, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (234, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (252, 662))
        self.image.blit(pygame.image.load("images/tile_0000.png"),
                        (270, 662))
        self.rect = self.image.get_rect()

    def blitme(self):
        self.screen.blit(self.image, self.rect)

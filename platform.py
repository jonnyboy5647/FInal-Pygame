import pygame


class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((width, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(width / 2, height - 10))

    def move(self):
        pass


PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

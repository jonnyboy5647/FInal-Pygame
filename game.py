import pygame
import sys
from player import Player

TILE_SIZE = 1024
WINDOW_SIZE = TILE_SIZE
pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
back = pygame.image.load("images/backgroundCastles.png")
back_rect = back.get_rect()
screen_rect = screen.get_rect()


num_tiles = screen_rect.width // back_rect.width

background = pygame.surface.Surface((screen_rect.width,
                                     screen_rect.height))

for y in range(num_tiles):
    for x in range(num_tiles):
        background.blit(back, (x * back_rect.width, y * back_rect.height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.blit(background, (0, 0))

    pygame.display.flip()

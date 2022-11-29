import pygame


class Settings:
    def __init__(self):
        vec = pygame.math.Vector2

        self.screen_width = 1024
        self.screen_height = 1024
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
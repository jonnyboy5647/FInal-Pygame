import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        self.player_acc = 1.5
        self.player_limit = 0

        self.gravity = 0.5
        self.player_jump = 18
        self.y_vel = self.player_jump

        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3

        self.rock_speed = 2.5
        self.rock_frequency = 0.0009

        self.medkit_speed = 1.0
        self.medkit_frequency = 0.0005

        self.fps = 60
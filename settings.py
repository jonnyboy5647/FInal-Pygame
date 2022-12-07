import pygame


class Settings:
    """Class to store all settings"""
    def __init__(self):
        # screen settings
        self.screen_width = 1024
        self.screen_height = 660

        # player settings
        self.player_acc = 1.5
        self.player_limit = 0
        self.gravity = 0.125
        self.player_jump = 12
        self.y_vel = self.player_jump

        # bullet settings
        self.bullet_speed = 5
        self.bullet_width = 35
        self.bullet_height = 10
        self.bullet_color = (255, 0, 255)
        self.bullets_allowed = 1

        # obstacle settings
        self.rock_speed = 1.5
        self.rock_frequency = 0.0005

        # medkit settings
        self.medkit_speed = 1
        self.medkit_frequency = 0.00005

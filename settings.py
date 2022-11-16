class Settings:
    def __init__(self):
        self.screen_width = 400
        self.screen_height = 450
        self.acc = 0.5
        self.fric = -0.12
        self.fps = 60

        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 1000

        self.PT1 = platform()
        self.P1 = Player()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(PT1)
        self.all_sprites.add(P1)

        self.platforms = pygame.sprite.Group()
        self.platforms.add(PT1)

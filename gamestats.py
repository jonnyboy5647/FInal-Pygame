class GameStats:
    def __init__(self, jj_game):
        self.settings = jj_game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        self.players_left = self.settings.player_limit
class GameStats:
    """Class to track statistics for game"""
    def __init__(self, jj_game):
        self.settings = jj_game.settings
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        """Statics can change during the game"""
        self.players_left = self.settings.player_limit

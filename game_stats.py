import re

class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        # Start alien invasion in an inactive state
        self.game_active = False

        # High score should never be reset
        self.high_score_doc_return()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1


    def high_score_doc_return(self):
        open_doc = open('HighScore.txt', 'r')
        high_score_search = open_doc.read()

        score_search = re.compile(r'''(
[0-9]+
,
)''', re.VERBOSE)

        score_results = score_search.findall(high_score_search)
        last_score = score_results[-1:]

        num_char = str(last_score)
        num_cut = num_char[2:-3]
        self.high_score = int(num_cut)

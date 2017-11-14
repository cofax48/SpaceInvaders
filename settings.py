#! Settings for alien invasion

class Settings():
    """ A class to store all settings for alien invasion."""

    def __init__(self):
        """Initializ the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (1, 2, 1)

        # ship settings
        self.ship_speed_factor = 1.2
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 230, 230, 230
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed_factor = 1.3
        self.fleet_drop_speed = 15

        # How quickly the gam speeds up
        self.speedup_scale = 1.5
        # How quickly th point alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()
        
        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

         # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """INcrase sped settings and alien point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

#! Alien

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alin in the fleet"""

    def __init__(self, ai_settings, screen):
        """Initialize th alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load th alien image and set its rect attribute
        self.image = pygame.image.load('images/trump.bmp')
        self.rect = self.image.get_rect()

        # Start ach nw alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store th alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alein is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move th alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x

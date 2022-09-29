class Settings:
    """Class to store all of the settings of the game"""

    def __init__(self):
        """Initialise game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (230, 230, 230)

        # Ship settings
        self.ship_speed = 12.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 10.0
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_colour = (199, 14, 32)
        self.bullets_allowed = 10

        # Alien Settings
        self.alien_speed  = 4.0
        self.fleet_drop_speed = 20
        # fleet direction of 1 represents right, -1 represents left
        self.fleet_direction = 1


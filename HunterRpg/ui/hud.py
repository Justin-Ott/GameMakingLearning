# HUD display (health, mana, etc.)
class HUD:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def update(self):
        # Update health, mana, etc. from game manager's player state
        pass

    def draw(self, screen):
        # Draw health bar, mana bar, etc. on the screen
        pass
# Combat screen
from ui.hud import HUD
from ui.skills_menu import SkillsMenu

class BattleScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.hud = HUD(game_manager)
        self.skills_menu = SkillsMenu(game_manager)

    def handle_event(self, event):
        # Handle battle-specific events (e.g. attack, defend, use skill)
        pass

    def update(self):
        # Update battle state, check for win/loss conditions
        pass

    def draw(self, screen):
        # Draw battle background, characters, HUD, etc.
        self.hud.draw(screen)
        self.skills_menu.draw(screen)
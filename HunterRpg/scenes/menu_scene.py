# Menu scene handler
from ui.menu import Menu
class MenuScene:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.menu = None  # Initialize menu instance here

    def enter(self):
        self.menu = Menu(self.game_manager)  # Create menu instance when entering scene

    def exit(self):
        self.menu = None  # Clean up menu instance when exiting scene

    def handle_event(self, event):
        if self.menu:
            return self.menu.handle_event(event)
        return None

    def update(self):
        if self.menu:
            self.menu.update()

    def draw(self, screen):
        if self.menu:
            self.menu.draw(screen)
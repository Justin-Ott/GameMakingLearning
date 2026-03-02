# Main game logic, state management
class GameManager:
    def __init__(self):
        self.state = "menu"  # "menu", "game", "skills", "inventory"
        self.player = None
        self.current_scene = None
        
    def set_state(self, new_state):
        self.state = new_state
        
    def start_game(self):
        self.state = "game"
        # Initialize player, world, etc.
        
    def open_skills_menu(self):
        self.state = "skills"
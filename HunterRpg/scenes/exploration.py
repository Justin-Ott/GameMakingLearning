# Overworld/exploration Delte this later
class Exploration:
    def __init__(self, game_manager):
        self.game_manager = game_manager

    def enter(self):
        print("Entering the overworld...")
        # Here you would load the overworld map and initialize any necessary variables

    def update(self):
        # This method would be called every frame to update the overworld state
        pass

    def exit(self):
        print("Exiting the overworld...")
        # Clean up any resources or save the game state if necessary
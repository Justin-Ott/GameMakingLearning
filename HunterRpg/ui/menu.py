# Main menu navigation
import pygame
class Menu:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.options = ["Start Game", "Skills", "Exit"]
        self.selected_option = 0

    def navigate(self, direction):
        if direction == "up":
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif direction == "down":
            self.selected_option = (self.selected_option + 1) % len(self.options)

    def select(self):
        option = self.options[self.selected_option]
        print(f"Selected option: {option}")
        if option == "Start Game":
            self.game_manager.start_game()
        elif option == "Skills":
            self.game_manager.open_skills_menu() 
        elif option == "Exit":
            self.game_manager.exit_game()
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.navigate("up")
            elif event.key == pygame.K_DOWN:
                self.navigate("down")
            elif event.key == pygame.K_RETURN:
                self.select()
                return "selected"  # Return a signal that an option was selected
        return None  # Return None if no action was taken
    
    def update(self):
        pass  # For now, no dynamic updates needed

    def draw(self, screen):
        screen.fill((25, 30, 30))
        font = pygame.font.Font(None, 36)
        for i, option in enumerate(self.options):
            color = (0, 255, 255) if i == self.selected_option else (100, 100, 100)
            text = font.render(option, True, color)
            screen.blit(text, (350, 200 + i * 50))


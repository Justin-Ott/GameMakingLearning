# Skills upgrade menu
import pygame
from config import Config

class SkillsMenu:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.skills = ["Sword Mastery", "Archery", "Magic"]
        self.selected_skill = 0

    def navigate(self, direction):
        if direction == "up":
            self.selected_skill = (self.selected_skill - 1) % len(self.skills)
        elif direction == "down":
            self.selected_skill = (self.selected_skill + 1) % len(self.skills)

    def upgrade(self):
        skill = self.skills[self.selected_skill]
        # Implement skill upgrade logic here
        print(f"Upgrading {skill}...")

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.navigate("up")
            elif event.key == pygame.K_DOWN:
                self.navigate("down")
            elif event.key == pygame.K_RETURN:
                self.upgrade()
                return "upgraded"  # Return a signal that a skill was upgraded
        return None  # Return None if no action was taken
    
    def update(self):
        pass  # For now, no dynamic updates needed
        
    def draw(self, screen):
        screen.fill(Config.ORANGE)
        font = pygame.font.Font(None, 36)
        for i, skill in enumerate(self.skills):
            color = (0, 255, 255) if i == self.selected_skill else (100, 100, 100)
            text = font.render(skill, True, color)
            screen.blit(text, (350, 200 + i * 50))
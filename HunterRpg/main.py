# Entry point, game loop
import pygame
from ui.skills_menu import SkillsMenu
from config import Config
from game.game_manager import GameManager
from ui.menu import Menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))  # Use config
    pygame.display.set_caption("Hunter RPG")
    
    clock = pygame.time.Clock()
    running = True
    
    game_manager = GameManager()
    menu = Menu(game_manager)
    skills_menu = SkillsMenu(game_manager)  # Initialize skills menu
    state = "menu"  # Initial state

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_manager.state == "menu":
                action = menu.handle_event(event)  
            elif action == "start":
                game_manager.set_state("game")
            elif action == "skills":
                print("In skills state")  # Debug line
                game_manager.set_state("skills")
            elif action == "quit":
                running = False

        if game_manager.state == "menu":
            menu.update()
            menu.draw(screen)
        elif game_manager.state == "skills":
            skills_menu.update()
            skills_menu.draw(screen)

        pygame.display.flip()
        clock.tick(Config.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
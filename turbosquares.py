import pygame
from src.data import constants
from src.components import screens, squares


# Setup
pygame.init()
game_display = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
pygame.display.set_caption('Turbo Squares 2.0')
clock = pygame.time.Clock()
small_font = pygame.font.Font('res/fonts/freesans.ttf', 20)
large_font = pygame.font.Font('res/fonts/freesans.ttf', 40)


def main():
    current_screen = screens.MainMenuScreen(small_font, large_font)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit_game()

        current_screen.update(events)
        current_screen.render(game_display)

        pygame.display.update()
        clock.tick(constants.FPS)


def exit_game():
    pygame.quit()
    quit()


main()

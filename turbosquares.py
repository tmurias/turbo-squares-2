import pygame
from src.data import constants
from src.components import screens, squares


# Setup
pygame.init()
icon = pygame.image.load('res/images/icon.png')
pygame.display.set_icon(icon)
game_display = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))
pygame.display.set_caption('Turbo Squares 2.0')
icon = pygame.image.load('res/images/icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
small_font = pygame.font.Font('res/fonts/buster.ttf', 20)
large_font = pygame.font.Font('res/fonts/buster.ttf', 50)
background = pygame.image.load('res/images/background.png')


def main():
    current_screen = screens.MainMenuScreen(play)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit_game()

        current_screen.update(events)

        game_display.blit(background, (0, 0))
        current_screen.render(game_display)

        pygame.display.update()
        clock.tick(constants.FPS)


def play():
    print 'Play'


def exit_game():
    pygame.quit()
    quit()


main()

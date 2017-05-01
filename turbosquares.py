import pygame
from src.data import constants
from src.components import screens


class Main(object):

    def __init__(self):
        pygame.init()
        icon = pygame.image.load('res/images/icon.png')
        pygame.display.set_icon(icon)
        self.game_display = pygame.display.set_mode((constants.DISPLAY_WIDTH,
                                                    constants.DISPLAY_HEIGHT))
        pygame.display.set_caption('Turbo Squares 2.0')
        self.clock = pygame.time.Clock()
        self.small_font = pygame.font.Font('res/fonts/buster.ttf', 20)
        self.large_font = pygame.font.Font('res/fonts/buster.ttf', 50)
        self.background = pygame.image.load('res/images/background.png')
        self.current_screen = screens.MainMenuScreen(self.play_pressed, self.survival_pressed)

    def start(self):
        curr_time = pygame.time.get_ticks()

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.exit_game()

            # Update
            elapsed_time = pygame.time.get_ticks() - curr_time
            curr_time = pygame.time.get_ticks()
            self.current_screen.update(events, elapsed_time)

            # Render
            self.game_display.blit(self.background, (0, 0))
            self.current_screen.render(self.game_display)

            pygame.display.update()
            self.clock.tick(constants.FPS)

    def play_pressed(self):
        self.current_screen = screens.LevelsGameScreen(self.die)

    def survival_pressed(self):
        self.current_screen = screens.SurvivalGameScreen(self.die)

    def die(self):
        self.current_screen = screens.MainMenuScreen(self.play_pressed, self.survival_pressed)

    def exit_game(self):
        pygame.quit()
        quit()


Main().start()

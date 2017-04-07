import pygame
from .. data import constants
from buttons import Button
from squares import GoodSquare, BadSquare


class Screen(object):

    def __init__(self):
        pass

    def show_text(self, text, colour, x, y, font, game_display):
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.center = x, y
        game_display.blit(text_surface, text_rect)


class MainMenuScreen(Screen):

    def __init__(self, on_play_clicked):
        self.on_play_clicked = on_play_clicked

        self.title_font = pygame.font.Font('res/fonts/buster.ttf', 50)
        self.button_font = pygame.font.Font('res/fonts/buster.ttf', 25)
        self.button_font_hover = pygame.font.Font('res/fonts/buster.ttf', 30)

        self.play_button = Button(constants.DISPLAY_WIDTH * 0.5,
                                  constants.DISPLAY_HEIGHT * 0.4,
                                  225, 50,
                                  constants.GREEN,
                                  self.button_font, self.button_font_hover,
                                  "START GAME", self.on_play_clicked)

    def update(self, events, elapsed_time):
        self.play_button.update(events, pygame.mouse.get_pos())

    def render(self, game_display):
        self.show_text('Turbo Squares 2.0', constants.RED, constants.DISPLAY_WIDTH * 0.5,
                       constants.DISPLAY_HEIGHT * 0.15, self.title_font, game_display)

        self.play_button.render(game_display)


class GameScreen(Screen):

    def __init__(self, on_death):
        self.on_death = on_death

        # Sprite containers to make collision detection and rendering easier
        self.bad_squares = pygame.sprite.Group()
        self.all_squares = pygame.sprite.Group()

        # Spawn the good square
        self.good_square = GoodSquare(constants.DISPLAY_WIDTH / 2,
                                      constants.DISPLAY_HEIGHT / 2,
                                      20, 0)
        self.all_squares.add(self.good_square)

        self.score = 0

    def update(self, events, elapsed_time):
        for square in self.all_squares:
            square.update(events, elapsed_time)

    def render(self, game_display):
        pass

import pygame
from .. data import constants
from buttons import Button


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

    def update(self, events):
        self.play_button.update(events, pygame.mouse.get_pos())

    def render(self, game_display):
        self.show_text('Turbo Squares 2.0', constants.RED, constants.DISPLAY_WIDTH * 0.5,
                       constants.DISPLAY_HEIGHT * 0.15, self.title_font, game_display)

        self.play_button.render(game_display)

import pygame
from .. data import constants


class Screen(object):

    def __init__(self):
        pass

    def show_text(self, text, colour, x, y, font, game_display):
        text_surface, text_rect = self.text_objects(text, colour, font)
        text_rect.center = x, y
        game_display.blit(text_surface, text_rect)

    def text_objects(self, text, colour, font):
        text_surface = font.render(text, True, colour)
        return text_surface, text_surface.get_rect()


class MainMenuScreen(Screen):

    def __init__(self, small_font, large_font):
        self.small_font = small_font
        self.large_font = large_font

    def update(self, events):
        pass

    def render(self, game_display):
        game_display.fill(constants.WHITE)
        self.show_text('Main Menu', constants.BLACK, constants.DISPLAY_WIDTH / 2,
                       constants.DISPLAY_HEIGHT / 2, self.large_font, game_display)

import pygame
import random
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

        self.bad_squares = pygame.sprite.Group()

        # Spawn the good square
        self.good_square = GoodSquare(constants.DISPLAY_WIDTH / 2,
                                      constants.DISPLAY_HEIGHT / 2,
                                      constants.GOOD_SQUARE_SPEED, 0)

        for i in range(0, 10):
            bad_square = BadSquare()
            self.bad_squares.add(bad_square)

        self.score = 0

        # Keeps track of the last time a bad square was spawned
        self.time_since_spawn = 0

    def update(self, events, elapsed_time):
        self.time_since_spawn += elapsed_time

        if self.time_since_spawn >= 1000:
            self.spawn_bad_square()
            self.time_since_spawn = 0

        self.good_square.update(events, elapsed_time)
        for square in self.bad_squares:
            square.update(events, elapsed_time)

    def render(self, game_display):
        self.good_square.render(game_display)
        for bad_square in self.bad_squares:
            if bad_square.active:
                bad_square.render(game_display)

    def spawn_bad_square(self):
        for bad_square in self.bad_squares:
            if not bad_square.active:
                bad_square.active = True
                side = random.randint(0, 3)
                if side == 0:
                    # Spawn on left
                    y_slot = random.randint(0, 9)
                    bad_square.position_in_x_slot(-1)
                    bad_square.position_in_y_slot(y_slot)
                    bad_square.x_speed = constants.BAD_SQUARE_SPEED
                    bad_square.y_speed = 0
                elif side == 1:
                    # Spawn on right
                    y_slot = random.randint(0, 9)
                    bad_square.position_in_x_slot(15)
                    bad_square.position_in_y_slot(y_slot)
                    bad_square.x_speed = -constants.BAD_SQUARE_SPEED
                    bad_square.y_speed = 0
                elif side == 2:
                    # Spawn on top
                    x_slot = random.randint(0, 14)
                    bad_square.position_in_x_slot(x_slot)
                    bad_square.position_in_y_slot(-1)
                    bad_square.x_speed = 0
                    bad_square.y_speed = constants.BAD_SQUARE_SPEED
                elif side == 3:
                    # Spawn on bottom
                    x_slot = random.randint(0, 14)
                    bad_square.position_in_x_slot(x_slot)
                    bad_square.position_in_y_slot(10)
                    bad_square.x_speed = 0
                    bad_square.y_speed = -constants.BAD_SQUARE_SPEED
                break

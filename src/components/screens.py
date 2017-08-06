import pygame
import random
from .. data import constants
from buttons import Button
from squares import GoodSquare, BadSquare
from levels import Level1, Level2


class Screen(object):

    def __init__(self):
        pass

    def show_text(self, text, colour, x, y, font, game_display):
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.center = x, y
        game_display.blit(text_surface, text_rect)


class MainMenuScreen(Screen):

    def __init__(self, on_play_clicked, on_survival_clicked):
        self.on_play_clicked = on_play_clicked
        self.on_survival_clicked = on_survival_clicked

        self.title_font = pygame.font.Font('res/fonts/buster.ttf', 50)
        self.button_font = pygame.font.Font('res/fonts/buster.ttf', 25)
        self.button_font_hover = pygame.font.Font('res/fonts/buster.ttf', 30)

        self.play_button = Button(constants.DISPLAY_WIDTH * 0.5,
                                  constants.DISPLAY_HEIGHT * 0.4,
                                  225, 50,
                                  constants.GREEN,
                                  self.button_font, self.button_font_hover,
                                  "START GAME", self.on_play_clicked)
        self.survival_button = Button(constants.DISPLAY_WIDTH * 0.5,
                                      constants.DISPLAY_HEIGHT * 0.5,
                                      250, 50,
                                      constants.GREEN,
                                      self.button_font, self.button_font_hover,
                                      "SURVIVAL MODE", self.on_survival_clicked)

    def update(self, events, elapsed_time):
        self.play_button.update(events, pygame.mouse.get_pos())
        self.survival_button.update(events, pygame.mouse.get_pos())

    def render(self, game_display):
        self.show_text('Turbo Squares 2.0', constants.RED, constants.DISPLAY_WIDTH * 0.5,
                       constants.DISPLAY_HEIGHT * 0.15, self.title_font, game_display)

        self.play_button.render(game_display)
        self.survival_button.render(game_display)


class SurvivalGameScreen(Screen):

    def __init__(self, on_death):
        self.score_font = pygame.font.Font('res/fonts/arcade.ttf', 50)

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

        # Keeps track of the last time the score was incremented
        self.time_since_score = 0

    def update(self, events, elapsed_time):
        self.time_since_spawn += elapsed_time
        self.time_since_score += elapsed_time

        if self.time_since_spawn >= 500:
            self.spawn_bad_square()
            self.time_since_spawn = 0

        if self.time_since_score >= 1000:
            self.score += 1
            self.time_since_score = 0

        self.good_square.update(events, elapsed_time)
        for square in self.bad_squares:
            square.update(events, elapsed_time)

        collided_squares = pygame.sprite.spritecollide(self.good_square, self.bad_squares, False)
        if len(collided_squares) > 0:
            self.on_death()

    def render(self, game_display):
        self.good_square.render(game_display)
        for bad_square in self.bad_squares:
            if bad_square.active:
                bad_square.render(game_display)

        self.show_text(str(self.score), constants.BLUE,
                       constants.DISPLAY_WIDTH * 0.1, constants.DISPLAY_HEIGHT * 0.1,
                       self.score_font, game_display)

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


class LevelsGameScreen(Screen):

    def __init__(self, on_death):
        self.level_font = pygame.font.Font('res/fonts/arcade.ttf', 50)
        self.on_death = on_death
        self.level_screen = Level1(on_death, self.next_level)
        self.level_number = 1

    def update(self, events, elapsed_time):
        self.level_screen.update(events, elapsed_time)

    def render(self, game_display):
        self.level_screen.render(game_display)
        self.show_text(str(self.level_number), constants.BLUE,
                       constants.DISPLAY_WIDTH * 0.1, constants.DISPLAY_HEIGHT * 0.1,
                       self.level_font, game_display)

    def next_level(self):
        if self.level_number == 1:
            self.level_number = 2
            self.level_screen = Level2(self.on_death, self.next_level)
        else:
            self.on_death()

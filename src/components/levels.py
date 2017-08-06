import pygame
from .. data import constants
from squares import GoodSquare, BadSquare


class Level1(object):
    def __init__(self, on_death, on_complete):
        self.on_death = on_death
        self.on_complete = on_complete
        self.bad_squares = pygame.sprite.Group()

        # Spawn the good square
        self.good_square = GoodSquare(0,
                                      constants.DISPLAY_HEIGHT / 2,
                                      constants.GOOD_SQUARE_SPEED, 0,
                                      allow_off_screen=True)

        # Spawn the bad squares
        for i in range(0, 6):
            bad_square = BadSquare()
            bad_square.position_in_x_slot(i * 2 + 2)
            bad_square.position_in_y_slot(-1)
            bad_square.x_speed = 0
            bad_square.y_speed = -10
            self.bad_squares.add(bad_square)

    def update(self, events, elapsed_time):
        self.good_square.update(events, elapsed_time)
        for bad_square in self.bad_squares:
            bad_square.update(events, elapsed_time)
            reached_top = (bad_square.get_y() <= 0 and bad_square.y_speed < 0)
            reached_bottom = (bad_square.get_y() >=
                              constants.DISPLAY_HEIGHT-bad_square.get_height()
                              and bad_square.y_speed > 0)
            if reached_top or reached_bottom:
                bad_square.y_speed *= -1
                bad_square.active = True

        # If the player hit a red square, end the game
        collided_squares = pygame.sprite.spritecollide(self.good_square, self.bad_squares, False)
        if len(collided_squares) > 0:
            self.on_death()

        # If the player crossed the right side of the screen, they beat the level
        if self.good_square.get_x() >= constants.DISPLAY_WIDTH:
            self.on_complete()

    def render(self, game_display):
        self.good_square.render(game_display)
        for bad_square in self.bad_squares:
            if bad_square.active:
                bad_square.render(game_display)


class Level2(object):
    def __init__(self, on_death, on_complete):
        pass

    def update(self, events, elapsed_time):
        pass

    def render(self, game_display):
        pass

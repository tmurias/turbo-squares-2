import pygame
from .. data import constants


class GoodSquare(pygame.sprite.Sprite):
    def __init__(self, x, y, x_speed, y_speed):
        super(GoodSquare, self).__init__()
        self.image = pygame.image.load('res/images/good_square.png').convert_alpha()
        self.image.set_colorkey(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def update(self, events, elapsed_time):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_speed = -constants.GOOD_SQUARE_SPEED
                    self.y_speed = 0
                elif event.key == pygame.K_RIGHT:
                    self.x_speed = constants.GOOD_SQUARE_SPEED
                    self.y_speed = 0
                elif event.key == pygame.K_UP:
                    self.x_speed = 0
                    self.y_speed = -constants.GOOD_SQUARE_SPEED
                elif event.key == pygame.K_DOWN:
                    self.x_speed = 0
                    self.y_speed = constants.GOOD_SQUARE_SPEED

        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Prevent square from going out of bounds
        width = self.rect.size[0]
        height = self.rect.size[1]
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > constants.DISPLAY_WIDTH - width:
            self.rect.x = constants.DISPLAY_WIDTH - width
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > constants.DISPLAY_HEIGHT - height:
            self.rect.y = constants.DISPLAY_HEIGHT - height

    def render(self, game_display):
        game_display.blit(self.image, self.rect)


class BadSquare(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0, x_speed=0, y_speed=0, active=False):
        super(BadSquare, self).__init__()
        self.image = pygame.image.load('res/images/bad_square.png').convert_alpha()
        self.image.set_colorkey(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.active = active

    def update(self, events, elapsed_time):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Square is no longer active if it is off the screen
        width = self.rect.size[0]
        height = self.rect.size[1]
        off_left = (self.rect.x < -width) and (self.x_speed < 0)
        off_right = (self.rect.x > constants.DISPLAY_WIDTH) and (self.x_speed > 0)
        off_top = (self.rect.y < -height) and (self.y_speed < 0)
        off_bottom = (self.rect.y > constants.DISPLAY_HEIGHT) and (self.y_speed > 0)
        if off_left or off_right or off_top or off_bottom:
            self.active = False

    def render(self, game_display):
        game_display.blit(self.image, self.rect)

    def position_in_x_slot(self, x_slot):
        self.rect.x = x_slot * self.rect.size[0]

    def position_in_y_slot(self, y_slot):
        self.rect.y = y_slot * self.rect.size[1]

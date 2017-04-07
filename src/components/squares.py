import pygame
from .. data import constants


class GoodSquare(pygame.sprite.Sprite):
    def __init__(self, x, y, x_speed, y_speed):
        super(GoodSquare, self).__init__()
        self.image = pygame.image.load('res/images/good_square.png').convert()
        self.image.set_colorkey(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_speed = x_speed

    def update(self, events, elapsed_time):
        pass


class BadSquare(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(BadSquare, self).__init__()
        self.image = pygame.image.load('res/images/bad_square.png').convert()
        self.image.set_colorkey(constants.WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, events, elapsed_time):
        pass

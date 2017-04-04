import pygame


class Button(object):

    def __init__(self, x, y, width, height, text_colour, text_font, hover_text_font,
                 text, onclick):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_colour = text_colour
        self.text_font = text_font
        self.hover_text_font = hover_text_font
        self.text = text
        self.onclick = onclick

        self.current_text_font = text_font

    def update(self, events, mouse_pos):
        in_x_bounds = (self.x - self.width/2 < mouse_pos[0] < self.x + self.width/2)
        in_y_bounds = (self.y - self.height/2 < mouse_pos[1] < self.y + self.height/2)
        if in_x_bounds and in_y_bounds:
            self.current_text_font = self.hover_text_font
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.onclick()
                    break
        else:
            self.current_text_font = self.text_font

    def render(self, game_display):
        text_surface = self.current_text_font.render(self.text, True, self.text_colour)
        text_rect = text_surface.get_rect()
        text_rect.center = self.x, self.y
        game_display.blit(text_surface, text_rect)

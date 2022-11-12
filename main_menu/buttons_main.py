import pygame
from scales import Scale


class Button:
    def __init__(self, screen):
        self.screen = screen
        scale_position = Scale(screen)
        self.scale_position = scale_position.big()

    def main_menu(self, img_path, position, scale):
        button = pygame.image.load(img_path).convert_alpha()
        button = pygame.transform.scale(button, (
        int(button.get_width() * scale[0]), int(button.get_height() * scale[1])))
        rect = button.get_rect()
        position = (position[0]*self.scale_position[0], self.screen.get_height() - button.get_height() - (position[1]*self.scale_position[1]))
        rect.topleft = position
        return self.screen.blit(button, (rect.x, rect.y))

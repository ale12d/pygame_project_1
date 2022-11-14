import pygame
from scales import Scale
from main_menu.views.home import MainView


class Backgrounds:
    def __init__(self, screen, color, img_path):
        self.screen = screen
        self.color = color
        self.img_path = img_path

        scale = Scale(self.screen)
        self.rx, self.ry = scale.big()

        self.main_menu = MainView(self.screen)

    def show(self):
        self.screen.fill(self.color)
        self.main_menu.create_main_buttons()
        background = pygame.image.load(self.img_path).convert_alpha()
        background = pygame.transform.scale(background, (int(background.get_width() * self.rx), int(background.get_height() * self.ry)))
        self.screen.blit(background, (0, 0))
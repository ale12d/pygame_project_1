import pygame
from scales import Scale
from main_menu.views import MainView


class Backgrounds:
    def __init__(self, screen):
        self.screen = screen

        scale = Scale(self.screen)
        self.rx, self.ry = scale.big()

        self.main_menu = MainView(self.screen)

    def main_background(self):
        self.screen.fill((0, 0, 0))

    def play_background(self):
        self.screen.fill((92, 128, 55))
        self.main_menu.create_main_buttons()
        play_bar = pygame.image.load('medias/play_bar.png').convert_alpha()
        play_bar = pygame.transform.scale(play_bar, (int(play_bar.get_width() * self.rx), int(play_bar.get_height() * self.ry)))
        self.screen.blit(play_bar, (0, 0))

    def load_background(self):
        self.screen.fill((48, 96, 130))
        self.main_menu.create_main_buttons()
        play_bar = pygame.image.load('medias/load_bar.png').convert_alpha()
        play_bar = pygame.transform.scale(play_bar, (int(play_bar.get_width() * self.rx), int(play_bar.get_height() * self.ry)))
        self.screen.blit(play_bar, (0, 0))

    def settings_background(self):
        self.screen.fill((244, 194, 61))
        self.main_menu.create_main_buttons()
        play_bar = pygame.image.load('medias/settings_bar.png').convert_alpha()
        play_bar = pygame.transform.scale(play_bar, (int(play_bar.get_width() * self.rx), int(play_bar.get_height() * self.ry)))
        self.screen.blit(play_bar, (0, 0))
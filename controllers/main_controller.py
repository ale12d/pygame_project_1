import pygame
from sys import exit
from controllers.main_menu import MainMenuController

FRAMERATE = 60


class ApplicationController:

    def __init__(self):
        self.app_name = 'app'
        self.in_settings = False
        self.in_play = False
        self.in_load = False

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption(self.app_name)

        while True:
            for self.event in pygame.event.get():
                ApplicationController.quit(self, self.event)

            clock = Clock()
            clock.set_framerate(FRAMERATE)

            main_menu = MainMenuController(self.event, self.in_settings, self.in_play, self.in_load)
            self.in_settings, self.in_play, self.in_load = main_menu.setup_view(screen)

            pygame.display.update()

    def quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


class Clock:

    def __init__(self):
        self.clock = pygame.time.Clock()

    def set_framerate(self, framerate):
        self.clock.tick(framerate)

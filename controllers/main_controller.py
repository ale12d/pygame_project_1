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
        self.fullscreen = True
        self.sound_effect = True

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(self.app_name)

        while True:
            for self.event in pygame.event.get():
                ApplicationController.quit(self, self.event)
                main_menu = MainMenuController(self.event, self.in_settings, self.in_play, self.in_load,
                                               self.fullscreen, self.sound_effect)
                self.in_settings, self.in_play, self.in_load, self.fullscreen, self.sound_effect = main_menu.setup_view(
                    screen)

            clock = Clock()
            clock.set_framerate(FRAMERATE)

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

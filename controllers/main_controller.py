import pygame
from sys import exit
from controllers.main_menu import MainMenuController

FRAMERATE = 60


class ApplicationController:

    def __init__(self):
        self.app_name = 'app'
        self.click = False

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption(self.app_name)

        while True:
            for event in pygame.event.get():
                ApplicationController.quit(self, event)
                ApplicationController.click_check(self, event)

            clock = Clock()
            clock.set_framerate(FRAMERATE)

            main_menu = MainMenuController(self.click)
            main_menu.setup_view(screen)

            pygame.display.update()

    def quit(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    def click_check(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.click = True


class Clock:

    def __init__(self):
        self.clock = pygame.time.Clock()

    def set_framerate(self, framerate):
        self.clock.tick(framerate)

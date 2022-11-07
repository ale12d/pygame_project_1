import pygame
from main_menu.controllers import MainMenu
from cadence import Clock

FRAMERATE = 60


class Menu:
    def __init__(self, screen):
        self.event = None
        self.screen = screen

    def set(self):
        while True:
            for self.event in pygame.event.get():

                # show main buttons / .set call all menu views and controllers
                main_menu = MainMenu(self.screen, self.event)
                main_menu.set()

                # Close game if cross clicked or alt F4
                if self.event.type == pygame.QUIT:
                    quit()

            # start clock and set framerate
            clock = Clock()
            clock.set_framerate(FRAMERATE)

            pygame.display.update()

import pygame
from controllers import MainMenu


class Menu:
    def __init__(self, screen):
        self.screen = screen

    def set(self):
        while True:
            for self.event in pygame.event.get():

                # show main buttons / .set call all menu views and controllers
                main_menu = MainMenu()
                main_menu.set()

                # Close game if cross clicked or alt F4
                if self.event.type == pygame.QUIT:
                    quit()

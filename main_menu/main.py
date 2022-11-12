import pygame
from main_menu.controllers import MainMenu, PlayMenu, LoadMenu, SettingsMenu
from cadence import Clock

FRAMERATE = 60


class Menu:
    def __init__(self, screen):
        self.event = None
        self.screen = screen
        self.actual_menu = "main"

    def set(self):
        while True:
            for self.event in pygame.event.get():

                # show main buttons / .set call all menu views and controllers
                main_menu = MainMenu(self.screen, self.event, self.actual_menu)
                self.actual_menu = main_menu.set()

                if self.actual_menu == "play":
                    play_menu = PlayMenu(self.screen, self.event, self.actual_menu)
                    self.actual_menu = play_menu.set()
                elif self.actual_menu == "load":
                    load_menu = LoadMenu(self.screen, self.event, self.actual_menu)
                    self.actual_menu = load_menu.set()
                elif self.actual_menu == "settings":
                    settings_menu = SettingsMenu(self.screen, self.event, self.actual_menu)
                    self.actual_menu = settings_menu.set()

                # Close game if cross clicked or alt F4
                if self.event.type == pygame.QUIT:
                    quit()

            # start clock and set framerate
            clock = Clock()
            clock.set_framerate(FRAMERATE)

            pygame.display.update()

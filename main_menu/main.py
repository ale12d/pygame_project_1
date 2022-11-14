import pygame
from main_menu.controllers.home import MainController
from main_menu.controllers.play import PlayController
from main_menu.controllers.load import LoadController
from main_menu.controllers.settings import SettingsController
from sounds.sound import SoundGlobal
from cadence import Clock

FRAMERATE = 60


class Menu:
    def __init__(self, screen):
        self.event = None
        self.screen = screen
        self.actual_menu = "main"
        self.fullscreen = False
        self.sound = True

    def set(self):
        while True:
            for self.event in pygame.event.get():
                sound_vol = SoundGlobal(self.sound)

                # show main buttons / .set call all menu views and controllers
                main_menu = MainController(self.screen, self.event, self.actual_menu, sound_vol)
                self.actual_menu = main_menu.set()

                if self.actual_menu == "play":
                    play_menu = PlayController(self.screen, self.event)
                    play_menu.set()
                elif self.actual_menu == "load":
                    load_menu = LoadController(self.screen, self.event)
                    load_menu.set()
                elif self.actual_menu == "settings":
                    settings_menu = SettingsController(self.screen, self.event, self.fullscreen, self.sound)
                    self.fullscreen, self.sound = settings_menu.set()

                # Close game if cross clicked or alt F4
                if self.event.type == pygame.QUIT:
                    quit()

            # start clock and set framerate
            clock = Clock()
            clock.set_framerate(FRAMERATE)

            pygame.display.update()

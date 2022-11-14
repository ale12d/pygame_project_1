from devices.mouse import Pointer
from sounds.sound import SoundGlobal
from main_menu.backgrounds import Backgrounds
from main_menu.views.home import MainView

from main_menu.controllers.play import PlayController
from main_menu.controllers.load import LoadController
from main_menu.controllers.settings import SettingsController

import pygame


class MainController:
    def __init__(self, screen, event, actual_menu):
        self.screen = screen
        self.event = event
        self.buttons = None
        self.actual_menu = actual_menu

    def set(self):
        buttons = self.call_views()
        self.button_event_check(buttons)
        return self.actual_menu

    def call_views(self):
        main_view = MainView(self.screen)

        return main_view.create_main_buttons()

    def button_event_check(self, buttons):
        pointer = Pointer(self.event)
        for button in buttons:
            mx, my = pygame.mouse.get_pos()
            if button.collidepoint((mx, my)):
                click = pointer.click_check()
                if click:
                    sound = SoundGlobal()
                    sound.click_sound()
                    self.has_clicked(button)

    def has_clicked(self, button):
        print(dir(button))
        print(button.collidelist)
        if button[0] == 66:
            self.actual_menu = "play"
            play_menu = PlayController(self.screen, self.event, self.actual_menu)
            play_menu.set()
        elif button[0] == 213:
            self.actual_menu = "load"
            load_menu = LoadController(self.screen, self.event, self.actual_menu)
            load_menu.set()
        elif button[0] == 366:
            self.actual_menu = "settings"
            settings_menu = SettingsController(self.screen, self.event, self.actual_menu)
            settings_menu.set()
        elif button[0] == 606:
            quit()
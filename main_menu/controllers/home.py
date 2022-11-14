from devices.mouse import Pointer
from main_menu.backgrounds import Backgrounds
from main_menu.views.home import MainView

from main_menu.controllers.play import PlayController
from main_menu.controllers.load import LoadController
from main_menu.controllers.settings import SettingsController

import pygame


class MainController:
    def __init__(self, screen, event, actual_menu, sound):
        self.screen = screen
        self.event = event
        self.buttons = None
        self.actual_menu = actual_menu
        self.sound = sound

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
            if button[0].collidepoint((mx, my)):
                click = pointer.click_check()
                if click:
                    self.has_clicked(button)

    def has_clicked(self, button):
        if button[1] == "play_button":
            if self.actual_menu != "play":
                self.sound.click_sound()

            self.actual_menu = "play"

        elif button[1] == "load_button":
            if self.actual_menu != "load":
                self.sound.click_sound()

            self.actual_menu = "load"

        elif button[1] == "settings_button":
            if self.actual_menu != "settings":
                self.sound.click_sound()

            self.actual_menu = "settings"

        elif button[1] == "exit_button":
            quit()
import pygame
from main_menu.views import MainView
from devices.mouse import Pointer
from sounds.sound import SoundGlobal
from main_menu.backgrounds import Backgrounds


class MainMenu:
    def __init__(self, screen, event):
        self.screen = screen
        self.event = event
        self.buttons = None

    def set(self):
        self.buttons = self.call_views()
        self.button_event_check(self.buttons)

    def call_views(self):
        main_view = MainView(self.screen)

        return main_view.set()

    def button_event_check(self, buttons):
        pointer = Pointer(self.event)
        for button in buttons.values():
            mx, my = pygame.mouse.get_pos()
            if button.collidepoint((mx, my)):
                click = pointer.click_check()
                if click:
                    button = [k for k, v in buttons.items() if v == button]
                    self.has_clicked(button[0])

    def has_clicked(self, button):
        sound = SoundGlobal()
        sound.click_sound()
        if button == "play_button":
            play_menu = PlayMenu(self.screen)
            play_menu.set()
        if button == "load_button":
            load_menu = LoadMenu(self.screen)
            load_menu.set()
        if button == "settings_button":
            settings_menu = SettingsMenu(self.screen)
            settings_menu.set()
        if button == "exit_button":
            quit()


class PlayMenu:
    def __init__(self, screen):
        self.screen = screen

    def set(self):
        backgrounds = Backgrounds(self.screen)
        backgrounds.play_background()


class LoadMenu:
    def __init__(self, screen):
        self.screen = screen

    def set(self):
        backgrounds = Backgrounds(self.screen)
        backgrounds.load_background()


class SettingsMenu:
    def __init__(self, screen):
        self.screen = screen

    def set(self):
        backgrounds = Backgrounds(self.screen)
        backgrounds.settings_background()

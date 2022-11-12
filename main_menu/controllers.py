import pygame
from main_menu.views import MainView, PlayView, LoadView, SettingsView
from devices.mouse import Pointer
from sounds.sound import SoundGlobal
from main_menu.backgrounds import Backgrounds


class MainMenu:
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
        if button[0] == 66:
            self.actual_menu = "play"
            play_menu = PlayMenu(self.screen, self.event, self.actual_menu)
            play_menu.set()
        elif button[0] == 213:
            self.actual_menu = "load"
            load_menu = LoadMenu(self.screen, self.event, self.actual_menu)
            load_menu.set()
        elif button[0] == 366:
            self.actual_menu = "settings"
            settings_menu = SettingsMenu(self.screen, self.event, self.actual_menu)
            settings_menu.set()
        elif button[0] == 606:
            quit()


class PlayMenu:
    def __init__(self, screen, event, actual_menu):
        self.screen = screen
        self.event = event
        self.actual_menu = actual_menu

    def set(self):
        backgrounds = Backgrounds(self.screen, (92, 128, 55), 'medias/play_bar.png')
        backgrounds.show()
        return self.actual_menu


class LoadMenu:
    def __init__(self, screen, event, actual_menu):
        self.screen = screen
        self.event = event
        self.actual_menu = actual_menu

    def set(self):
        backgrounds = Backgrounds(self.screen, (48, 96, 130), 'medias/load_bar.png')
        backgrounds.show()
        return self.actual_menu


class SettingsMenu:
    def __init__(self, screen, event, actual_menu):
        self.screen = screen
        self.buttons = self.call_views()
        self.event = event
        self.actual_menu = actual_menu

    def set(self):
        backgrounds = Backgrounds(self.screen, (244, 194, 61), 'medias/settings_bar.png')
        backgrounds.show()

        buttons = self.call_views()
        self.button_event_check(buttons)
        return self.actual_menu

    def call_views(self):

        settings_views = SettingsView(self.screen)

        return settings_views.create_main_buttons()

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
        print("fdfsdqfdsqfdsqsq")


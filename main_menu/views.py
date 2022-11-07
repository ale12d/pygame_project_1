import pygame
from main_menu.buttons import Play, Load, Settings, Exit


class MainView:
    def __init__(self, screen):
        self.screen = screen

    def set(self):

        buttons = self.create_main_buttons()
        return buttons

    def create_main_buttons(self):
        play_button = Play(self.screen)
        load_button = Load(self.screen)
        settings_button = Settings(self.screen)
        exit_button = Exit(self.screen)

        buttons_list = [play_button, load_button, settings_button, exit_button]
        buttons_name = ["play_button", "load_button", "settings_button", "exit_button"]
        buttons_formated = {}
        for i in range(len(buttons_list)):

            img, position = buttons_list[i].set()
            buttons_formated[buttons_name[i]] = self.show(img, position)

        return buttons_formated

    def show(self, img, position):
        return self.screen.blit(img, position)


class PlayView:
    def __init__(self):
        pass

    def set(self):
        pass


class LoadView:
    def __init__(self):
        pass

    def set(self):
        pass


class SettingsView:
    def __init__(self):
        pass

    def set(self):
        pass


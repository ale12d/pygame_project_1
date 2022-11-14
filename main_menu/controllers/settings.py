from devices.mouse import Pointer
from sounds.sound import SoundGlobal
from main_menu.backgrounds import Backgrounds
from main_menu.views.settings import SettingsView
import pygame


class SettingsController:
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
        print(button)

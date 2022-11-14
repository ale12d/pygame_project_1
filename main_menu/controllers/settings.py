from devices.mouse import Pointer
from sounds.sound import SoundGlobal
from main_menu.backgrounds import Backgrounds
from main_menu.views.settings import SettingsView
import pygame


class SettingsController:
    def __init__(self, screen, event, fullscreen, sound):
        self.screen = screen
        self.event = event
        self.fullscreen = fullscreen
        self.sound = sound

    def set(self):
        backgrounds = Backgrounds(self.screen, (244, 194, 61), 'medias/settings_bar.png')
        backgrounds.show()

        buttons = self.call_views()
        self.button_event_check(buttons)

        return self.fullscreen, self.sound

    def call_views(self):
        settings_views = SettingsView(self.screen, self.fullscreen, self.sound)

        return settings_views.create_main_buttons()

    def button_event_check(self, buttons):
        pointer = Pointer(self.event)
        for button in buttons:
            mx, my = pygame.mouse.get_pos()
            if button[0].collidepoint((mx, my)):
                click = pointer.click_check()
                if click:
                    self.has_clicked(button)

    def has_clicked(self, button):
        if self.fullscreen:
            display = pygame.FULLSCREEN
        else:
            display = False

        if button[1] == "resolution1":
            pygame.display.set_mode((800, 600), display)
        if button[1] == "resolution2":
            pygame.display.set_mode((1024, 768), display)
        if button[1] == "resolution3":
            pygame.display.set_mode((1152, 648), display)
        if button[1] == "resolution4":
            pygame.display.set_mode((1366, 768), display)
        if button[1] == "resolution5":
            pygame.display.set_mode((1920, 1080), display)

        if button[1] == "fullscreen":
            if self.fullscreen:
                pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()))
                self.fullscreen = False
            else:
                pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()), pygame.FULLSCREEN)
                self.fullscreen = True

        if button[1] == "sound":
            if self.sound:
                self.sound = False
            else:
                self.sound = True

        sounds = SoundGlobal(self.sound)
        sounds.click_sound()


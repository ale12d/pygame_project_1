from views import MainMenu, SettingsMenu, PlayMenu, LoadMenu
from controllers.device import Mouse, Keyboard
import pygame


class MainMenuController:
    def __init__(self, event, in_settings, in_play, in_load):
        self.event = event
        self.in_settings = in_settings
        self.in_play = in_play
        self.in_load = in_load

    def setup_view(self, screen):
        mx, my = pygame.mouse.get_pos()
        mouse = Mouse(self.event)

        keyboard = Keyboard(self.event)
        keyboard.arrow_keys()

        main_menu = MainMenu()
        play_button, load_button, settings_button, exit_button = main_menu.display(screen)

        if play_button.collidepoint((mx, my)) or self.in_play is True:
            click = mouse.click_check()
            if click or self.in_play is True:
                MainMenuController.play(self, screen, mx, my, mouse)
        if load_button.collidepoint((mx, my)) or self.in_load is True:
            click = mouse.click_check()
            if click or self.in_load is True:
                MainMenuController.load(self, screen, mx, my, mouse)
        if settings_button.collidepoint((mx, my)) or self.in_settings is True:
            click = mouse.click_check()
            if click or self.in_settings is True:
                MainMenuController.settings(self, screen, mx, my, mouse)
        if exit_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.quit(self)

        return self.in_settings, self.in_play, self.in_load

    def play(self, screen, mx, my, mouse):
        self.in_play = True
        self.in_load = False
        self.in_settings = False

        play = PlayMenu()
        play.display(screen)

    def load(self, screen, mx, my, mouse):
        self.in_load = True
        self.in_play = False
        self.in_settings = False

        load = LoadMenu()
        load.display(screen)

    def settings(self, screen, mx, my, mouse):
        self.in_settings = True
        self.in_load = False
        self.in_play = False

        settings = SettingsMenu()
        fullscreen_img_button, resolution_1_button = settings.display(screen)

        if fullscreen_img_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        if resolution_1_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                pygame.display.set_mode((1152, 648))

    def quit(self):
        pygame.quit()
        exit()

from views import MainMenu, SettingsMenu
from controllers.device import Mouse, Keyboard
import pygame


class MainMenuController:
    def __init__(self, event):
        self.event = event

    def setup_view(self, screen):
        mx, my = pygame.mouse.get_pos()
        mouse = Mouse(self.event)

        keyboard = Keyboard(self.event)
        keyboard.arrow_keys()

        main_menu = MainMenu()
        play_button, load_button, settings_button, exit_button = main_menu.display(screen)

        if play_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.play(self)
        if load_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.load(self)
        if settings_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.settings(self, screen)
        if exit_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.quit(self)

    def play(self):
        pass

    def load(self):
        pass

    def settings(self, screen):
        settings = SettingsMenu()
        settings.display(screen)

    def quit(self):
        pygame.quit()
        exit()

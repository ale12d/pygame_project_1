from views import MainMenu, SettingsMenu
from controllers.device import Mouse, Keyboard
import pygame


class MainMenuController:
    def __init__(self, event, in_settings):
        self.event = event
        self.in_settings = in_settings

    def setup_view(self, screen):
        mx, my = pygame.mouse.get_pos()
        mouse = Mouse(self.event)

        keyboard = Keyboard(self.event)
        keyboard.arrow_keys()

        if self.in_settings is False:
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
                    MainMenuController.settings(self, screen, mx, my, mouse)
            if exit_button.collidepoint((mx, my)):
                click = mouse.click_check()
                if click:
                    MainMenuController.quit(self)

            return self.in_settings

        else:
            MainMenuController.settings(self, screen, mx, my, mouse)

    def play(self):
        pass

    def load(self):
        pass

    def settings(self, screen, mx, my, mouse):
        self.in_settings = True

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

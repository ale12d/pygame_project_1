from views import MainMenu
from controllers.device import Mouse
import pygame


class MainMenuController:
    def __init__(self, event):
        self.event = event

    def setup_view(self, screen):
        mx, my = pygame.mouse.get_pos()
        mouse = Mouse(self.event)

        main_menu = MainMenu()
        play_button, load_button, option_button, quit_button = main_menu.display(screen)

        if play_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.play(self)
        if load_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.load(self)
        if option_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.option(self)
        if quit_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.quit(self)

    def play(self):
        pass

    def load(self):
        pass

    def option(self):
        pass

    def quit(self):
        pygame.quit()
        exit()

from views import MainMenu
import pygame


class MainMenuController:
    def __init__(self, click):
        self.click = click

    def setup_view(self, screen):
        mx, my = pygame.mouse.get_pos()

        main_menu = MainMenu()
        play_button, load_button, option_button, quit_button = main_menu.display(screen)

        if play_button.collidepoint((mx, my)):
            if self.click:
                MainMenuController.play(self)
        if load_button.collidepoint((mx, my)):
            if self.click:
                MainMenuController.load(self)
        if option_button.collidepoint((mx, my)):
            if self.click:
                MainMenuController.option(self)
        if quit_button.collidepoint((mx, my)):
            if self.click:
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

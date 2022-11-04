from views import MainMenu, SettingsMenu, PlayMenu, LoadMenu
from controllers.device import Mouse, Keyboard
import pygame


class MainMenuController:
    def __init__(self, event, in_settings, in_play, in_load, fullscreen):
        self.event = event
        self.in_settings = in_settings
        self.in_play = in_play
        self.in_load = in_load
        self.fullscreen = fullscreen


    def setup_view(self, screen):

        self.in_settings, self.in_play, self.in_load, self.fullscreen = MainMenuController.menu_buttons(self, screen)

        return self.in_settings, self.in_play, self.in_load, self.fullscreen

    def play(self, screen, mx, my, mouse):
        self.in_play = True
        self.in_load = False
        self.in_settings = False

        play = PlayMenu()
        play.display(screen)

        main_menu = MainMenu()
        main_menu.display(screen)

    def load(self, screen, mx, my, mouse):
        self.in_load = True
        self.in_play = False
        self.in_settings = False

        load = LoadMenu()
        load.display(screen)

        main_menu = MainMenu()
        main_menu.display(screen)

    def settings(self, screen, mx, my, mouse):
        self.in_settings = True
        self.in_load = False
        self.in_play = False

        settings = SettingsMenu()
        fullscreen_img_button, resolution_1_button = settings.display(screen)

        if fullscreen_img_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                if not self.fullscreen:
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    self.fullscreen = True
                else:
                    pygame.display.set_mode((1152, 648))
                    self.fullscreen = False

        if resolution_1_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                pygame.display.set_mode((1152, 648))

        main_menu = MainMenu()
        main_menu.display(screen)

    def quit(self):
        pygame.quit()
        exit()


    def menu_buttons(self, screen):
        mx, my = pygame.mouse.get_pos()
        mouse = Mouse(self.event)

        keyboard = Keyboard(self.event)
        keyboard.arrow_keys()

        sound = Sound()

        main_menu = MainMenu()
        play_button, load_button, settings_button, exit_button = main_menu.display(screen)

        if play_button.collidepoint((mx, my)) or self.in_play :
            click = mouse.click_check()
            if click and play_button.collidepoint((mx, my)) and not self.in_play:
                sound.click_sound()
            if click or self.in_play is True:
                MainMenuController.play(self, screen, mx, my, mouse)

        if load_button.collidepoint((mx, my)) or self.in_load :
            click = mouse.click_check()
            if click and load_button.collidepoint((mx, my)) and not self.in_load:
                sound.click_sound()
            if click or self.in_load is True:
                MainMenuController.load(self, screen, mx, my, mouse)

        if settings_button.collidepoint((mx, my)) or self.in_settings :
            click = mouse.click_check()
            if click and settings_button.collidepoint((mx, my)) and not self.in_settings:
                sound.click_sound()
            if click or self.in_settings is True:
                MainMenuController.settings(self, screen, mx, my, mouse)

        if exit_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                MainMenuController.quit(self)

        return self.in_settings, self.in_play, self.in_load, self.fullscreen

class Sound:
    def __int__(self):
        pass

    def click_sound(self):
        click_sound = pygame.mixer.Sound("sounds/click_sound.wav")
        pygame.mixer.Sound.play(click_sound)

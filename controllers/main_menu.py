from views import MainMenu, SettingsMenu, PlayMenu, LoadMenu
from controllers.device import Mouse, Keyboard
import pygame


class MainMenuController:
    def __init__(self, event, in_settings, in_play, in_load, fullscreen, sound_effect):
        self.event = event
        self.in_settings = in_settings
        self.in_play = in_play
        self.in_load = in_load
        self.fullscreen = fullscreen
        self.sound_effect = sound_effect


    def setup_view(self, screen):

        self.in_settings, self.in_play, self.in_load, self.fullscreen, self.sound_effect = MainMenuController.menu_buttons(self, screen)

        return self.in_settings, self.in_play, self.in_load, self.fullscreen, self.sound_effect

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

        settings = SettingsMenu(self.fullscreen, self.sound_effect)
        fullscreen_img_button, sound_img_button, resolution_1_button, resolution_2_button, resolution_3_button, resolution_4_button, resolution_5_button = settings.display(screen)

        if fullscreen_img_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                if not self.fullscreen:
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                    self.fullscreen = True
                else:
                    pygame.display.set_mode((800, 600))
                    self.fullscreen = False

        if sound_img_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                if not self.sound_effect:
                    print('sound on')
                    self.sound_effect = True
                else:
                    print('sound off')
                    self.sound_effect = False

        if resolution_1_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                pygame.display.set_mode((800, 600))
                self.fullscreen = False

        if resolution_2_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                pygame.display.set_mode((1024, 768))
                self.fullscreen = False

        if resolution_3_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                pygame.display.set_mode((1152, 648))
                self.fullscreen = False

        if resolution_4_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                pygame.display.set_mode((1366, 768))
                self.fullscreen = False

        if resolution_5_button.collidepoint((mx, my)):
            click = mouse.click_check()
            if click:
                pygame.display.set_mode((1920, 1080))
                self.fullscreen = False

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

        sound = Sound(self.sound_effect)

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

        return self.in_settings, self.in_play, self.in_load, self.fullscreen, self.sound_effect


class Sound:
    def __init__(self, sound_effect):
        self.sound_effect = sound_effect

    def click_sound(self):
        if self.sound_effect:
            click_sound = pygame.mixer.Sound("sounds/click_sound.wav")
            pygame.mixer.Sound.play(click_sound)

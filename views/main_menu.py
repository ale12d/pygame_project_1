import pygame


class MainMenu:
    def __init__(self):
        pass

    def display(self, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        play_img = pygame.image.load('medias/play_btn.png').convert_alpha()
        load_img = pygame.image.load('medias/load_btn.png').convert_alpha()
        settings_img = pygame.image.load('medias/settings_btn.png').convert_alpha()
        exit_img = pygame.image.load('medias/exit_btn.png').convert_alpha()

        rx = screen_width / 120
        ry = screen_height / 67

        play_img = pygame.transform.scale(play_img, (int(play_img.get_width() * rx), int(play_img.get_height() * ry)))
        load_img = pygame.transform.scale(load_img, (int(load_img.get_width() * rx), int(load_img.get_height() * ry)))
        settings_img = pygame.transform.scale(settings_img, (int(settings_img.get_width() * rx), int(settings_img.get_height() * ry)))
        exit_img = pygame.transform.scale(exit_img, (int(exit_img.get_width() * rx), int(exit_img.get_height() * ry)))
        button_y_position = screen_height - play_img.get_height() - (1*rx)

        play_button = MainMenu.button(self, screen, ((10*rx), button_y_position), play_img)
        load_button = MainMenu.button(self, screen, ((11*rx) + play_img.get_width(), button_y_position), load_img)
        settings_button = MainMenu.button(self, screen, ((12*rx) + play_img.get_width() + load_img.get_width(), button_y_position), settings_img)
        exit_button = MainMenu.button(self, screen, (110*rx - exit_img.get_width(), button_y_position), exit_img)

        return play_button, load_button, settings_button, exit_button

    def button(self, screen, position, img):
        width = img.get_width()
        height = img.get_height()
        img = pygame.transform.scale(img, (int(width), int(height)))
        rect = img.get_rect()
        rect.topleft = position
        return screen.blit(img, (rect.x, rect.y))


class PlayMenu:
    def __int__(self):
        pass

    def display(self, screen):
        screen.fill((92, 128, 55))
        screen_width = screen.get_width()
        rx = screen_width / 120
        play_bar = pygame.image.load('medias/play_bar.png').convert_alpha()
        play_bar = pygame.transform.scale(play_bar, (int(play_bar.get_width() * rx), int(play_bar.get_height() * rx)))
        screen.blit(play_bar, (0, 0))


class LoadMenu:
    def __init__(self):
        pass

    def display(self,screen):
        screen.fill((48, 96, 130))
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        rx = screen_width / 120
        ry = screen_height / 120
        load_bar = pygame.image.load('medias/load_bar.png').convert_alpha()
        load_bar = pygame.transform.scale(load_bar, (int(load_bar.get_width() * rx), int(load_bar.get_height() * rx)))
        screen.blit(load_bar, (0, 0))


class SettingsMenu:
    def __init__(self, fullscreen, sound_effect):
        self.fullscreen = fullscreen
        self.sound_effect = sound_effect

    def display(self, screen):
        screen.fill((244, 194, 61))
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        rx = screen_width / 120
        ry = screen_height / 67
        rx_resolution = screen_width / 200
        ry_resolution = screen_height / 112

        settings_bar = pygame.image.load('medias/settings_bar.png').convert_alpha()
        settings_bar = pygame.transform.scale(settings_bar, (int(settings_bar.get_width() * rx), int(settings_bar.get_height() * ry)))

        resolution_img = pygame.image.load('medias/resolution.png').convert_alpha()
        resolution_img = pygame.transform.scale(resolution_img, (int(resolution_img.get_width() * rx), int(resolution_img.get_height() * ry)))

        other_img = pygame.image.load('medias/other.png').convert_alpha()
        other_img = pygame.transform.scale(other_img, (int(other_img.get_width() * rx), int(other_img.get_height() * ry)))

        screen.blit(settings_bar, (0, 0))
        screen.blit(resolution_img, (2*rx, 10*ry))
        screen.blit(other_img, (73.2*rx, 10*ry))

        if self.fullscreen:
            fullscreen_img = pygame.image.load('medias/fullscreen_on_btn.png').convert_alpha()
        else:
            fullscreen_img = pygame.image.load('medias/fullscreen_btn.png').convert_alpha()

        if self.sound_effect:
            sound_effect_img = pygame.image.load('medias/sound_on_btn.png').convert_alpha()
        else:
            sound_effect_img = pygame.image.load('medias/sound_off_btn.png').convert_alpha()

        fullscreen_img = pygame.transform.scale(fullscreen_img, (int(fullscreen_img.get_width() * rx_resolution), int(fullscreen_img.get_height() * ry_resolution)))
        sound_effect_img = pygame.transform.scale(sound_effect_img, (int(sound_effect_img.get_width() * rx_resolution), int(sound_effect_img.get_height() * ry_resolution)))


        resolution_1_img = pygame.image.load('medias/800x600_btn.png').convert_alpha()
        resolution_1_img = pygame.transform.scale(resolution_1_img, (int(resolution_1_img.get_width() * rx_resolution), int(resolution_1_img.get_height() * ry_resolution)))

        resolution_2_img = pygame.image.load('medias/1024x768_btn.png').convert_alpha()
        resolution_2_img = pygame.transform.scale(resolution_2_img, (int(resolution_2_img.get_width() * rx_resolution), int(resolution_2_img.get_height() * ry_resolution)))

        resolution_3_img = pygame.image.load('medias/1152x648_btn.png').convert_alpha()
        resolution_3_img = pygame.transform.scale(resolution_3_img, (int(resolution_3_img.get_width() * rx_resolution), int(resolution_3_img.get_height() * ry_resolution)))

        resolution_4_img = pygame.image.load('medias/1366x768_btn.png').convert_alpha()
        resolution_4_img = pygame.transform.scale(resolution_4_img, (int(resolution_4_img.get_width() * rx_resolution), int(resolution_4_img.get_height() * ry_resolution)))

        resolution_5_img = pygame.image.load('medias/1920x1080_btn.png').convert_alpha()
        resolution_5_img = pygame.transform.scale(resolution_5_img, (int(resolution_5_img.get_width() * rx_resolution), int(resolution_5_img.get_height() * ry_resolution)))

        fullscreen_button = MainMenu.button(self, screen, (82*rx, 20*ry), fullscreen_img)
        sound_button = MainMenu.button(self, screen, (82*rx, 27*ry), sound_effect_img)

        resolution_1_button = MainMenu.button(self, screen, (12*rx, 20*ry), resolution_1_img)
        resolution_2_button = MainMenu.button(self, screen, (12*rx, 27*ry), resolution_2_img)
        resolution_3_button = MainMenu.button(self, screen, (12*rx, 34*ry), resolution_3_img)
        resolution_4_button = MainMenu.button(self, screen, (12*rx, 41*ry), resolution_4_img)
        resolution_5_button = MainMenu.button(self, screen, (12*rx, 48*ry), resolution_5_img)

        return fullscreen_button, sound_button, resolution_1_button, resolution_2_button, resolution_3_button, resolution_4_button, resolution_5_button

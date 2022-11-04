import pygame


class MainMenu:
    def __init__(self):
        pass

    def display(self, screen):
        screen_width = screen.get_width()
        screen_height = screen.get_height()


        screen.fill((48, 96, 130))
        play_img = pygame.image.load('medias/play_btn.png').convert_alpha()
        load_img = pygame.image.load('medias/load_btn.png').convert_alpha()
        settings_img = pygame.image.load('medias/settings_btn.png').convert_alpha()
        exit_img = pygame.image.load('medias/exit_btn.png').convert_alpha()

        rx = screen_width / 120
        play_img = pygame.transform.scale(play_img, (int(play_img.get_width() * rx), int(play_img.get_height() * rx)))
        load_img = pygame.transform.scale(load_img, (int(load_img.get_width() * rx), int(load_img.get_height() * rx)))
        settings_img = pygame.transform.scale(settings_img, (int(settings_img.get_width() * rx), int(settings_img.get_height() * rx)))
        exit_img = pygame.transform.scale(exit_img, (int(exit_img.get_width() * rx), int(exit_img.get_height() * rx)))
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
        screen_width = screen.get_width()
        rx = screen_width / 120
        play_bar = pygame.image.load('medias/play_bar.png').convert_alpha()
        play_bar = pygame.transform.scale(play_bar, (int(play_bar.get_width() * rx), int(play_bar.get_height() * rx)))
        screen.blit(play_bar, (0, 0))


class LoadMenu:
    def __init__(self):
        pass

    def display(self,screen):
        screen_width = screen.get_width()
        rx = screen_width / 120
        load_bar = pygame.image.load('medias/load_bar.png').convert_alpha()
        load_bar = pygame.transform.scale(load_bar, (int(load_bar.get_width() * rx), int(load_bar.get_height() * rx)))
        screen.blit(load_bar, (0, 0))


class SettingsMenu:
    def __init__(self):
        pass

    def display(self, screen):
        screen_width = screen.get_width()
        rx = screen_width / 120
        settings_bar = pygame.image.load('medias/settings_bar.png').convert_alpha()

        settings_bar = pygame.transform.scale(settings_bar, (int(settings_bar.get_width() * rx), int(settings_bar.get_height() * rx)))

        fullscreen_img = pygame.image.load('medias/settings_fullscreen_btn.png').convert_alpha()
        resolution_1_img = pygame.image.load('medias/settings_resolution_1_btn.png').convert_alpha()

        fullscreen_img_button = MainMenu.button(self, screen, (-40, 0), fullscreen_img)
        resolution_1_button = MainMenu.button(self, screen, (-40, 300), resolution_1_img)

        screen.blit(settings_bar, (0, 0))
        return fullscreen_img_button, resolution_1_button

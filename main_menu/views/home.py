from main_menu.buttons import Button
from scales import Scale


class MainView:
    def __init__(self, screen):
        self.screen = screen

    def create_main_buttons(self):
        button = Button(self.screen)
        scale = Scale(self.screen)
        rx, ry = scale.big()
        play_button = button.set('medias/play_btn.png', (10, 1), (rx, ry), "play_button")
        load_button = button.set('medias/load_btn.png', (32, 1), (rx, ry), "load_button")
        settings_button = button.set('medias/settings_btn.png', (55, 1), (rx, ry), "settings_button")
        exit_button = button.set('medias/exit_btn.png', (91, 1), (rx, ry), "exit_button")

        buttons_list = [play_button, load_button, settings_button, exit_button]

        return buttons_list
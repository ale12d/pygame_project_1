from main_menu.buttons_main import Button
from scales import Scale


class SettingsView:
    def __init__(self, screen):
        self.screen = screen

    def create_main_buttons(self):
        button = Button(self.screen)
        scale = Scale(self.screen)
        rx, ry = scale.medium()
        rxb, ryb = scale.big()

        button.main_menu('medias/resolution.png', (2, 48), (rxb, ryb))
        button.main_menu('medias/other.png', (73, 48), (rxb, ryb))

        resolution1 = button.main_menu('medias/800x600_btn.png', (12, 41), (rx, ry))
        resolution2 = button.main_menu('medias/1024x768_btn.png', (12, 34), (rx, ry))
        resolution3 = button.main_menu('medias/1152x648_btn.png', (12, 27), (rx, ry))
        resolution4 = button.main_menu('medias/1366x768_btn.png', (12, 20), (rx, ry))
        resolution5 = button.main_menu('medias/1920x1080_btn.png', (12, 13), (rx, ry))

        fullscreen = button.main_menu('medias/fullscreen_btn.png', (82, 41), (rx, ry))
        sound = button.main_menu('medias/sound_on_btn.png', (82, 34), (rx, ry))

        buttons_list = [resolution1, resolution2, resolution3, resolution4, resolution5, fullscreen, sound]

        return buttons_list

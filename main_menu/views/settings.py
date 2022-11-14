from main_menu.buttons import Button
from scales import Scale


class SettingsView:
    def __init__(self, screen, fullscreen, sound):
        self.screen = screen
        self.fullscreen = fullscreen
        self.sound = sound

    def create_main_buttons(self):
        button = Button(self.screen)
        scale = Scale(self.screen)
        rx, ry = scale.medium()

        resolution1 = button.set('medias/800x600_btn.png', (12, 41), (rx, ry), "resolution1")
        resolution2 = button.set('medias/1024x768_btn.png', (12, 34), (rx, ry), "resolution2")
        resolution3 = button.set('medias/1152x648_btn.png', (12, 27), (rx, ry), "resolution3")
        resolution4 = button.set('medias/1366x768_btn.png', (12, 20), (rx, ry), "resolution4")
        resolution5 = button.set('medias/1920x1080_btn.png', (12, 13), (rx, ry), "resolution5")

        if self.fullscreen:
            fullscreen = button.set('medias/fullscreen_on_btn.png', (82, 41), (rx, ry), "fullscreen")
        else:
            fullscreen = button.set('medias/fullscreen_btn.png', (82, 41), (rx, ry), "fullscreen")

        if self.sound:
            sound = button.set('medias/sound_on_btn.png', (82, 34), (rx, ry), "sound")
        else:
            sound = button.set('medias/sound_off_btn.png', (82, 34), (rx, ry), "sound")

        buttons_list = [resolution1, resolution2, resolution3, resolution4, resolution5, fullscreen, sound]

        return buttons_list

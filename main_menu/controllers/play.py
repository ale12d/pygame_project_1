from devices.mouse import Pointer
from sounds.sound import SoundGlobal
from main_menu.backgrounds import Backgrounds
from main_menu.views.play import PlayView

class PlayController:
    def __init__(self, screen, event, actual_menu):
        self.screen = screen
        self.event = event
        self.actual_menu = actual_menu

    def set(self):
        backgrounds = Backgrounds(self.screen, (92, 128, 55), 'medias/play_bar.png')
        backgrounds.show()
        return self.actual_menu
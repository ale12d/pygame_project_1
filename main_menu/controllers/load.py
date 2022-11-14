from devices.mouse import Pointer
from sounds.sound import SoundGlobal
from main_menu.backgrounds import Backgrounds
from main_menu.views.load import LoadView

class LoadController:
    def __init__(self, screen, event):
        self.screen = screen
        self.event = event

    def set(self):
        backgrounds = Backgrounds(self.screen, (48, 96, 130), 'medias/load_bar.png')
        backgrounds.show()
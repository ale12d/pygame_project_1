class Scale:
    def __init__(self, screen):
        self.screen = screen

    def big(self):
        rx = self.screen.get_width() / 120
        ry = self.screen.get_height() / 67

        return rx, ry

    def medium(self):
        rx = self.screen.get_width() / 200
        ry = self.screen.get_height() / 112

        return rx, ry

    def small(self):
        pass

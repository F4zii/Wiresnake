from kivy.app import App
from kivy.uix.widget import Widget


class WireGrid(Widget):
    pass


class WireApp(App):
    def build(self):
        return WireGrid()


if __name__ == '__main__':
    WireApp().run()

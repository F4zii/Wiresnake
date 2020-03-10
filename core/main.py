from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class WireGrid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)


class WireApp(App):
    def build(self):
        return WireGrid()


if __name__ == '__main__':
    WireApp().run()

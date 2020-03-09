from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class WireGrid(GridLayout):
    def __init__(self, **kwargs):
        super(WireGrid, self).__init__(**kwargs)

        self.inside = GridLayout(cols=2)

        self.cols = 1
        # self.rows = 2
        self.inside.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        self.inside.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False)
        self.inside.add_widget(self.password)
        self.submit = Button(text="Click me!")
        self.add_widget(self.inside)
        self.add_widget(self.submit)


class WireSnake(App):
    def build(self):
        return WireGrid()


if __name__ == "__main__":
    WireSnake().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window


class Clacwindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.size = (300, 500)




class ClacApp(App):
    def build(self):

        return Clacwindow()

if __name__=='__main__':
    ClacApp().run()
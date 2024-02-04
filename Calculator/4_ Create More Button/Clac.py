from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button




class Clacwindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.size = (300, 500)

        numb = [7,8,9,'+', 4,5,6, '-', 1,2,3, '*', '.', 0, '(', ')', '/']
        self.numbers = self.ids.numbers

        numc = ['C', 'CA']
        self.numbers = self.ids.numbers

        for num in numb:
            btn = Button(text = str(num), font_size= '30px', background_color= (1.0,0.0,0.0,1.0))
            self.numbers.add_widget(btn)

        for num in numc:
            btn = Button(text = str(num), font_size= '30px', background_color= (1.0,2.0,2.0,0.6))
            self.numbers.add_widget(btn)

        btn = Button(text = '=', font_size= '30px', background_color= (1.0,2.0,2.0,0.6))
        self.numbers.add_widget(btn)


class ClacApp(App):   
    def build(self):

        return Clacwindow()

if __name__=='__main__':
    ClacApp().run()
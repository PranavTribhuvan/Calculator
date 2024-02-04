from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar
from kivy.core.window import Window

class Clacwindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Window.size = (300, 500)

        numb = [7,8,9,'+',4,5,6,'-',1,2,3,'*', '.', 0,'(', ')', '/']
        self.numbers = self.ids.numbers
        
        numbC = ['C', 'CA']
        self.numbers = self.ids.numbers

        for num in numb:
            btn = Button(text=str(num),font_size='30px',background_color = (1.0,0.0,0.0,1.0))
            btn.bind(on_release=self.echo_numb)
            self.numbers.add_widget(btn)

        for num in numbC:
            btn = Button(text=str(num),font_size='30px',background_color = (1.0,2.0,3.0,0.6))
            btn.bind(on_release=self.echo_numb)
            self.numbers.add_widget(btn)


        eq = Button(text='=',font_size='30px',background_color = (1.0,2.0,3.0,0.6))
        eq.bind(on_release=self.evaluate_exp)
        self.ids.numbers.add_widget(eq)



    def echo_numb(self, instance):
        inputt = self.ids.inputt

        inputt.text += instance.text
        if instance.text == 'C' :
            inputt.text = ''      
        elif instance.text == 'CA' :
            inputt.text = inputt.text[:-3]         
        


    
    def evaluate_exp(self, text):
        inputt = self.ids.inputt 
        exp = inputt.text
        res = eval(exp)
        inputt.text =str(res)






class ClacApp(App):
    def build(self):

        return Clacwindow()

if __name__=='__main__':
    ClacApp().run()
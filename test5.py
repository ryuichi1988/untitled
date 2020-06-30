#-*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
def messageShow(message):
    if message == "stock":
        btn3=Button(text='Close me!')
        pop=Popup(content=btn3, title='Information Message !')
        pop.open()
        btn3.bind(on_press=pop.dismiss)

    else:
        btn3=Button(text='Exit')
        pop=Popup(content=btn3, title='Information Message !')
        pop.open()
        btn3.bind(on_press=pop.dismiss)

class LoginScreen(GridLayout):
    def __init__(self):
        super(LoginScreen, self).__init__()
        self.rows=3
        self.cols=2
        lbl1=Label(text="ID :",italic=True, bold=True)
        lbl2=Label(text="Password :",italic=True, bold=True)
        txt1=TextInput(multiline=False, font_size=50)
        txt2=TextInput(multiline=False, password=True)
        btn1=Button(text="Exit",italic=True)
        btn2=Button(text="OK",italic=True)
        btn2.bind(on_press=lambda *a:messageShow(txt1.text))
        self.add_widget(lbl1)
        self.add_widget(txt1)
        self.add_widget(lbl2)
        self.add_widget(txt2)
        self.add_widget(btn1)
        self.add_widget(btn2)

class SimpleKivy(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    SimpleKivy().run()
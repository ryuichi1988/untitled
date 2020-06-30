from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.textinput import TextInput
#from kivy.uix.listview import ListView
import os

Config.set('graphics','resizable',1)
Config.set('graphics','width','390')
Config.set('graphics','height','550')
class MyApp(App):
    def update_label(self):
        self.lbl.text=self.formula
    def add_number(self,instance):
        if(self.formula=='0'):
            self.formula=''
        self.formula += str(instance.text)
        self.update_label()
        #print(self.formula)
    def add_operation(self,instance):
        self.formula += str(instance.text)
        self.update_label()
    def calculate(self,instance):
        self.lbl.text=str(eval(self.lbl.text))
        self.formula='0'
    def play_music(self,intance):
        from kivy.core.audio import SoundLoader
        print(self.tx.text)
        self.tx.text=intance.text
        sound = SoundLoader.load(self.tx.text)
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        else:

            self.files = os.listdir(os.getcwd())
            self.bt=self.files
            self.list=self.files
            self.tx.text='Песня не найдена'
    def build(self):

        self.formula='0'
        bl=BoxLayout(orientation='vertical',padding=2,spacing=2)

        gl=GridLayout(cols=4, padding=2,spacing=2, size_hint=[1,.2])
        gl.add_widget(Button(text="7", on_press=self.add_number))
        gl.add_widget(Button(text="8", on_press=self.add_number))
        gl.add_widget(Button(text="9", on_press=self.add_number))
        gl.add_widget(Button(text="/", background_color=[1,0,0,1], background_normal="", on_press=self.add_operation))

        gl.add_widget(Button(text="4", on_press=self.add_number))
        gl.add_widget(Button(text="5", on_press=self.add_number))
        gl.add_widget(Button(text="6", on_press=self.add_number))
        gl.add_widget(Button(text="*", background_color=[1,0,0,1], background_normal="", on_press=self.add_operation))

        gl.add_widget(Button(text="1", on_press=self.add_number))
        gl.add_widget(Button(text="2", on_press=self.add_number))
        gl.add_widget(Button(text="3", on_press=self.add_number))
        gl.add_widget(Button(text="-", background_color=[1,0,0,1], background_normal="", on_press=self.add_operation))

        gl.add_widget(Button(text="0", on_press=self.add_number))
        gl.add_widget(Button(text=".", on_press=self.add_operation))
        gl.add_widget(Button(text="+", background_color=[1,0,0,1], background_normal="", on_press=self.add_operation))
        gl.add_widget(Button(text="=", background_color=[0.5, 0, 10, 3], background_normal="", on_press=self.calculate))

        self.lbl=Label(text="0", font_size=25, size_hint=[1,.2],halign='right',valign='center', text_size=[390-8,550*0.4-4])
        self.b2=Button(text="PLAY", on_press=self.play_music,size_hint=[1,.1])
        self.tx=TextInput(text='Введите',size_hint=[1, .05])
        self.bt = []
        self.files = os.listdir(os.getcwd())
        self.bt =self.files

        bl.add_widget(self.lbl)
        bl.add_widget(gl)
        bl.add_widget(self.tx,)
        for i in range(0, len(self.bt)):
            self.b2=(Button(text=self.bt[i],size_hint=[1, .02],on_press=self.play_music))
            bl.add_widget(self.b2)
        self.b2 = Button(text="PLAY", on_press=self.play_music, size_hint=[1, .07])
        bl.add_widget(self.b2)
        #bl.add_widget(self.list)
        return bl


if __name__ == '__main__':
    MyApp().run()
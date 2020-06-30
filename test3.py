from kivy.app import App
from kivy.uix.button import Button
import csv,os


n=0
class Test(App):

    def press(self,instance):
        global n
        print("Pressed")
        try:
            with open("test.csv", "a",newline="" ,encoding="utf_8_sig")as file1:
                wr = csv.writer(file1)
                list = [n,"我是中国人", 1223, 254512, "sasdfsad", "ddsa", "3m3,3"]
                wr.writerow(list)
                n+=1

        except PermissionError:
            print("PermissionError. Please close the file and try again.")
        file1.close()



    def build(self):
        butt=Button(text="Click")
        butt.bind(on_press=self.press) #dont use brackets while calling function
        return butt

Test().run()
print("程序结束")
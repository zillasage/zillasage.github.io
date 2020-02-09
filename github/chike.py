import kivy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty



class chike(Widget):
    date_ = ObjectProperty(None)
    total_returns_ = ObjectProperty(None)
    expenses_ = ObjectProperty(None)
    remainder_ = ObjectProperty(None)


    def btn(self):
        print(self.date_.text)
        print(self.total_returns_.text)
        print(self.expenses_.text)
        print(self.remainder_.text)
        date = self.date_.text
        date_file = open("CHIKE_TRANSPO_DATE.txt","+a")
        date_file.write(date + "\n")
        date_file.close()
        total_returns = self.total_returns_.text
        total_returns_file = open("CHIKE_TRANSPO_TOTAL_RETURNS.txt","+a")
        total_returns_file.write(total_returns + "\n")
        total_returns_file.close()
        expenses = self.expenses_.text
        expenses_file = open("CHIKE_TRANSPO_EXPENSES.txt","+a")
        expenses_file.write(expenses + "\n")
        expenses_file.close()
        remainder = self.remainder_.text
        remainder_file = open("CHIKE_TRANSPO_REMAINDER.txt","+a")
        remainder_file.write(remainder + "\n")
        remainder_file.close()

        print("DONE")

        self.date_.text = ""
        self.total_returns_.text = ""
        self.expenses_.text = ""
        self.remainder_.text = ""




class chike_runnr(App):
    def build(self):
        return chike()



if __name__ == "__main__":
    chike_runnr().run()
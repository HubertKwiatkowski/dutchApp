import os
import json

import quiz


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# jsonFilePath = os.path.join('.', 'dutchApp', 'data', 'vocabulary.json')
#   with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
#       jsonf.write(json.dumps(data, indent=4))

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.add_widget(Label(text='How many questions would you like to answer?', font_size=30))

        self.questionNumber = TextInput(multiline=False)

        self.add_widget(self.questionNumber)

        self.submit = Button(text="New test", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        number = self.questionNumber.text
        try
        self.questionNumber.text = ''



class DutchPracticeApp(App):
    def build(self):
        return MyGrid()


if __name__ == '__main__':
    DutchPracticeApp().run()


# TODO: import words

# TODO: interface

# TODO: basic test

# TODO: different difficulties

# TODO: favorite - words anwered incorrectly

# TODO: fiszki

# TODO: tips - drawings

# TODO: score?

# TODO: json file update
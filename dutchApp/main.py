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
        self.add_widget(Label(text='Dutch word'))
        self.add_widget(Label(text='Polish word'))
        self.add_widget(Label(text='Some other word'))
        self.add_widget(Label(text='More other words'))
        self.add_widget(Label(text='Different word'))


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
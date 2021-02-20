import os
import json


import quiz


import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


# jsonFilePath = os.path.join('.', 'dutchApp', 'data', 'vocabulary.json')
#   with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
#       jsonf.write(json.dumps(data, indent=4))

class MyGrid(Widget):
    pyNumber = ObjectProperty(None)

    def btn(self):
        print(self.pyNumber.text)
        self.pyNumber.text = ''


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
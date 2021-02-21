import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty


import quiz as q


class MainWindow(Screen):
    pyNumber = ObjectProperty(None)

    def btn(self):
        try:
            self.questions = int(self.pyNumber.text)
            self.pyNumber.text = ''
        except:
            self.pyNumber.text = 0
    

class QuestionWindow(Screen):
    pyPolish = ObjectProperty(None)
    pyDutch1 = ObjectProperty(None)
    pyDutch2 = ObjectProperty(None)
    pyDutch3 = ObjectProperty(None)
    pyDutch4 = ObjectProperty(None)


class AnswerWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


kv = Builder.load_file('my.kv')


class DutchApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    DutchApp().run()


# TODO: import words

# TODO: basic test

# TODO: different difficulties

# TODO: favorite - words answered incorrectly

# TODO: fiszki

# TODO: tips - drawings

# TODO: score?
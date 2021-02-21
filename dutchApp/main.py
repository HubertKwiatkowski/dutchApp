import random

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty


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

    Polish = StringProperty('POLISH WORD')
    Dutch1 = StringProperty('A')
    Dutch2 = StringProperty('B')
    Dutch3 = StringProperty('C')
    Dutch4 = StringProperty('D')

    def generateQuestion(self):

        quiz = q.singleQuestion()
        print(quiz)
        
        question = quiz[0]
        correctAnswer = quiz[1]
        wrongAnswers = quiz[2]
        answerOptions = [correctAnswer] + wrongAnswers
        random.shuffle(answerOptions)

        self.Polish = question
        self.Dutch1 = answerOptions[0]
        self.Dutch2 = answerOptions[1]
        self.Dutch3 = answerOptions[2]
        self.Dutch4 = answerOptions[3]

        return correctAnswer

    def checkAnswer(self):
        pass

    def reset(self):
        self.Polish = 'POLISH WORD'
        self.Dutch1 = 'A'
        self.Dutch2 = 'B'
        self.Dutch3 = 'C'
        self.Dutch4 = 'D'


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
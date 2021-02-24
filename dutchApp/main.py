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
        # TODO: add change of buttons colour to standard
        quiz = q.singleQuestion()
        print(quiz)
        
        self.question = quiz[0]
        self.correctAnswer = quiz[1]
        self.wrongAnswers = quiz[2]
        self.answerOptions = [self.correctAnswer] + self.wrongAnswers
        random.shuffle(self.answerOptions)

        self.Polish = self.question
        self.Dutch1 = self.answerOptions[0]
        self.Dutch2 = self.answerOptions[1]
        self.Dutch3 = self.answerOptions[2]
        self.Dutch4 = self.answerOptions[3]
        
    def checkAnswer(self, number):
        name = ('Dutch%s' % (number))
        value = self.answerOptions[number-1]
        answer = self.correctAnswer
        if value == self.correctAnswer:
            print('GOOD')
            """"val1 = ''
            val2 = [1,0,0,1]
            name1 = (name+'.background_normal')
            name2 = (name+'.background_color')
            setattr(self, name1, val1)
            setattr(self, name2, val2)"""
            # TODO: add change of button colour to green
        else:
            print('WRONG')
            # TODO: add change of button colours to green/red

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



# TODO: different difficulties

# TODO: favorite - words answered incorrectly

# TODO: fiszki

# TODO: tips - drawings

# TODO: score?
import os
import csv
import random


csvFilePath = os.path.join('.', 'dutchApp', 'data', 'vocabulary.csv')
vocabulary = []

def openCsv():
    """Read csv file with all words."""
    with open(csvFilePath) as csvf:
        readCsv = csv.reader(csvf)
        csvRow = next(readCsv)
        for line in readCsv:
            vocabulary.append(line)


def createEasyQuiz():
    pass

def createNormalQuiz():
    """Create the quiz."""
    
    order = vocabulary.copy()
    print('\nHow many questions would you like to answer?')
    questions = input('_> ')

    random.shuffle(order)


    for questionNum in range(int(questions)):
        # Get right and wrong answers.
        wrongAnswers = []
        for word in range(len(order)):
            wrongAnswers.append(order[word][1])

        question = order[questionNum][0]
        correctAnswer = wrongAnswers.pop(questionNum)

        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        print(order[questionNum][0])
        print(answerOptions)

        print('\nChoose correct answer')
        answer = input('_> ')    
        if answer == correctAnswer:
            print('\nGood')
        else: print('\nWrong')


def createHardQuiz():
    pass


openCsv()
createNormalQuiz()
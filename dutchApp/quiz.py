import os
import csv
import random


csvFilePath = os.path.join('.', 'dutchApp', 'data', 'vocabulary.csv')
vocabulary = []

def openCsv():
    with open(csvFilePath) as csvf:
        kutum.clear()
        readCsv = csv.reader(csvf)
        csvRow = next(readCsv)
        for line in readCsv:
            vocabulary.append(line)

def createQuiz():
    pass


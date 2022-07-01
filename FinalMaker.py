import copy
from Backtracker import *
from genartor import *
from random import seed
from random import randint
from time import time


class Earaser:
    def __init__(self, FullPuzzle, Number):
        self.puzzle = FullPuzzle
        self.index = 0
        self.Enumb = Number
        self.counter = 0
        self.taken = []  # A list for elements that are earased
        self.uniqueness = True

    def indexDecoding(self, numb):
        a = -1
        number = numb
        while number > 9:
            number = number - 9
            a += 1
        return [a, number - 1]

    def GetUntakenIndex(self):
        while True:
            print("In loop 1")
            if self.index in self.taken:
                self.index = self.indexDecoding(RandomNumber(1, 81))
            else:
                self.taken.append(self.index)
                return

    def checkIfUnique(self):
        temp = copy.deepcopy(self.puzzle)
        self.uniqueness = sudoku(temp, self.counter)

    def Earase(self):
        self.index = self.indexDecoding(RandomNumber(1, 81))
        temp = self.puzzle
        self.GetUntakenIndex()
        for i in range(self.Enumb+1):
            self.GetUntakenIndex()
            a = temp[self.index[0]][self.index[1]]
            temp[self.index[0]][self.index[1]] = 0
            self.counter += 1
            self.checkIfUnique()
            while True:
                if self.uniqueness:
                    print("entered 1")
                    break

                else:
                    print("entered 2")
                    temp[self.index[0]][self.index[1]] = a
                    self.GetUntakenIndex()
                    a = temp[self.index[0]][self.index[1]]
                    temp[self.index[0]][self.index[1]] = 0
                    self.checkIfUnique()

    def starter(self):
        self.Earase()
        return self.puzzle


def RandomNumber(start, end):
    seed(time())
    return randint(start, end)


def start(puzzle, number):
    myP = Earaser(puzzle, number)
    a = myP.starter()
    return a


starter = []
for i in range(0, 9):
    starter.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
b = create(starter)
print("The awnser is : ")
print(b)
puzz = start(b, 49)
print("******************The Puzzle IS*********************")
print(puzz)

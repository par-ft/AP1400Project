import random
import copy
from tracemalloc import start
from solver import *
from random import seed
from random import randint
from time import time


class Maker:
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, Wboard):
        self.puzzle = Wboard  # pass a puzzle white board
        # choose the index for changing
        self.index = 0
        self.timecounter = time()
        self.untaken = list(range(1, 82))
        self.initialize()
        self.unsolvable = False

    def initialize(self):
        a = time()
        for i in range(1):
            print(f"try {i}")
            self.index = self.indexDecoding(RandomNumber(1, 81))
            self.GetUntakenIndex()
            self.GetANumber()

    def GetUntakenIndex(self):
        a = random.choice(self.untaken)
        self.index = self.indexDecoding(a)
        self.untaken.remove(a)

    def GetANumber(self):
        numb = RandomNumber(1, 9)
        print("Get a Number")
        while True:
            print("In loop 2")
            numb = RandomNumber(1, 9)
            if self.check_colum(numb) and self.check_row(numb) and self.check_box(numb):
                break
        self.puzzle[self.index[0]][self.index[1]] = numb

    def indexDecoding(self, numb):
        a = 0
        number = numb
        while number > 9:
            number = number - 9
            a += 1
        return [a, number - 1]

    def check_row(self, val):
        row = self.index[0]
        Row = self.puzzle[row]
        if val in Row:
            print("Row False")
            print(Row)
            print(val)
            return False
        else:
            return True

    def check_colum(self, val):
        col = self.index[1]
        Col = [[row[col] for row in self.puzzle]]
        if val in Col:
            print("Col False")
            return False
        else:
            return True

    def find_box_start(self, coordinate):
        return coordinate // 3 * 3

    def get_box_coordinates(self, row_number, column_number):
        return self.find_box_start(column_number), self.find_box_start(row_number)

    def get_box(self):
        start_y, start_x = self.get_box_coordinates(
            self.index[0], self.index[1])
        box = []
        for i in range(start_x, 3 + start_x):
            box.extend(self.puzzle[i][start_y:start_y + 3])
        return box

    def check_box(self, val):
        b = self.get_box()
        if val in b:
            print("Box False")
            return False
        else:
            return True

    def creater(self):
        temp = self.puzzle
        temp2 = copy.deepcopy(temp)

        return solve(temp2)

    def check_forsolve(self):
        print(self.puzzle)
        temp_puzzle = self.creater()
        # print(self.puzzle)
        tempList = temp_puzzle[0] + temp_puzzle[1]+temp_puzzle[2]+temp_puzzle[3] + \
            temp_puzzle[4]+temp_puzzle[5]+temp_puzzle[6] + \
            temp_puzzle[7]+temp_puzzle[8]
        if 0 in tempList:
            self.unsolvable = True
            print("unsolvable")
        else:
            print("solvable")
            self.unsolvable = False


def RandomNumber(start, end):
    seed(time())
    return randint(start, end)


def create(starter):
    board = Maker(starter)
    return board.creater()

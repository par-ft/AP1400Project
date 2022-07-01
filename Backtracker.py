from msilib.schema import Class

from solver import Cell


class SudokuSolver:
    def __init__(self, puzzle, count):
        self.puzzle = puzzle
        self.solve_puzzle = []
        self.box_size = 3
        self.counter = count
        self.uniqunes = True

    def find_possibilities(self, row_number, column_number):
        possibilities = set(range(1, 10))
        row = self.get_row(row_number)
        column = self.get_column(column_number)
        box = self.get_box(row_number, column_number)
        for item in row + column + box:
            if not isinstance(item, list) and item in possibilities:
                possibilities.remove(item)
        return possibilities

    def get_row(self, row_number):
        return self.puzzle[row_number]

    def get_column(self, column_number):
        return [row[column_number] for row in self.puzzle]

    def get_box(self, row_number, column_number):
        start_y = column_number // 3 * 3
        start_x = row_number // 3 * 3
        if start_x < 0:
            start_x = 0
        if start_y < 0:
            start_y = 0
        box = []
        for i in range(start_x, self.box_size + start_x):
            box.extend(self.puzzle[i][start_y:start_y+self.box_size])
        return box

    def find_spot(self):
        unsolved = True
        while unsolved:
            unsolved = False
            for row_number, row in enumerate(self.puzzle):
                for column_number, item in enumerate(row):
                    if item == 0:
                        if self.uniqunes:
                            unsolved = True
                            possibilities = self.find_possibilities(
                                row_number, column_number)
                            if self.counter == 1:
                                if len(possibilities) == 1:
                                    self.puzzle[row_number][column_number] = list(possibilities)[
                                        0]
                                else:
                                    self.uniqunes = False
                            else:
                                if len(possibilities) == 1:
                                    self.puzzle[row_number][column_number] = list(possibilities)[
                                        0]
                                    self.counter -= 1
                        else:
                            return self.puzzle
        return self.puzzle


def sudoku(puzzle, count):
    sudoku = SudokuSolver(puzzle, count)
    awnser = sudoku.find_spot()
    uniqueness = sudoku.uniqunes
    return uniqueness

import os
import PyQt5
import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QMessageBox
from FinalMaker import *
from genartor import *
import random
import copy

# اینجا باید اینو باز کنیم ببینیم طرف چی انتخاب کرده بعد ببندیم بعدیو باز  کنیم
Form = uic.loadUiType(os.path.join(os.getcwd(), "project.ui"))[0]

# اینا باید تو کلاس تعریف بشن ولی نمیدونم چجوری برا همین اینجا نوشتم


class IntroWindow(QMainWindow, Form):
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.setupUi(self)
        self.puzzle = 0
        self.hintcount = 0
        self.sul = 0
        self.untaken = list(range(1, 82))
        self.fails = 0  # faills in every try
        self.TotalFail = 0  # fails in one round
        self.index = 0
        self.numb = 0
        self.values = 0
        # Push button Clicked
        self.hint.clicked.connect(self.sayhint)
        self.quit.clicked.connect(lambda: app.quit())
        self.checkbutton.clicked.connect(self.CheckAwnser)
        self.clearbutton.clicked.connect(self.Clear)
        self.resetbutton.clicked.connect(self.Reset)
        self.buildbutton.clicked.connect(self.build)
        self.solvebutton.clicked.connect(self.Solve)
        self.hintLCD.display(self.hintcount)
        self.failLCD.display(self.TotalFail)
        # PushButton Colors
        self.setStyleSheet("Background-color : #22303C")
        self.label.setStyleSheet("color : white")
        self.label_2.setStyleSheet("color : white")
        self.buildbutton.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : #8899A6;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : #0f8b8e"
                                       "}")
        self.hint.setStyleSheet("QPushButton"
                                "{"
                                "background-color : #8899A6;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : #0f8b8e"
                                "}")
        self.quit.setStyleSheet("QPushButton"
                                "{"
                                "background-color : #8899A6;"
                                "}"
                                "QPushButton::pressed"
                                "{"
                                "background-color : #0f8b8e"
                                "}")
        self.checkbutton.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : #8899A6;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : #0f8b8e"
                                       "}")
        self.clearbutton.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : #8899A6;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : #0f8b8e"
                                       "}")
        self.resetbutton.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : #8899A6;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : #0f8b8e"
                                       "}")
        self.solvebutton.setStyleSheet("QPushButton"
                                       "{"
                                       "background-color : #8899A6;"
                                       "}"
                                       "QPushButton::pressed"
                                       "{"
                                       "background-color : #0f8b8e"
                                       "}")
        Palette = QtGui.QPalette()
        Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
        self.numberInput.setPalette(Palette)

    def Lock(self):
        for i in range(9):
            for j in range(9):
                getattr(self, "lineEdit_"+str(i) +
                        "_"+str(j)).setReadOnly(True)

    def unLock(self):
        for i in range(9):
            for j in range(9):
                getattr(self, "lineEdit_"+str(i) +
                        "_"+str(j)).setReadOnly(False)

    def Fill(self):
        Palette = QtGui.QPalette()
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] != 0:
                    self.index = [i, j]
                    self.untaken.remove(self.indexCoding())
                    getattr(self, "lineEdit_"+str(i)+"_" +
                            str(j)).setText(str(self.puzzle[i][j]))
                    getattr(self, "lineEdit_"+str(i)+"_"+str(j)
                            ).setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
                    Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setPalette(Palette)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setReadOnly(True)
                else:
                    getattr(self, "lineEdit_"+str(i)+"_" +
                            str(j)).setText('')
                    Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.white)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setPalette(Palette)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setReadOnly(False)

    def indexDecoding(self, numb):
        a = 0
        number = numb
        while number > 9:
            number = number - 9
            a += 1
        return [a, number - 1]

    def indexCoding(self):
        row = self.index[0]
        col = self.index[1]
        return (row*9) + col + 1

    def GetUntakenIndex(self):
        a = random.choice(self.untaken)
        self.index = self.indexDecoding(a)
        self.untaken.remove(a)

    def sayhint(self):
        Palette = QtGui.QPalette()
        if self.hintcount == 3:
            self.showMessageBox()
        else:
            self.GetUntakenIndex()
            i = self.index[0]
            j = self.index[1]
            # self.untaken.remove(self.indexCoding())
            getattr(self, "lineEdit_"+str(i)+"_" + str(j)
                    ).setText(str(self.sul[i][j]))
            getattr(self, "lineEdit_"+str(i)+"_"+str(j)
                    ).setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
            Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.green)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setPalette(Palette)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setReadOnly(True)
            self.hintcount += 1
            self.hintLCD.display(self.hintcount)

    def Clear(self):
        for i in self.untaken:
            [i, j] = self.indexDecoding(i)
            a = getattr(self, "lineEdit_"+str(i) + "_"+str(j)).clear()

    def Reset(self):
        self.TotalFail = 0
        self.hintcount = 0
        self.hintLCD.display(self.hintcount)
        self.failLCD.display(self.TotalFail)
        self.unLock()
        self.untaken = list(range(1, 82))
        starter = []
        for i in range(0, 9):
            starter.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        b = create(starter)
        print("Created")
        self.sul = b
        c = copy.deepcopy(b)
        self.puzzle = startMaker(c, self.numb)
        print("Started")
        self.Fill()

    def CheckAwnser(self):
        Palette = QtGui.QPalette()
        self.fails = 0
        for i in self.untaken:
            [i, j] = self.indexDecoding(i)
            a = getattr(self, "lineEdit_"+str(i) + "_"+str(j)).text()
            self.values = [i, j]
            if a == '':
                if self.TotalFail == 3:
                    self.showfailMessage()
                Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
                getattr(self, "lineEdit_"+str(i) +
                        "_"+str(j)).setPalette(Palette)
                self.fails += 1
            else:
                b = int(a)
                if self.checkwSul(i, j, b):
                    print(f"checked [ {i} , {j} ]")
                    Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.green)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setPalette(Palette)

                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setReadOnly(True)
                else:
                    if self.TotalFail == 3:
                        self.showfailMessage()
                    Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
                    getattr(self, "lineEdit_"+str(i) +
                            "_"+str(j)).setPalette(Palette)
                    self.fails += 1
        if self.fails > 0:
            self.TotalFail += 1
            self.failLCD.display(self.TotalFail)

    def Solve(self):
        Palette = QtGui.QPalette()
        for i in range(9):
            for j in range(9):
                getattr(self, "lineEdit_"+str(i)+"_" +
                        str(j)).setText(str(self.sul[i][j]))
                getattr(self, "lineEdit_"+str(i)+"_"+str(j)
                        ).setFont(QtGui.QFont("Times", weight=QtGui.QFont.Bold))
                Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.green)
                getattr(self, "lineEdit_"+str(i) +
                        "_"+str(j)).setPalette(Palette)
                getattr(self, "lineEdit_"+str(i) +
                        "_"+str(j)).setReadOnly(True)

    def changed(self):
        for i in self.untaken:
            [i, j] = self.indexDecoding(i)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).clear()
            self.values = [i, j]
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)
                    ).returnPressed.connect(getattr(self.textchange))

    def checkwSul(self, i, j, val):

        if val == self.sul[i][j]:
            return True
        else:
            return False

    def textchange(self):

        Palette = QtGui.QPalette()
        # اینجا باید یه مشت ایف بزنی چک کنه ببینه درسته یا نه
        [i, j] = self.values
        a = getattr(self, "lineEdit_"+str(i) + "_"+str(j)).displayText()
        print(f"[ {i} , {j}]")
        getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setText("0")
        print(str(a))
        self.puzzle[i][j] = a
        if self.check_row(a) and self.check_colum(a) and self.check_box(a):
            Palette.setColor(QtGui.QPalette.Text, QtCore.Qt.red)
            getattr(self, "lineEdit_"+str(i) + "_"+str(j)).setPalette(Palette)

    def check_row(self, val):
        row = self.values[0]
        Row = self.puzzle[row]
        if val in Row:
            return False
        else:
            return True

    def check_colum(self, val):
        col = self.values[1]
        Col = [[row[col] for row in self.puzzle]]
        if val in Col:
            return False
        else:
            return True

    def find_box_start(self, coordinate):
        return coordinate // 3 * 3

    def get_box_coordinates(self, row_number, column_number):
        return self.find_box_start(column_number), self.find_box_start(row_number)

    def get_box(self):
        start_y, start_x = self.get_box_coordinates(
            self.values[0], self.values[1])
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

    def showMessageBox(self):
        QMessageBox.about(self, "No more Hints!", "You have used Your 3 hints")

    def showfailMessage(self):
        self.Lock()
        QMessageBox.about(
            self, "Sorry!", "Unfortunally you used your 3 chances")

    def build(self):
        self.TotalFail = 0
        self.hintcount = 0
        self.hintLCD.display(self.hintcount)
        self.failLCD.display(self.TotalFail)
        self.untaken = list(range(1, 82))
        starter = []
        for i in range(0, 9):
            starter.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        b = create(starter)
        print("Created")
        self.sul = b
        c = copy.deepcopy(b)
        self.numb = int(self.numberInput.text())
        self.puzzle = startMaker(c, self.numb - 1)
        print("Started")
        self.Fill()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("breeze")
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_())

import os
import PyQt5
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np


Form = uic.loadUiType(os.path.join(os.getcwd(), "Form.ui"))[0]

class IntroWindow(QMainWindow, Form):
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.setupUi(self)

        self.hint.clicked.connect(self.sayhint)
        self.quit.clicked.connect(self.quit)

    def sayhint(self):
       #hint code here
       # self.text_xy.setText(f"{}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_())

    
        
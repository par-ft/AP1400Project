import os
from time import time
import PyQt5
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np

 #برا صفحه اول و اخرش ببندیمش
#اینجا باید اینو باز کنیم ببینیم طرف چی انتخاب کرده بعد ببندیم بعدیو باز  کنیم
Form = uic.loadUiType(os.path.join(os.getcwd(), "proj.main.ui"))[0]
self.pushButton_biginner.connect()
self.pushButton_medium.connect()
self.pushButton_hard.connect(asghar)
 
def asghar(self):
    #تابعو تعریف میکنیم و تهش صفحه بعدیو باز میکنیم 
     Form = uic.loadUiType(os.path.join(os.getcwd(), "proj.ui"))[0]                
    


# اینا باید تو کلاس تعریف بشن ولی نمیدونم چجوری برا همین اینجا نوشتم

Form = uic.loadUiType(os.path.join(os.getcwd(), "proj.ui"))[0]

class IntroWindow(QMainWindow, Form):
    def __init__(self):
        super(IntroWindow, self).__init__()
        self.setupUi(self)

        self.hint.clicked.connect(self.sayhint)
        self.quit.clicked.connect(lambda: app.quit())
        self.text_time.setText(f"{time_ns()/1000000}ms")
        #   به جای این که خیلی اشغاله میتونیم از ال سی دی استفاده کنیم به نظرت هرچی بهتره
        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QLCDNumber.html 
        
        for  i in range (81):
            self.text_xy.setText()
            #تو کدت اونجایی که خونه ها تعریف میشن چی باشن اینو ست تکست کن کن
        self.text_xy.textChanged.connect(self.textchange)
        self.progressBar.setRange (maximum,minimum)
        self.progressBar.valueChanged()
        #برای اینکه نشون بده چند درصدش کامل شده اینجا درصد میدی نشون میده




    def sayhint(self):
       #hint code here
       # self.text_xy.setText(f"{}")
        pass
    def textchange(self):
        #اینجا باید یه مشت ایف بزنی چک کنه ببینه درسته یا نه
        pass
    #کد رو نوشتی passهارو بردار 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    w = IntroWindow()
    w.show()
    sys.exit(app.exec_())

    
        
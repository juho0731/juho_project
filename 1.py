import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import uic

form_class = uic.loadUiType('test.ui')[0]

class WindowClass(QMainWindow, QWidget, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.a = 0
        self.change.clicked.connect(self.change_func)

    def change_func(self):
        if self.a == 0:
            self.mainlabel.setText("before")
            self.a += 1
        else:
            self.mainlabel.setText("after")
            self.a -= 1
        self.mainlabel.setFont(QtGui.QFont("Agency", 36))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowClass()
    window.show()
    app.exec_()
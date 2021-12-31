#!/bin/python3
import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 150, 300, 450)
        self.setWindowTitle("This")
        self.Ui()

    def Ui(self):
        self.text1 = QLabel("Hello PYthon", self)
        enterButton = QPushButton("Enter", self)
        exitButton = QPushButton("Exit", self)
        self.text1.move(100, 50)
        enterButton.move(100, 80)
        exitButton.move(100, 120)
        enterButton.clicked.connect(self.enterfunc)
        exitButton.clicked.connect(self.exitfunc)

        self.show()

    def enterfunc(self):
        self.text1.setText("Enter")

    def exitfunc(self):
        self.text1.setText("exit")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

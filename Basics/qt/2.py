#!/bin/python3
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(50, 150, 300, 450)
        self.setWindowTitle("ARENA")
        self.Ui()

    def Ui(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('images/spy.png'))
       # self.image.move(150, 150)

        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Enter Name")
        self.nameTextBox.move(80, 50)

        self.passTextBox = QLineEdit(self)
        self.passTextBox.move(80, 80)
        self.passTextBox.setPlaceholderText("Enter Password")
        self.passTextBox.setEchoMode(QLineEdit.Password)

        enterButton = QPushButton("Enter", self)
        enterButton.move(80, 130)
        enterButton.clicked.connect(self.enterfunc)

        self.remember = QCheckBox("Remember me", self)
        self.remember.move(80, 110)

        self.show()

    def enterfunc(self):
        name = self.nameTextBox.text()
        password = self.passTextBox.text()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

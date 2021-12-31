import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("THERE")
        self.setGeometry(150, 150, 500, 500)
        self.Ui()

    def Ui(self):
        self.editor = QTextEdit(self)
        self.editor.move(150, 80)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

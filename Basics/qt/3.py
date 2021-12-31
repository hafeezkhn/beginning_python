import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font = QFont("Times", 12)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RADIO")
        self.setGeometry(250, 150, 500, 500)
        self.Ui()

    def Ui(self):
        button = QPushButton("Click me", self)
        button.move(200, 150)
        button.setFont(font)
        button.clicked.connect(self.messageBox)
        self.show()

    def messageBox(self):
        nbox = QMessageBox.question(self, "Warning", "Are you sure", QMessageBox.Yes |
                                    QMessageBox.No | QMessageBox.Cancel, QMessageBox.No)
        if nbox == QMessageBox.Yes:
            sys.exit()
        elif nbox == QMessageBox.No:
            print("NO clicked")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

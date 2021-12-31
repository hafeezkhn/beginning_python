import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPS")
        self.setGeometry(350, 50, 550, 500)
        self.UI()

    def UI(self):
        mainLayout = QVBoxLayout()
        top = QHBoxLayout()
        bottom = QHBoxLayout()

        mainLayout.addLayout(top)
        mainLayout.addLayout(bottom)

        cbox = QCheckBox()
        rbtn = QRadioButton()
        combo = QComboBox()
        btn1 = QPushButton()
        btn2 = QPushButton()

        top.setContentsMargins(100, 10, 20, 20)

        top.addWidget(cbox)
        top.addWidget(rbtn)
        top.addWidget(combo)

        bottom.addWidget(btn1)
        bottom.addWidget(btn2)

        self.setLayout(mainLayout)

        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

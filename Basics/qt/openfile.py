import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RPS")
        self.setGeometry(350, 50, 550, 500)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        self.editor = QTextEdit()
        fileButton = QPushButton("open file")
        fileButton.clicked.connect(self.openFile)

        vbox.addWidget(self.editor)
        vbox.addLayout(hbox)
        hbox.addWidget(fileButton)

        self.setLayout(vbox)

        self.show()

    def openFile(self):
        url = QFileDialog.getOpenFileName(
            self, "open", "", "All files(*);;*txt")
        print(url)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SLider")
        self.setGeometry(350, 150, 350, 400)
        self.UI()

    def UI(self):
        vbox = QVBoxLayout()
        self.tabs = QTabWidget()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TicksAbove)
        self.slider.setTickInterval(10)
        self.slider.valueChanged.connect(self.getValue)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1, "first tab")
        self.tabs.addTab(self.tab2, "second tab")

        self.text1 = QLabel("0")
        self.text1.setAlignment(Qt.AlignCenter)

        vbox.addStretch()
        vbox.addWidget(self.slider)
        vbox.addWidget(self.text1)
        vbox.addWidget(self.tabs)

        self.setLayout(vbox)

        self.show()

    def getValue(self):
        val = self.slider.value()
        self.text1.setText(str(val))


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

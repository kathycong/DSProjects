import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(aa.exec())

    
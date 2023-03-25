import sys
from PyQt5.QtWidgets import (Qwidget, QApplication, 
                             QHBoxLayout, QVBoxLayout, QPushButton, QLabel)

#creating a window or our main widget

class MainWindow(Qwidget):
    def __init__(self):
        super().__init__()
        self.init_ui() 

    #this will run all our code, init_ui
    def init_ui(self):
        label = QLabel("Name: ")
        name_input = QLineEdit()
        button = QPushButton("Set Name")

        h = QHBoxLayout()
        h.addStretch(1) #removed this later
        h.addWidget(label)
        h.addWidget(name_input)

        v = QVBoxLayout()
        v.addStretch(1) 
        v.addLayout(h)
        v.addWidget(button)

        self.setLayout(v)

        self.setWindowTitle("Horizontal Layout")
        self.show()

#running the code
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
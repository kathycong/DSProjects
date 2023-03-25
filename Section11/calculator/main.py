import sys
from PyQt5.QtWidgets import (Qwidget, QApplication, 
                             QHBoxLayout, QVBoxLayout, QPushButton, QLabel)

#creating a window or our main widget

class MainWindow(Qwidget):
    def __init__(self):
        super().__init__()
        self.init_ui() 
        self.counter = 0

    #this will run all our code, init_ui
    def init_ui(self):
        label = QLabel("Name: ")
        name_input = QLineEdit()
        self.button = QPushButton("Clicked: ")
        self.button.pressed.connect(self.pressButton)
        self.button.released.connect(self.clickedButton)

        h = QHBoxLayout()
        h.addStretch(1) #removed this later
        h.addWidget(label)
        h.addWidget(name_input)

        v = QVBoxLayout()
        v.addStretch(1) 
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)

        self.setWindowTitle("Horizontal Layout")
        self.show()

    def clickedButton(self):
        print("This button has been released")

    def pressButton(self):
        print("This button has been pressed")
        self.counter += 1
        self.button.setText("Clicked: " + str(self.counter))

#running the code
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
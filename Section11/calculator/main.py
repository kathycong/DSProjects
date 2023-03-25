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
        self.text_label = QLabel("There has been no name entereed, so I can't do anything yet")
        self.label = QLabel("Name: ")
        self.name_input = QLineEdit()
        self.button = QPushButton("Clicked: ")
        self.button.pressed.connect(self.pressButton)
        self.button.released.connect(self.clickedButton)

        self.button.setText("Set Name")
        self.button.clicked.connect(self.alterName)

        h = QHBoxLayout()
        h.addWidget(self.label)
        h.addWidget(self.name_input)

        v = QVBoxLayout()
        v.addWidget(self.text_label)
        v.addLayout(h)
        v.addWidget(self.button)

        self.setLayout(v)

        self.setWindowTitle("Nothing has been clicked")
        self.show()

    def alterName(self):
        inputted_text = self.name_input.text()
        our_string = "You've entered " + inputted_text
        self.text_label.setText(our_string)
        self.setWindowTitle(inputted_text + "'s Window")




#running the code
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
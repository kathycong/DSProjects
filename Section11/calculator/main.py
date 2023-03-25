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
        label = QLabel("Hi there, I'm a label. Woot")
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        horizontal = QHBoxLayout()
        horizontal.addStretch()

        #example of a widgeth is a push button, notebook and etc
        #use this method to stuff things to the layout
        horizontal.addWidget(okButton)
        horizontal.addWidget(cancelButton)

        vertical = QVBoxLayout()
        vertical.addWidget(label)
        vertical.addStretch(1)
        vertical.addLayout(horizontal)

        #setting which lay out to use
        self.setLayout(vertical)

        self.setWindowTitle("Horizontal Layout")
        self.show()

#running the code
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
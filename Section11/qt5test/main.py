#!usr/bin/python3

from PyQt5.QtCore import *
from PyQt5.QtWidgest import *

#Qwidget inherits from the Page class
class Page(Qwidget): 
    def __init__(self, parent = None):
        super(Page, self).__init__(parent)

        my_label = Qlabel("this is my label")
        layout = QVBoxLayout()

        layout.addWidget(my_label)

        mainLayout = QGridLayout()
        mainLayout.addLayout(layout, 0, 1)

        self.Layout(mainLayout)
        self.setWindowTitle("my First Qt App")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = Page()
    window.show()

    sys.exit(app.exec())



    
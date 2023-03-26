import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar, 
                             QFrame, QStackedLayout, QTabWidget)


from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *

#creating our main application
class App(QFrame):
    def __init__(self):
        super().__init__() #initialising the parent
        self.setWindowTitle("Web Browser")
        set.setBaseSize(1366, 768)
        self.CreateApp()

    #this where we are doing stuff
    #setting up our main window
    def CreateApp(self):
        self.layout = QVBoxLayout()

        self.tabbar = QTabBar()
        #self.tabbar = QTabWidget()

        #adding tabs
        self.tabbar.addTab("Tab 1") #tab 0
        self.tabbar.addTab("Tab 2") #tab 1

        #setting the current index of the tab. Telling which tab is active
        self.tabbar.setCurrentIndex(0)

        self.layout.addWidget(self.tabbar)
        self.setLayout(self.layout)

        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())




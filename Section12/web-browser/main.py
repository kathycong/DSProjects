import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar, 
                             QFrame, QStackedLayout, QTabWidget)


from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *

class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousePressEvent(self, e):
        self.selectAll()

#creating our main application
class App(QFrame):
    def __init__(self):
        super().__init__() #initialising the parent
        self.setWindowTitle("Web Browser")
        self.CreateApp()
        set.setBaseSize(1366, 768)

    #this where we are doing stuff
    #setting up our main window
    def CreateApp(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsmargins(0, 0, 0, 0)


        #Create Tabs

        self.tabbar = QTabBar(movable = True, tabsClosable = True)
        self.tabbar.tabCloseRequested.connect(self.CloseTab) #this is a signal not a method. sends a connection which tabl should be closed

        #adding tabs
        self.tabbar.addTab("Tab 1") #tab 0
        self.tabbar.addTab("Tab 2") #tab 1

        #setting the current index of the tab. Telling which tab is active
        self.tabbar.setCurrentIndex(0)

        #Create AddressBar
        self.Toolbar = QWidget()
        self.ToolbarLayout = QHBoxLayout()
        self.addressbar = AddressBar()

        self.Toolbar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.addressbar)

        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.Toolbar)
        self.setLayout(self.layout)

        self.show()

    def CloseTab(self, i):
        self.tabbar.removeTab(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())




import sys
import os
import json

from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QLabel, QLineEdit, QTabBar, 
                             QFrame, QStackedLayout, QTabWidget)


from PyQt5.QtGui import QIcon, QWindow, QImage
from PyQt5.QtCore import *
from PyQt5.QtWebEngine import *

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
        self.tabbar.tabBarClicked.connec(self.SwitchTab)

        #setting the current index of the tab. Telling which tab is active
        self.tabbar.setCurrentIndex(0)

        #Keep track of tabs
        self.tabCount = 0
        self.tabs = []
        

        #Create AddressBar
        self.Toolbar = QWidget()
        self.ToolbarLayout = QHBoxLayout()
        self.addressbar = AddressBar()
        self.AddTabButton = QPushButton("+")

        self.addressbar.returnPressed.connect(self.BrowseTo)

        # New tab button
        self.AddTabButton.clicked.connect(self.AddTab)

        self.Toolbar.setLayout(self.ToolbarLayout)
        self.ToolbarLayout.addWidget(self.addressbar)
        self.ToolbarLayout.addWidget(self.AddTabButton)

        #set main view
        self.container = QWidget()
        self.container.layout = QStackedLayout()
        self.container.setLayout(self.container.layout)

        self.layout.addWidget(self.tabbar)
        self.layout.addWidget(self.Toolbar)
        self.layout.addWidget(self.container)
        self.setLayout(self.layout)

        self.AddTab()

        self.show()

    def CloseTab(self, i):
        self.tabbar.removeTab(i)

    def AddTab(self):
        i = self.tabCount

        self.tabs.append(QWidget())
        self.tabs[i].layout = QVBoxLayout()
        self.tabs[i].setObjectName("tab" + str(i))

        #Oopen webview
        self.tabs[i].content = QWebEngineView()
        self.tabs[i].content.load(QUrl.fromUserInput("http://google.com"))

        #Add webview to tabs layout
        self.tabs[i].layout.addWidget(self.tabs[i].content)


        # set top level tab from [] to layout
        self.tabs[i].setLayout(self.tabs[i].layout)

        #Add tab to top level stackedwidget
        self.container.layout.AddWidget(self.tabs[i])
        self.container.layout.setCurrentWidge(self.tabs[i])

        #Set the tab at top of screen
        self.tabbar.addTab("New Tab")
        self.tabbar.setTabData(i, "tab" + str(i))
        self.tabbar.setCurrentIndex(i)
        self.tabCount += 1

    def SwitchTab(self, i):
        tab_data = self.tabbar.tabData(i)
        print("tab: ", tab_data)

        tab_content = self.findChild(QWidget, tab_data)
        self.container.layout.setCurrentWidget(self.tabs[i])


    def BrowseTo(self):
        text = self.addressbar.text()
        print(text)

        i = self.tabbar.currentIndex()
        tab = self.tabbar.tabData(i)
        wv = self.findChild(QWidget, tab).content

        if "http" not in text:
            if "." not in text:
                url = "https://google.com/#q=" + text
            else: 
                url = "http://" + text
        else:
            url = text


        wv.load(QUrl.fromUserInput(url))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()

    sys.exit(app.exec_())




import sys
import client
from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import results_screen_ui
import time


# Static Variables for pipes
CONNECTION = "tcp://localhost:5555"


class MainWindow(QMainWindow):
    '''Defines the Home screen for the application and the functionality of each object.'''
    def __init__(self):
        '''Initializes the the Home screen and adds events for each of the buttons.'''
        super(MainWindow,self).__init__()
        uic.loadUi("Home_screen.ui",self)
        self.GenerateTrail.clicked.connect(self.goto_search)
        self.trailList.clicked.connect(self.goto_trails)
    
    def goto_search(self):
        '''Defines the event for the Generate trails button.
        Takes the user to the the Search screen.'''
        mtb_app.setCurrentIndex(mtb_app.currentIndex() + 1)

    def goto_trails(self):
        '''Defines the event for the trailsList button.
        Takes the user to the Trails Riden screen.'''
        mtb_app.setCurrentWidget(trailList)
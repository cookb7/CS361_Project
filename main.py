import sys
import socket
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import 

# Static Variables for pipes
HOST = 'localhost'
PORT = 2001


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


class searchScreen(QMainWindow):
    '''Defines the Search screen for the application and the functionality of each object.'''
    def __init__(self):
        '''Initializes the the Search screen and adds events for each of the buttons.'''
        super(searchScreen,self).__init__()
        uic.loadUi("search_screen.ui",self)
        self.home.clicked.connect(self.goto_home)
        self.generateButton.clicked.connect(self.generate)
        
    def goto_home(self):
        '''Takes the user back to the Home screen.'''
        mtb_app.setCurrentIndex(0)

    def generate(self):
        '''Creates the sql, sends it to the database microservices and
        takes the user to the Results screen'''
        # Create sql
        # TODO 
        sql = "Sending out an SOS! I'm sending out an SOS!"

        # Send sql
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        skt.connect((HOST, PORT))
        skt.send(sql.encode())

        # Add data to table in results
        data = resultScreen.add_trail("Moderate", '10')

        # Take user to the results screeen
        mtb_app.setCurrentWidget(results)

    
class resultScreen(QMainWindow):
    def __init__(self):
        super(resultScreen,self).__init__()
        uic.loadUi("results_screen.ui",self)
        self.back.clicked.connect(self.goto_search)
        self.home.clicked.connect(self.goto_home)
        

    def goto_search(self):
        mtb_app.setCurrentIndex(mtb_app.currentIndex() - 1)
    
    def goto_home(self):
        mtb_app.setCurrentIndex(0)

    def add_trail(self, dif, len):
        trail_dif = self.trailList.item(0, 0)
        trail_dif.setText(dif)

        trail_len = self.trailList.item(0, 1)
        trail_len.setText(len)


class trailListScreen(QMainWindow):
    def __init__(self):
        super(trailListScreen,self).__init__()
        uic.loadUi("trails_riden_screen.ui",self)
        self.searchButton.clicked.connect(self.search)
        self.home.clicked.connect(self.goto_home)

    def goto_home(self):
        mtb_app.setCurrentIndex(0)
        
    def search(self):
        mtb_app.setCurrentWidget(results)


if __name__ == "__main__":
    
    # Create the application
    app = QApplication(sys.argv)
    mtb_app = QtWidgets.QStackedWidget()

    # Add screens to application
    mainwindow = MainWindow()
    search = searchScreen()
    results = resultScreen()
    trailList = trailListScreen()

    # Initialize widgets
    mtb_app.addWidget(mainwindow)
    mtb_app.addWidget(search)
    mtb_app.addWidget(results)
    mtb_app.addWidget(trailList)

    # Show applicaton
    mtb_app.setFixedWidth(600)
    mtb_app.setFixedHeight(800)
    mtb_app.show()

    # Close app
    sys.exit(app.exec_())
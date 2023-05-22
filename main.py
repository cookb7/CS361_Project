import sys
import client
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QListWidget, QTextEdit


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
        # Select all data in the table
        sql = "SELECT trails.name FROM riden JOIN trails ON riden.trail_id = trails.trail_id"
        # Send to server
        data = client.send_sql_request(sql)
        data_list = data.split('\n')
        trail_list = trailListScreen.removeBreak(trailListScreen, data_list)

        # Add to list
        mtb_app.setCurrentWidget(trailList)
        trailListScreen.displayResults(trailListScreen, trail_list)




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
        # Difficulty Selection
        current = mtb_app.currentWidget()
        select = current.findChild(QComboBox, 'difficulty')
        dif = select.currentText()

        # Length Selection
        min_len, max_len = self.findLength()

        # Elevation Selection
        min_elev, max_elev = self.findElevation()

        sql = f"SELECT name, difficulty, length, elev FROM trails \
        WHERE difficulty = '{dif}' AND length BETWEEN '{min_len}' \
        AND '{max_len}' AND elev BETWEEN '{min_elev}' AND '{max_elev}'"

        # Send sql
        data = client.send_sql_request(sql)

        # Split data to list
        data_list = data.split('\n')
    
        # Add data to table in results
        mtb_app.setCurrentWidget(results)
        resultScreen.add_trail(resultScreen, data_list) 

    def findLength(self):
        '''Finds the input length and returns the range'''
        current = mtb_app.currentWidget()
        length_list = [(0, 5), (5, 10), (10, 20)]
        select = current.findChild(QComboBox, 'length')
        index = select.currentIndex()
        return length_list[index]
    
    def findElevation(self):
        '''Finds the input elevation and returns the range'''
        current = mtb_app.currentWidget()
        elev_list = [(0, 500), (500, 1000), (1000, 1500)]
        select = current.findChild(QComboBox, 'elevation')
        index = select.currentIndex()
        return elev_list[index]

    
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

    def add_trail(self, data_list):
        '''Yeah this sucks but I couldn't find another way'''
        current = mtb_app.currentWidget()
        if len(data_list) >= 1:
            trail_1 = current.findChild(QLabel, 'trail_1')
            trail_1.setText(data_list[0])
        if len(data_list) >= 2:
            trail_2 = current.findChild(QLabel, 'trail_2')
            trail_2.setText(data_list[1])
        if len(data_list) >= 3:
            trail_3 = current.findChild(QLabel, 'trail_3')
            trail_3.setText(data_list[2])
        if len(data_list) >= 4:
            trail_3 = current.findChild(QLabel, 'trail_4')
            trail_3.setText(data_list[3])
        if len(data_list) >= 5:
            trail_3 = current.findChild(QLabel, 'trail_5')
            trail_3.setText(data_list[4])

class trailListScreen(QMainWindow):
    def __init__(self):
        super(trailListScreen,self).__init__()
        uic.loadUi("trails_riden_screen.ui",self)
        self.home.clicked.connect(self.goto_home)
        self.addButton.clicked.connect(self.add_trail)

    def goto_home(self):
        mtb_app.setCurrentIndex(0)
        
    def displayResults(self, trail_list):
        current = mtb_app.currentWidget()
        trails = current.findChild(QListWidget, 'trailsRiden')
        if len(trail_list) >= 1:
            trail_1 = trails.item(0)
            trail_1.setText(trail_list[0])
        if len(trail_list) >= 2:
            trail_2 = trails.item(1)
            trail_2.setText(trail_list[1])
        if len(trail_list) >= 3:
            trail_3 = trails.item(2)
            trail_3.setText(trail_list[2])
        if len(trail_list) >= 4:
            trail_3 = trails.item(3)
            trail_3.setText(trail_list[3])
        if len(trail_list) >= 5:
            trail_3 = trails.item(4)
            trail_3.setText(trail_list[4])

    def removeBreak(self, data_list):
        trail_list = []
        for i in range(len(data_list)):
            trail = data_list[i].replace('|', '')
            trail_list.append(trail)
        return trail_list
    
    def add_trail(self):
        current = mtb_app.currentWidget()
        search = current.findChild(QTextEdit, "searchText")
        trail = search.toPlainText()

        # Find number of entries
        sql = 'SELECT * FROM riden'
        data = client.send_sql_request(sql)
        data_list = data.split('\n')
        riden_id = len(data_list)

        # Insert new trail
        sql = f"INSERT INTO riden VALUES({riden_id}, (SELECT trail_id FROM trails WHERE name = '{trail}'))"
        client.send_sql_request(sql)
        # Add to list
        sql = "SELECT trails.name FROM riden JOIN trails ON riden.trail_id = trails.trail_id"
        data = data = client.send_sql_request(sql)
        data_list = data.split('\n')
        trail_list = self.removeBreak(data_list)
        self.displayResults(trail_list)


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
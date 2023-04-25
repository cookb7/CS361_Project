import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        uic.loadUi("Home_screen.ui",self)
        self.GenerateTrail.clicked.connect(self.goto_search)
        self.reviewTrail.clicked.connect(self.goto_review)
    
    def goto_search(self):
        mtb_app.setCurrentIndex(mtb_app.currentIndex() + 1)

    def goto_review(self):
        mtb_app.setCurrentWidget(reviewTrail)


class searchScreen(QMainWindow):
    def __init__(self):
        super(searchScreen,self).__init__()
        uic.loadUi("search_screen.ui",self)
        self.home.clicked.connect(self.goto_search)
        self.generateButton.clicked.connect(self.generate)
        
    def goto_search(self):
        mtb_app.setCurrentIndex(mtb_app.currentIndex() - 1)

    def generate(self):
        mtb_app.setCurrentIndex(mtb_app.currentIndex() + 1)

    



class resultScreen(QMainWindow):
    def __init__(self):
        super(resultScreen,self).__init__()
        uic.loadUi("results_screen.ui",self)
        self.back.clicked.connect(self.goto_search)
        self.home.clicked.connect(self.goto_home)
        self.review.clicked.connect(self.goto_addReview)

    def goto_search(self):
        mtb_app.setCurrentIndex(mtb_app.currentIndex() - 1)
    
    def goto_home(self):
        mtb_app.setCurrentIndex(0)

    def goto_addReview(self):
        mtb_app.setCurrentWidget(addReview)


class reviewTrailScreen(QMainWindow):
    def __init__(self):
        super(reviewTrailScreen,self).__init__()
        uic.loadUi("review_trail_screen.ui",self)
        self.searchButton.clicked.connect(self.search)
        self.home.clicked.connect(self.goto_home)

    def goto_home(self):
        mtb_app.setCurrentIndex(0)
        
    def search(self):
        mtb_app.setCurrentWidget(addReview)


class addReviewScreen(QMainWindow):
    def __init__(self):
        super(addReviewScreen,self).__init__()
        uic.loadUi("add_review_screen.ui",self)
        self.back.clicked.connect(self.goto_review)
        self.home.clicked.connect(self.goto_home)
        self.submit.clicked.connect(self.goto_home)

    def goto_home(self):
        mtb_app.setCurrentIndex(0)

    def goto_review(self):
        mtb_app.setCurrentWidget(reviewTrail)
    


app = QApplication(sys.argv)
mtb_app = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
search = searchScreen()
results = resultScreen()
reviewTrail = reviewTrailScreen()
addReview = addReviewScreen()

mtb_app.addWidget(mainwindow)
mtb_app.addWidget(search)
mtb_app.addWidget(results)
mtb_app.addWidget(reviewTrail)
mtb_app.addWidget(addReview)



mtb_app.setFixedWidth(800)
mtb_app.setFixedHeight(600)
mtb_app.show()
sys.exit(app.exec_())
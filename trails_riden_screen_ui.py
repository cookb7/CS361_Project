# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Brendan\Documents\CS 361\MTBApp\GUI\trails_riden_screen.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(230, 10, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.home = QtWidgets.QPushButton(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(0, 0, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        self.home.setFont(font)
        self.home.setObjectName("home")
        self.searchText = QtWidgets.QTextEdit(self.centralwidget)
        self.searchText.setGeometry(QtCore.QRect(50, 660, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(18)
        self.searchText.setFont(font)
        self.searchText.setObjectName("searchText")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 640, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(300, 670, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(14)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.trailsRiden = QtWidgets.QListWidget(self.centralwidget)
        self.trailsRiden.setGeometry(QtCore.QRect(50, 70, 501, 561))
        self.trailsRiden.setObjectName("trailsRiden")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        item.setFont(font)
        self.trailsRiden.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        item.setFont(font)
        self.trailsRiden.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        item.setFont(font)
        self.trailsRiden.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        item.setFont(font)
        self.trailsRiden.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(20)
        item.setFont(font)
        self.trailsRiden.addItem(item)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 750, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Riden Trails"))
        self.home.setText(_translate("MainWindow", "Home"))
        self.label_3.setText(_translate("MainWindow", "Add trail to list"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        __sortingEnabled = self.trailsRiden.isSortingEnabled()
        self.trailsRiden.setSortingEnabled(False)
        self.trailsRiden.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("MainWindow", "Application by Brendan Cook"))

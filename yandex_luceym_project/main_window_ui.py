# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Main_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 891)
        MainWindow.setStyleSheet("backgroud-color: #3f2561")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(./images/back.jpg);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 180, 451, 61))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: white;\n"
"background: opacity 0;\n"
"\n"
"")
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 240, 641, 31))
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font-family: \'Merienda\';\n"
"color: #fff;\n"
"font-weight: bold;\n"
"font-size: 22px;\n"
"background: opacity 0;")
        self.label_2.setObjectName("label_2")
        self.button_travel = QtWidgets.QPushButton(self.centralwidget)
        self.button_travel.setGeometry(QtCore.QRect(160, 510, 321, 41))
        self.button_travel.setStyleSheet("QPushButton{\n"
"background-color: #425865;\n"
"border: 2px solid #425865;\n"
"border-radius: 30px;\n"
"color: white;\n"
"font-family: \'Luckiest Guy\', cursive;\n"
"font-size: 15px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #fa4244;\n"
"}")
        self.button_travel.setObjectName("button_travel")
        self.button_convert = QtWidgets.QPushButton(self.centralwidget)
        self.button_convert.setGeometry(QtCore.QRect(160, 580, 321, 41))
        self.button_convert.setStyleSheet("QPushButton{\n"
"background-color: #425865;\n"
"border: 2px solid #425865;\n"
"border-radius: 30px;\n"
"color: white;\n"
"font-family: \'Luckiest Guy\', cursive;\n"
"font-size: 15px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #fa4244;\n"
"}")
        self.button_convert.setObjectName("button_convert")
        self.button_weather = QtWidgets.QPushButton(self.centralwidget)
        self.button_weather.setGeometry(QtCore.QRect(160, 650, 321, 41))
        self.button_weather.setStyleSheet("QPushButton{\n"
"background-color: #425865;\n"
"border: 2px solid #425865;\n"
"border-radius: 30px;\n"
"color: white;\n"
"font-family: \'Luckiest Guy\', cursive;\n"
"font-size: 15px;\n"
"}\n"
"QPushButton:pressed{\n"
"    background-color: #fa4244;\n"
"}")
        self.button_weather.setObjectName("button_weather")
        self.information = QtWidgets.QPushButton(self.centralwidget)
        self.information.setGeometry(QtCore.QRect(570, 820, 61, 51))
        self.information.setAutoFillBackground(False)
        self.information.setStyleSheet("QPushButton{\n"
"    background-color: #425865;\n"
"    border: 2px solid #425865;\n"
"    border-radius: 30px;\n"
"    color: white;\n"
"    font-family: \'Luckiest Guy\', cursive;\n"
"    font-size: 15px;\n"
"    border-radius: 20%;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #fa4244;\n"
"}")
        self.information.setObjectName("information")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"</style></head><body style=\" font-family:\'Luckiest Guy\',\'cursive\'; font-size:45px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:27pt;\">Traveler\'s suitcase</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "GET READY FOR A TRIP WITHOUT ANY PROBLEMS!"))
        self.button_travel.setText(_translate("MainWindow", "Let\'s go in travel!"))
        self.button_convert.setText(_translate("MainWindow", "Convert your valute"))
        self.button_weather.setText(_translate("MainWindow", "Weather in country"))
        self.information.setText(_translate("MainWindow", "?"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'temperature.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Temperature(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(668, 890)
        MainWindow.setStyleSheet("backgroud: opacity 0;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(./images/back.jpg);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 110, 491, 61))
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
        self.button_get_the_weather = QtWidgets.QPushButton(self.centralwidget)
        self.button_get_the_weather.setGeometry(QtCore.QRect(140, 460, 361, 71))
        self.button_get_the_weather.setStyleSheet("QPushButton{\n"
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
        self.button_get_the_weather.setObjectName("button_get_the_weather")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 300, 411, 71))
        font = QtGui.QFont()
        font.setFamily("Merienda")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: #fff;\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 660, 511, 111))
        font = QtGui.QFont()
        font.setFamily("Merienda")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #fff;")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btn_home = QtWidgets.QPushButton(self.centralwidget)
        self.btn_home.setGeometry(QtCore.QRect(590, 820, 61, 51))
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet("QPushButton{\n"
"    border: 2px solid #425865;\n"
"    border-radius: 30px;\n"
"    border-radius: 20%;\n"
"    background-color: opacity 0;\n"
"    \n"
"}\n"
"")
        self.btn_home.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/house.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QtCore.QSize(40, 40))
        self.btn_home.setObjectName("btn_home")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"</style></head><body style=\" font-family:\'Luckiest Guy\',\'cursive\'; font-size:45px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:27pt;\">Check temperature!\n"
"</span></p></body></html>"))
        self.button_get_the_weather.setText(_translate("MainWindow", "get the weather"))

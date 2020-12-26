# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Info(object):
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
        self.label.setGeometry(QtCore.QRect(30, 80, 491, 61))
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
        self.label_2.setGeometry(QtCore.QRect(30, 280, 361, 51))
        font = QtGui.QFont()
        font.setFamily("Merienda")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("font-family: \'Merienda\';\n"
"color: #fff;\n"
"font-weight: bold;\n"
"font-size: 40px;\n"
"background: opacity 0;")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 581, 61))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(36)
        self.label_5.setFont(font)
        self.label_5.setAcceptDrops(False)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setStyleSheet("color: white;\n"
"background: opacity 0;\n"
"\n"
"")
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 210, 581, 61))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(36)
        self.label_6.setFont(font)
        self.label_6.setAcceptDrops(False)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setStyleSheet("color: white;\n"
"background: opacity 0;\n"
"\n"
"")
        self.label_6.setWordWrap(False)
        self.label_6.setObjectName("label_6")
        self.btn_home = QtWidgets.QPushButton(self.centralwidget)
        self.btn_home.setGeometry(QtCore.QRect(590, 810, 61, 51))
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
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:27pt;\">If you have questions</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "+79992283988"))
        self.label_5.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"</style></head><body style=\" font-family:\'Luckiest Guy\',\'cursive\'; font-size:45px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:27pt;\">you can contact me</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"</style></head><body style=\" font-family:\'Luckiest Guy\',\'cursive\'; font-size:45px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:27pt;\">in telegram</span></p></body></html>"))

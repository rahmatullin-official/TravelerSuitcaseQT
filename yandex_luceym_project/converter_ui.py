# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'converter.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Converter(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 891)
        MainWindow.setStyleSheet("background-image: url(./images/conv_back.jpeg);\n"
"color: #fff;\n"
"align-items: center;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-image: url(./images/back.jpeg);\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.btn_home = QtWidgets.QPushButton(self.centralwidget)
        self.btn_home.setGeometry(QtCore.QRect(570, 820, 61, 51))
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
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 331, 81))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: opacity 0;\n"
"color: #fff;\n"
"")
        self.label_3.setObjectName("label_3")
        self.input_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.input_currency.setGeometry(QtCore.QRect(130, 310, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(14)
        self.input_currency.setFont(font)
        self.input_currency.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid #425865;\n"
"color: #33A6C5;\n"
"placeholder-color: #33A6C5;")
        self.input_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.input_currency.setObjectName("input_currency")
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(130, 430, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(14)
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid #425865;\n"
"color: #33A6C5;\n"
"placeholder-color: #33A6C5;")
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.output_currency = QtWidgets.QLineEdit(self.centralwidget)
        self.output_currency.setGeometry(QtCore.QRect(130, 560, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(14)
        self.output_currency.setFont(font)
        self.output_currency.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid #425865;\n"
"color: #33A6C5;\n"
"placeholder-color: #33A6C5;")
        self.output_currency.setAlignment(QtCore.Qt.AlignCenter)
        self.output_currency.setObjectName("output_currency")
        self.output_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.output_amount.setGeometry(QtCore.QRect(130, 690, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(14)
        self.output_amount.setFont(font)
        self.output_amount.setStyleSheet("border-radius: 30px;\n"
"border: 2px solid #425865;\n"
"color: #33A6C5;\n"
"placeholder-color: #33A6C5;")
        self.output_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.output_amount.setReadOnly(True)
        self.output_amount.setObjectName("output_amount")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 800, 380, 60))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: #33A6C5;\n"
"    border-radius: 30;\n"
"    border: 2px solid #425865;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #ABBBBB;\n"
"\n"
"};")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 195, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Luckiest Guy")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("background: opacity 0;\n"
"color: #fff;\n"
"")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "CONVERT YOUR VALUTE"))
        self.pushButton.setText(_translate("MainWindow", "CONVERT"))
        self.label.setText(_translate("MainWindow", "(USD, EURO, CNY)"))

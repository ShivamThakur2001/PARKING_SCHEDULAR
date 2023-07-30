# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\HP\Desktop\Internship 2\Parking Scheduler\Parking.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1175, 836)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(50, 80, 1065, 581))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 0, 1061, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Background.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(660, 20, 181, 61))
        self.label_2.setStyleSheet("font: 90 25pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(660, 250, 191, 61))
        self.label_3.setStyleSheet("font: 90 18pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(660, 130, 251, 41))
        self.label_4.setStyleSheet("font: 90 18pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_4.setObjectName("label_4")
        self.USERNAME = QtWidgets.QLineEdit(self.tab)
        self.USERNAME.setGeometry(QtCore.QRect(660, 180, 261, 41))
        self.USERNAME.setStyleSheet("font: 90 18pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.USERNAME.setText("")
        self.USERNAME.setObjectName("USERNAME")
        self.PASSWORD = QtWidgets.QLineEdit(self.tab)
        self.PASSWORD.setGeometry(QtCore.QRect(660, 310, 261, 41))
        self.PASSWORD.setStyleSheet("font: 90 18pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.PASSWORD.setText("")
        self.PASSWORD.setObjectName("PASSWORD")
        self.LOGIN_BUTTON = QtWidgets.QPushButton(self.tab)
        self.LOGIN_BUTTON.setGeometry(QtCore.QRect(660, 400, 121, 41))
        self.LOGIN_BUTTON.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.LOGIN_BUTTON.setObjectName("LOGIN_BUTTON")
        self.LOGIN_INFO = QtWidgets.QLabel(self.tab)
        self.LOGIN_INFO.setGeometry(QtCore.QRect(670, 370, 271, 16))
        self.LOGIN_INFO.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.LOGIN_INFO.setText("")
        self.LOGIN_INFO.setObjectName("LOGIN_INFO")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(0, -20, 1065, 581))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Background.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.ADD = QtWidgets.QPushButton(self.tab_2)
        self.ADD.setGeometry(QtCore.QRect(690, 70, 221, 71))
        self.ADD.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.ADD.setObjectName("ADD")
        self.REMOVE = QtWidgets.QPushButton(self.tab_2)
        self.REMOVE.setGeometry(QtCore.QRect(690, 410, 221, 71))
        self.REMOVE.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.REMOVE.setObjectName("REMOVE")
        self.DISPLAY = QtWidgets.QPushButton(self.tab_2)
        self.DISPLAY.setGeometry(QtCore.QRect(640, 240, 321, 71))
        self.DISPLAY.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 87 12pt \"Arial Black\";")
        self.DISPLAY.setObjectName("DISPLAY")
        self.LOGOUT = QtWidgets.QPushButton(self.tab_2)
        self.LOGOUT.setGeometry(QtCore.QRect(950, 20, 93, 28))
        self.LOGOUT.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 87 8pt \"Arial Black\";")
        self.LOGOUT.setObjectName("LOGOUT")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(0, -30, 1065, 581))
        self.label_6.setStyleSheet("background-color: rgb(252, 246, 245);")
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(200, 10, 681, 61))
        self.label_9.setStyleSheet("color: rgb(153, 0, 17);\n"
"font: 87 20pt \"Arial Black\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(240, 140, 171, 31))
        self.label_10.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(240, 190, 171, 31))
        self.label_11.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(240, 240, 171, 31))
        self.label_12.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(240, 290, 211, 31))
        self.label_13.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(240, 340, 211, 31))
        self.label_14.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(240, 390, 171, 31))
        self.label_15.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_15.setObjectName("label_15")
        self.OWNER_NAME = QtWidgets.QLineEdit(self.tab_3)
        self.OWNER_NAME.setGeometry(QtCore.QRect(530, 140, 301, 31))
        self.OWNER_NAME.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.OWNER_NAME.setText("")
        self.OWNER_NAME.setObjectName("OWNER_NAME")
        self.MOBILE_NUMBER = QtWidgets.QLineEdit(self.tab_3)
        self.MOBILE_NUMBER.setGeometry(QtCore.QRect(530, 340, 301, 31))
        self.MOBILE_NUMBER.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.MOBILE_NUMBER.setText("")
        self.MOBILE_NUMBER.setObjectName("MOBILE_NUMBER")
        self.VEHICLE_NUMBER = QtWidgets.QLineEdit(self.tab_3)
        self.VEHICLE_NUMBER.setGeometry(QtCore.QRect(530, 290, 301, 31))
        self.VEHICLE_NUMBER.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.VEHICLE_NUMBER.setText("")
        self.VEHICLE_NUMBER.setObjectName("VEHICLE_NUMBER")
        self.VEHICLE_NAME = QtWidgets.QLineEdit(self.tab_3)
        self.VEHICLE_NAME.setGeometry(QtCore.QRect(530, 190, 301, 31))
        self.VEHICLE_NAME.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.VEHICLE_NAME.setText("")
        self.VEHICLE_NAME.setObjectName("VEHICLE_NAME")
        self.label_16 = QtWidgets.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(240, 440, 171, 31))
        self.label_16.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_16.setObjectName("label_16")
        self.ARRIVAL_TIME = QtWidgets.QLabel(self.tab_3)
        self.ARRIVAL_TIME.setGeometry(QtCore.QRect(530, 390, 141, 31))
        self.ARRIVAL_TIME.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.ARRIVAL_TIME.setText("")
        self.ARRIVAL_TIME.setObjectName("ARRIVAL_TIME")
        self.ARRIVAL_DAY = QtWidgets.QLabel(self.tab_3)
        self.ARRIVAL_DAY.setGeometry(QtCore.QRect(530, 440, 141, 31))
        self.ARRIVAL_DAY.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.ARRIVAL_DAY.setText("")
        self.ARRIVAL_DAY.setObjectName("ARRIVAL_DAY")
        self.ADD_VEHICLE = QtWidgets.QPushButton(self.tab_3)
        self.ADD_VEHICLE.setGeometry(QtCore.QRect(380, 500, 93, 28))
        self.ADD_VEHICLE.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.ADD_VEHICLE.setObjectName("ADD_VEHICLE")
        self.BACK_3 = QtWidgets.QPushButton(self.tab_3)
        self.BACK_3.setGeometry(QtCore.QRect(500, 500, 111, 28))
        self.BACK_3.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.BACK_3.setObjectName("BACK_3")
        self.ADD_ALERT = QtWidgets.QLabel(self.tab_3)
        self.ADD_ALERT.setGeometry(QtCore.QRect(380, 80, 281, 31))
        self.ADD_ALERT.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"")
        self.ADD_ALERT.setText("")
        self.ADD_ALERT.setObjectName("ADD_ALERT")
        self.VEHICLE_TYPE = QtWidgets.QComboBox(self.tab_3)
        self.VEHICLE_TYPE.setGeometry(QtCore.QRect(530, 240, 301, 31))
        self.VEHICLE_TYPE.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.VEHICLE_TYPE.setObjectName("VEHICLE_TYPE")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(0, -30, 1065, 581))
        self.label_7.setStyleSheet("background-color: rgb(252, 246, 245);")
        self.label_7.setText("")
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_17 = QtWidgets.QLabel(self.tab_4)
        self.label_17.setGeometry(QtCore.QRect(83, 20, 881, 61))
        self.label_17.setStyleSheet("color: rgb(153, 0, 17);\n"
"font: 87 20pt \"Arial Black\";")
        self.label_17.setObjectName("label_17")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(40, 80, 981, 431))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setGeometry(QtCore.QRect(10, 10, 961, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(30, 30, 55, 16))
        self.label_18.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(150, 30, 61, 16))
        self.label_19.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(270, 20, 91, 16))
        self.label_20.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(390, 30, 91, 16))
        self.label_21.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_21.setObjectName("label_21")
        self.label_23 = QtWidgets.QLabel(self.frame)
        self.label_23.setGeometry(QtCore.QRect(750, 20, 81, 16))
        self.label_23.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(655, 20, 55, 16))
        self.label_22.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_22.setObjectName("label_22")
        self.label_33 = QtWidgets.QLabel(self.frame)
        self.label_33.setGeometry(QtCore.QRect(23, 10, 81, 16))
        self.label_33.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame)
        self.label_34.setGeometry(QtCore.QRect(141, 10, 81, 16))
        self.label_34.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame)
        self.label_35.setGeometry(QtCore.QRect(390, 10, 91, 16))
        self.label_35.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.frame)
        self.label_36.setGeometry(QtCore.QRect(515, 30, 91, 16))
        self.label_36.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.frame)
        self.label_37.setGeometry(QtCore.QRect(515, 10, 91, 16))
        self.label_37.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.frame)
        self.label_38.setGeometry(QtCore.QRect(861, 20, 91, 20))
        self.label_38.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_38.setObjectName("label_38")
        self.TABLE = QtWidgets.QTableWidget(self.groupBox)
        self.TABLE.setGeometry(QtCore.QRect(10, 80, 961, 341))
        self.TABLE.setObjectName("TABLE")
        self.TABLE.setColumnCount(0)
        self.TABLE.setRowCount(0)
        self.BACK = QtWidgets.QPushButton(self.tab_4)
        self.BACK.setGeometry(QtCore.QRect(500, 520, 93, 28))
        self.BACK.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(246, 240, 239);\n"
"color: rgb(153, 0, 17);")
        self.BACK.setObjectName("BACK")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_8 = QtWidgets.QLabel(self.tab_5)
        self.label_8.setGeometry(QtCore.QRect(0, -30, 1065, 581))
        self.label_8.setStyleSheet("background-color: rgb(252, 246, 245);")
        self.label_8.setText("")
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_24 = QtWidgets.QLabel(self.tab_5)
        self.label_24.setGeometry(QtCore.QRect(210, 10, 631, 61))
        self.label_24.setStyleSheet("color: rgb(153, 0, 17);\n"
"font: 87 20pt \"Arial Black\";")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_5)
        self.label_25.setGeometry(QtCore.QRect(240, 120, 211, 31))
        self.label_25.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_25.setObjectName("label_25")
        self.REMOVE_NUMBER = QtWidgets.QLineEdit(self.tab_5)
        self.REMOVE_NUMBER.setGeometry(QtCore.QRect(530, 120, 301, 31))
        self.REMOVE_NUMBER.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.REMOVE_NUMBER.setText("")
        self.REMOVE_NUMBER.setObjectName("REMOVE_NUMBER")
        self.REMOVE_OWNER_NAME = QtWidgets.QLineEdit(self.tab_5)
        self.REMOVE_OWNER_NAME.setGeometry(QtCore.QRect(530, 200, 301, 31))
        self.REMOVE_OWNER_NAME.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.REMOVE_OWNER_NAME.setText("")
        self.REMOVE_OWNER_NAME.setObjectName("REMOVE_OWNER_NAME")
        self.REMOVE_MOBILE_NUMBER = QtWidgets.QLineEdit(self.tab_5)
        self.REMOVE_MOBILE_NUMBER.setGeometry(QtCore.QRect(530, 350, 301, 31))
        self.REMOVE_MOBILE_NUMBER.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.REMOVE_MOBILE_NUMBER.setText("")
        self.REMOVE_MOBILE_NUMBER.setObjectName("REMOVE_MOBILE_NUMBER")
        self.REMOVE_VEHICLE_NAME = QtWidgets.QLineEdit(self.tab_5)
        self.REMOVE_VEHICLE_NAME.setGeometry(QtCore.QRect(530, 250, 301, 31))
        self.REMOVE_VEHICLE_NAME.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.REMOVE_VEHICLE_NAME.setText("")
        self.REMOVE_VEHICLE_NAME.setObjectName("REMOVE_VEHICLE_NAME")
        self.label_26 = QtWidgets.QLabel(self.tab_5)
        self.label_26.setGeometry(QtCore.QRect(240, 400, 171, 31))
        self.label_26.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_5)
        self.label_27.setGeometry(QtCore.QRect(240, 300, 171, 31))
        self.label_27.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.tab_5)
        self.label_28.setGeometry(QtCore.QRect(240, 350, 211, 31))
        self.label_28.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_28.setObjectName("label_28")
        self.REMOVAL_TIME_2 = QtWidgets.QLabel(self.tab_5)
        self.REMOVAL_TIME_2.setGeometry(QtCore.QRect(530, 450, 141, 31))
        self.REMOVAL_TIME_2.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.REMOVAL_TIME_2.setText("")
        self.REMOVAL_TIME_2.setObjectName("REMOVAL_TIME_2")
        self.label_29 = QtWidgets.QLabel(self.tab_5)
        self.label_29.setGeometry(QtCore.QRect(240, 200, 171, 31))
        self.label_29.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_29.setObjectName("label_29")
        self.REMOVE_VEHICLE_TYPE = QtWidgets.QLineEdit(self.tab_5)
        self.REMOVE_VEHICLE_TYPE.setGeometry(QtCore.QRect(530, 300, 301, 31))
        self.REMOVE_VEHICLE_TYPE.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.REMOVE_VEHICLE_TYPE.setText("")
        self.REMOVE_VEHICLE_TYPE.setObjectName("REMOVE_VEHICLE_TYPE")
        self.label_30 = QtWidgets.QLabel(self.tab_5)
        self.label_30.setGeometry(QtCore.QRect(240, 450, 181, 31))
        self.label_30.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.tab_5)
        self.label_31.setGeometry(QtCore.QRect(240, 250, 171, 31))
        self.label_31.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"color: rgb(153, 0, 17);")
        self.label_31.setObjectName("label_31")
        self.ARRIVAL_TIME_2 = QtWidgets.QLabel(self.tab_5)
        self.ARRIVAL_TIME_2.setGeometry(QtCore.QRect(530, 400, 141, 31))
        self.ARRIVAL_TIME_2.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.ARRIVAL_TIME_2.setText("")
        self.ARRIVAL_TIME_2.setObjectName("ARRIVAL_TIME_2")
        self.label_32 = QtWidgets.QLabel(self.tab_5)
        self.label_32.setGeometry(QtCore.QRect(530, 150, 301, 31))
        self.label_32.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(153, 0, 17);")
        self.label_32.setObjectName("label_32")
        self.REMOVE_BUTTON = QtWidgets.QPushButton(self.tab_5)
        self.REMOVE_BUTTON.setGeometry(QtCore.QRect(380, 510, 111, 28))
        self.REMOVE_BUTTON.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.REMOVE_BUTTON.setObjectName("REMOVE_BUTTON")
        self.SEARCH = QtWidgets.QPushButton(self.tab_5)
        self.SEARCH.setGeometry(QtCore.QRect(860, 120, 101, 28))
        self.SEARCH.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.SEARCH.setObjectName("SEARCH")
        self.BACK_2 = QtWidgets.QPushButton(self.tab_5)
        self.BACK_2.setGeometry(QtCore.QRect(520, 510, 111, 28))
        self.BACK_2.setStyleSheet("background-color: rgb(153, 0, 17);\n"
"border:none;\n"
"color: rgb(252, 246, 245);\n"
"font: 10 12pt \"Arial Black\";")
        self.BACK_2.setObjectName("BACK_2")
        self.REMOVE_ALERT = QtWidgets.QLabel(self.tab_5)
        self.REMOVE_ALERT.setGeometry(QtCore.QRect(370, 70, 371, 31))
        self.REMOVE_ALERT.setStyleSheet("font: 10 12pt \"Arial Black\";\n"
"")
        self.REMOVE_ALERT.setText("")
        self.REMOVE_ALERT.setObjectName("REMOVE_ALERT")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1175, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "LOGIN "))
        self.label_3.setText(_translate("MainWindow", "PASSWORD"))
        self.label_4.setText(_translate("MainWindow", "USERNAME"))
        self.LOGIN_BUTTON.setText(_translate("MainWindow", "LOGIN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.ADD.setText(_translate("MainWindow", "ADD VEHICLE"))
        self.REMOVE.setText(_translate("MainWindow", "REMOVE VEHICLE"))
        self.DISPLAY.setText(_translate("MainWindow", "DISPLAY PARKED VEHICLE"))
        self.LOGOUT.setText(_translate("MainWindow", "LOGOUT"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_9.setText(_translate("MainWindow", "ADD NEW VEHICLE TO THE PARKING"))
        self.label_10.setText(_translate("MainWindow", "OWNER NAME"))
        self.label_11.setText(_translate("MainWindow", "VEHICLE NAME"))
        self.label_12.setText(_translate("MainWindow", "VEHICLE TYPE"))
        self.label_13.setText(_translate("MainWindow", "VEHICLE NUMBER"))
        self.label_14.setText(_translate("MainWindow", "MOBILE NUMBER"))
        self.label_15.setText(_translate("MainWindow", "ARRIVAL TIME"))
        self.label_16.setText(_translate("MainWindow", "ARRIVAL DAY"))
        self.ADD_VEHICLE.setText(_translate("MainWindow", "ADD "))
        self.BACK_3.setText(_translate("MainWindow", "BACK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.label_17.setText(_translate("MainWindow", "LIST OF PARKED VEHICLE IN THE PARKING LOT"))
        self.label_18.setText(_translate("MainWindow", "NAME"))
        self.label_19.setText(_translate("MainWindow", "NAME"))
        self.label_20.setText(_translate("MainWindow", "TYPE 2/4"))
        self.label_21.setText(_translate("MainWindow", "NUMBER"))
        self.label_23.setText(_translate("MainWindow", "IN TIME"))
        self.label_22.setText(_translate("MainWindow", "DATE"))
        self.label_33.setText(_translate("MainWindow", "OWNER"))
        self.label_34.setText(_translate("MainWindow", "VEHICLE"))
        self.label_35.setText(_translate("MainWindow", "VEHICLE"))
        self.label_36.setText(_translate("MainWindow", "NUMBER"))
        self.label_37.setText(_translate("MainWindow", "MOBILE"))
        self.label_38.setText(_translate("MainWindow", "OUT TIME"))
        self.BACK.setText(_translate("MainWindow", "BACK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        self.label_24.setText(_translate("MainWindow", "REMOVE VEHICLE FROM PARKING"))
        self.label_25.setText(_translate("MainWindow", "VEHICLE NUMBER"))
        self.label_26.setText(_translate("MainWindow", "ARRIVAL TIME"))
        self.label_27.setText(_translate("MainWindow", "VEHICLE TYPE"))
        self.label_28.setText(_translate("MainWindow", "MOBILE NUMBER"))
        self.label_29.setText(_translate("MainWindow", "OWNER NAME"))
        self.label_30.setText(_translate("MainWindow", "REMOVAL TIME"))
        self.label_31.setText(_translate("MainWindow", "VEHICLE NAME"))
        self.label_32.setText(_translate("MainWindow", "Enter Vehicle Number To Remove"))
        self.REMOVE_BUTTON.setText(_translate("MainWindow", "REMOVE"))
        self.SEARCH.setText(_translate("MainWindow", "SEARCH"))
        self.BACK_2.setText(_translate("MainWindow", "BACK"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Page"))


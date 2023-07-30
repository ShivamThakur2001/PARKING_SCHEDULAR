from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5.QtPrintSupport import QPrinter 
from datetime import date,time
import sys
import sqlite3
import time


ui, _ = loadUiType("Parking.ui")

class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.LOGIN_BUTTON.clicked.connect(self.login)
        self.ADD.clicked.connect(self.add_vehicle)
        self.ADD_VEHICLE.clicked.connect(self.add)
        self.REMOVE.clicked.connect(self.remove_vehicle)
        self.SEARCH.clicked.connect(self.search)
        self.REMOVE_BUTTON.clicked.connect(self.remove)
        self.BACK_2.clicked.connect(self.back)
        self.LOGOUT.clicked.connect(self.logout)
        self.DISPLAY.clicked.connect(self.display)
        self.BACK_3.clicked.connect(self.back1)
        self.BACK.clicked.connect(self.back2)
    
    ## LOGIN ##
    def login(self):
        un = self.USERNAME.text()
        pw = self.PASSWORD.text()
        if(un =="Admin" and pw == "Admin@123"):
            self.USERNAME.setText("")
            self.PASSWORD.setText("")
            self.tabWidget.setCurrentIndex(1)
        else:
            self.LOGIN_INFO.setText("Invalid Details")
    
    ## LOGOUT ##
    def logout(self):
        self.tabWidget.setCurrentIndex(0)
        
    ## ADD VEHICLE ##
    def add_vehicle(self):
        self.OWNER_NAME.setText("")
        self.VEHICLE_NAME.setText("")
        self.VEHICLE_TYPE.setCurrentIndex(0)
        self.VEHICLE_NUMBER.setText("")
        self.MOBILE_NUMBER.setText("")
        self.OWNER_NAME.text()
        self.VEHICLE_NAME.text()
        #self.VEHICLE_TYPE.text()
        self.VEHICLE_TYPE.addItem("NONE")
        self.VEHICLE_TYPE.addItem("2 Wheeler")
        self.VEHICLE_TYPE.addItem("4 Wheeler")
        self.VEHICLE_NUMBER.text()
        self.MOBILE_NUMBER.text()
        t = time.localtime()
        ot = time.strftime("%H:%M:%S",t)
        date1 = date.today()
        self.ARRIVAL_DAY.setText(str(date1))
        self.ARRIVAL_TIME.setText(str(ot))
        self.tabWidget.setCurrentIndex(2)
        
    def add(self):
        if (self.OWNER_NAME.text() == "" or self.VEHICLE_NAME.text() == "" or self.VEHICLE_TYPE.currentText() == "NONE" or self.VEHICLE_NUMBER.text() == "" or self.MOBILE_NUMBER.text() == ""):
            self.ADD_ALERT.setText("FILL DETAILS PROPERLY")
        else:
            con = sqlite3.connect("Parking.db")
            cursor = con.execute("INSERT INTO add_vehicle(vehicle_owner , vehicle_name , vehicle_type , vehicle_number , mobile_number , date , in_time , out_time) values('"+ self.OWNER_NAME.text() +"', '"+ self.VEHICLE_NAME.text() +"', '"+ self.VEHICLE_TYPE.currentText() +"', '"+ self.VEHICLE_NUMBER.text() +"', '"+ str(self.MOBILE_NUMBER.text()) +"', '"+ str(self.ARRIVAL_DAY.text()) +"', '"+ str(self.ARRIVAL_TIME.text()) +"', 'NULL')") 
            con.commit()
            con.close()
            self.ADD_ALERT.setText("ADDED SUCCESSFULLY")
        
        self.tabWidget.setCurrentIndex(2)
        self.OWNER_NAME.setText("")
        self.VEHICLE_NAME.setText("")
        self.VEHICLE_TYPE.setCurrentIndex(0)
        self.VEHICLE_NUMBER.setText("")
        self.MOBILE_NUMBER.setText("")
        self.ARRIVAL_TIME.setText("")
        self.ARRIVAL_DAY.setText("")
        t = time.localtime()
        ot = time.strftime("%H:%M:%S",t)
        date1 = date.today()
        self.ARRIVAL_DAY.setText(str(date1))
        self.ARRIVAL_TIME.setText(str(ot))
    def back1(self):
        self.tabWidget.setCurrentIndex(1)
    
    ## DISPLAY ##
    def display(self):
        self.tabWidget.setCurrentIndex(3)
        self.TABLE.setRowCount(0)
        self.TABLE.clear()
        self.TABLE.setColumnWidth(0,110)
        self.TABLE.setColumnWidth(1,110)
        self.TABLE.setColumnWidth(2,110)
        self.TABLE.setColumnWidth(3,110)
        self.TABLE.setColumnWidth(4,110)
        self.TABLE.setColumnWidth(5,110)
        con = sqlite3.connect("Parking.db")
        cursor = con.execute("SELECT * FROM add_vehicle WHERE out_time = 'NULL' ")
        result = cursor.fetchall()
        r = 0
        c = 0
        for row_number, row_data in enumerate(result):
            r += 1
            c = 0
            for column_number, data in enumerate(row_data):
                c += 1
        self.TABLE.setColumnCount(c)
        for row_number, row_data in enumerate(result):
            self.TABLE.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.TABLE.setItem(row_number,column_number,QTableWidgetItem(str(data)))
        self.TABLE.verticalHeader().setVisible(False)
        self.TABLE.horizontalHeader().setVisible(False)
    def back2(self):
        self.tabWidget.setCurrentIndex(1)
    
    ## REMOVE ##
    def remove_vehicle(self):
        self.REMOVE_NUMBER.setText("")
        self.REMOVE_OWNER_NAME.setText("")
        self.REMOVE_VEHICLE_NAME.setText("")
        self.REMOVE_VEHICLE_TYPE.setText("")
        self.REMOVE_MOBILE_NUMBER.setText("")
        self.ARRIVAL_TIME_2.setText("")
        self.REMOVAL_TIME_2.setText("")
        self.tabWidget.setCurrentIndex(4)
        self.REMOVE_NUMBER.text()
    def search(self):
        a = "" 
        b = "" 
        c = ""
        d = ""
        e = ""
        f = ""
        g = ""
        #h = ""
        t = time.localtime()
        rt = time.strftime("%H:%M:%S",t)
        con = sqlite3.connect("Parking.db")
        cursor = con.execute("SELECT * FROM add_vehicle WHERE vehicle_number = '"+ self.REMOVE_NUMBER.text() +"'")
        result = cursor.fetchall()
        if result:
            for prod in result:
                a = str(prod[0])
                b = str(prod[1])
                c = str(prod[2])
                d = str(prod[3])
                e = str(prod[4])
                f = str(prod[5])
                g = str(prod[6])
                #h = str(prod[7])
        self.REMOVE_OWNER_NAME.setText(str(a))
        self.REMOVE_VEHICLE_NAME.setText(str(b))
        self.REMOVE_VEHICLE_TYPE.setText(str(c))
        self.REMOVE_MOBILE_NUMBER.setText(str(e))
        self.ARRIVAL_TIME_2.setText(str(g))
        self.REMOVAL_TIME_2.setText(str(rt))
        
    def remove(self):
        if (self.REMOVE_NUMBER.text() == ""):
            self.REMOVE_ALERT.setText("ENTER VALID VEHICLE NUMBER")
        else:
            con = sqlite3.connect("Parking.db")
            cursor = con.execute("UPDATE add_vehicle SET out_time = '"+ self.REMOVAL_TIME_2.text() +"' WHERE vehicle_number == '"+ self.REMOVE_NUMBER.text() +"' ")
            con.commit()
            con.close()
            self.REMOVE_ALERT.setText("REMOVED SUCCESSFULLY")
        self.tabWidget.setCurrentIndex(4)
        self.REMOVE_NUMBER.setText("")
        self.REMOVE_OWNER_NAME.setText("")
        self.REMOVE_VEHICLE_NAME.setText("")
        self.REMOVE_VEHICLE_TYPE.setText("")
        self.REMOVE_MOBILE_NUMBER.setText("")
        self.ARRIVAL_TIME_2.setText("")
        self.REMOVAL_TIME_2.setText("")
        t = time.localtime()
        rt = time.strftime("%H:%M:%S",t)
        self.REMOVAL_TIME_2.setText(str(rt))

    
    ## BACK TO HOME ##
    def back(self):
        self.tabWidget.setCurrentIndex(1)
## MAIN FUNCTION ##
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

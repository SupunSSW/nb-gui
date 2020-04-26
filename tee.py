import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, QtWidgets

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="nbdatabase"
)

mycursor = mydb.cursor()


class Window(QMainWindow):
    
    def launch(self):
        Notices.setObjectName("Notices")
        Notices.resize(1030, 698)
        Notices.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(209, 209, 209);")
        

        # buttonWindow1 = QPushButton('Window1', self)
        # buttonWindow1.move(100, 100)
        # buttonWindow1.clicked.connect(self.buttonWindow_onClick)
        # self.lineEdit1 = QLineEdit("Type here what you want to transfer for [Window1].", self)
        # self.lineEdit1.setGeometry(250, 100, 400, 30)
        # self.show()

    # @pyqtSlot()
    # def buttonWindow_onClick(self):
        # self.statusBar().showMessage("Switched to window 1")
        # self.cams = Window1() 
        # self.cams.launch1()
        # ex1.launch1()
        # self.cams.show()
        # self.close()


class Window1(QMainWindow):
  
    def __init__(self, parent=None):
        super().__init__()
        self.value = -1

        self.nid = QtWidgets.QLabel('Window1', self)
        self.nid.setGeometry(QtCore.QRect(110, 20, 171, 61))
        self.nid.setObjectName("nid")

        self.dprt = QtWidgets.QLabel('Window1', self)
        self.dprt.setGeometry(QtCore.QRect(110, 50, 171, 61))
        self.dprt.setObjectName("dprt")

        self.expdt = QtWidgets.QLabel('Window1', self)
        self.expdt.setGeometry(QtCore.QRect(110, 80, 171, 61))
        self.expdt.setObjectName("expdt")

        self.tpc = QtWidgets.QLabel('Window1', self)
        self.tpc.setGeometry(QtCore.QRect(10, 140, 171, 61))
        self.tpc.setObjectName("tpc")

        self.cont = QtWidgets.QPlainTextEdit('Window1', self)
        self.cont.setGeometry(QtCore.QRect(10, 200, 510, 110))
        self.cont.setObjectName("cont")

        self.aca = QtWidgets.QLabel('Window1', self)
        self.aca.setGeometry(QtCore.QRect(110, 110, 171, 61))
        self.aca.setObjectName("aca")

        mycursor.execute("SELECT * FROM `myapp_notice`")

        myresult = mycursor.fetchall()

        self.gotdata = []

        for x in myresult:
            self.gotdata.append(x)


    def launch1(self,val=0):
        # super().__init__()
        self.title = "App"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        
        self.InitUI(val)

    def InitUI(self,val):

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)

        nid1 = QtWidgets.QLabel('Window1', self)
        nid1.setGeometry(QtCore.QRect(10, 20, 171, 61))
        nid1.setObjectName("nid1")
        nid1.setText(_translate("MainWindow", "Notice"))


        dprt1 = QtWidgets.QLabel('Window1', self)
        dprt1.setGeometry(QtCore.QRect(10, 50, 171, 61))
        dprt1.setObjectName("dprt1")
        dprt1.setText(_translate("MainWindow", "Department"))

        

        expdt1 = QtWidgets.QLabel('Window1', self)
        expdt1.setGeometry(QtCore.QRect(10, 80, 171, 61))
        expdt1.setObjectName("expdt1")
        expdt1.setText(_translate("MainWindow", "Expires on"))

        aca1 = QtWidgets.QLabel('Window1', self)
        aca1.setGeometry(QtCore.QRect(10, 110, 171, 61))
        aca1.setObjectName("aca1")
        aca1.setText(_translate("MainWindow", "Year"))

        buttonWindow1 = QPushButton('Window1', self)
        buttonWindow1.move(350, 50)
        buttonWindow1.clicked.connect(self.buttonWindow1_onClick)

        nbtn = QPushButton('Next', self)
        nbtn.move(350, 110)
        nbtn.clicked.connect(self.nbtn_click)

        bbtn = QPushButton('Back', self)
        bbtn.move(350, 170)
        bbtn.clicked.connect(self.bbtn_click)
        
        self.show()
        self.nbtn_click()

    @pyqtSlot()
    def buttonWindow1_onClick(self):
        # self.cams = Window()
        # self.cams.launch()
        self.value=-1
        ex.launch()
        # self.cams.show()
        self.close() 

    @pyqtSlot()
    def nbtn_click(self):
        if self.value < len(self.gotdata) - 1:
            self.value += 1


        _translate = QtCore.QCoreApplication.translate
        self.nid.setText(_translate("MainWindow", str(self.gotdata[self.value][0])))
        self.dprt.setText(_translate("MainWindow", str(self.gotdata[self.value][1])))
         
        self.expdt.setText(_translate("MainWindow", str(self.gotdata[self.value][2]))) 
        self.tpc.setText(_translate("MainWindow", str(self.gotdata[self.value][3]))) 
        self.cont.setPlainText(_translate("MainWindow", str(self.gotdata[self.value][4]))) 
        self.aca.setText(_translate("MainWindow", str(self.gotdata[self.value][5]))) 


    def bbtn_click(self):
        if self.value > 0:
            self.value -= 1


        _translate = QtCore.QCoreApplication.translate
        self.nid.setText(_translate("MainWindow", str(self.gotdata[self.value][0])))
        self.dprt.setText(_translate("MainWindow", str(self.gotdata[self.value][1])))
         
        self.expdt.setText(_translate("MainWindow", str(self.gotdata[self.value][2]))) 
        self.tpc.setText(_translate("MainWindow", str(self.gotdata[self.value][3]))) 
        self.cont.setPlainText(_translate("MainWindow", str(self.gotdata[self.value][4]))) 
        self.aca.setText(_translate("MainWindow", str(self.gotdata[self.value][5]))) 


if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex = Window()
    ex1 = Window1()
    ex.launch()
    # ex.buttonWindow_onClick()
    # fanfanfan()
    sys.exit(app.exec_())



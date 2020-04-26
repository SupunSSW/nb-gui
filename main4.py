
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
now = QDate.currentDate()

datetime = QDateTime.currentDateTime()
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="nbdatabase"
)

mycursor = mydb.cursor()

class Ui_Notices(object):
    def setupUi(self, Notices):
        Notices.setObjectName("Notices")
        Notices.resize(1030, 698)
        Notices.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(209, 209, 209);")
        self.lblDate = QtWidgets.QLabel(Notices)
        self.lblDate.setGeometry(QtCore.QRect(720, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblDate.setFont(font)
        self.lblDate.setText(datetime.toString())
        self.lblDate.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblDate.setAlignment(QtCore.Qt.AlignCenter)
        self.lblDate.setObjectName("lblDate")
        self.lblCurrent = QtWidgets.QLabel(Notices)
        self.lblCurrent.setGeometry(QtCore.QRect(300, 20, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lblCurrent.setFont(font)
        self.lblCurrent.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 0);")
        self.lblCurrent.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrent.setObjectName("lblCurrent")
        self.lblAvailable = QtWidgets.QLabel(Notices)
        self.lblAvailable.setGeometry(QtCore.QRect(510, 20, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lblAvailable.setFont(font)
        self.lblAvailable.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblAvailable.setAlignment(QtCore.Qt.AlignCenter)
        self.lblAvailable.setObjectName("lblAvailable")
        self.lblOutof = QtWidgets.QLabel(Notices)
        self.lblOutof.setGeometry(QtCore.QRect(360, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblOutof.setFont(font)
        self.lblOutof.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblOutof.setAlignment(QtCore.Qt.AlignCenter)
        self.lblOutof.setObjectName("lblOutof")
        self.lblDep = QtWidgets.QLabel(Notices)
        self.lblDep.setGeometry(QtCore.QRect(30, 100, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblDep.setFont(font)
        self.lblDep.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.lblDep.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblDep.setObjectName("lblDep")
        self.lblAcdyr = QtWidgets.QLabel(Notices)
        self.lblAcdyr.setGeometry(QtCore.QRect(30, 130, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblAcdyr.setFont(font)
        self.lblAcdyr.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.lblAcdyr.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblAcdyr.setObjectName("lblAcdyr")
        self.lblShowDe = QtWidgets.QLabel(Notices)
        self.lblShowDe.setGeometry(QtCore.QRect(210, 100, 691, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblShowDe.setFont(font)
        self.lblShowDe.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.lblShowDe.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblShowDe.setObjectName("lblShowDe")
        self.lblShowAcdyr = QtWidgets.QLabel(Notices)
        self.lblShowAcdyr.setGeometry(QtCore.QRect(210, 130, 691, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblShowAcdyr.setFont(font)
        self.lblShowAcdyr.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblShowAcdyr.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblShowAcdyr.setObjectName("lblShowAcdyr")
        self.lblExp = QtWidgets.QLabel(Notices)
        self.lblExp.setGeometry(QtCore.QRect(30, 160, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblExp.setFont(font)
        self.lblExp.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.lblExp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblExp.setObjectName("lblExp")
        self.lblShowExp = QtWidgets.QLabel(Notices)
        self.lblShowExp.setGeometry(QtCore.QRect(210, 160, 691, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblShowExp.setFont(font)
        self.lblShowExp.setStyleSheet("\n"
"color: rgb(255, 255, 255);")
        self.lblShowExp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lblShowExp.setObjectName("lblShowExp")
        self.lblTopic = QtWidgets.QLabel(Notices)
        self.lblTopic.setGeometry(QtCore.QRect(50, 240, 921, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblTopic.setFont(font)
        self.lblTopic.setStyleSheet("background-color: rgb(91, 91, 91);\n"
"color: rgb(255, 255, 255);")
        self.lblTopic.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTopic.setObjectName("lblTopic")
        self.lblContent = QtWidgets.QLabel(Notices)
        self.lblContent.setGeometry(QtCore.QRect(50, 290, 921, 311))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblContent.setFont(font)
        self.lblContent.setStyleSheet("background-color: rgb(91, 91, 91);\n"
"color: rgb(255, 255, 255);")
        self.lblContent.setAlignment(QtCore.Qt.AlignCenter)
        self.lblContent.setObjectName("lblContent")
        self.lblHint = QtWidgets.QLabel(Notices)
        self.lblHint.setGeometry(QtCore.QRect(180, 640, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(9)
        self.lblHint.setFont(font)
        self.lblHint.setStyleSheet("color: rgb(107, 107, 107);")
        self.lblHint.setAlignment(QtCore.Qt.AlignCenter)
        self.lblHint.setObjectName("lblHint")
        self.btnPrev = QtWidgets.QPushButton(Notices)
        self.btnPrev.setStyleSheet("background-color: rgb(107, 107, 107);")
        self.btnPrev.setGeometry(QtCore.QRect(30, 620, 261, 61))
        self.btnPrev.setText("")
        self.btnPrev.setObjectName("btnPrev")

        self.btnNext = QtWidgets.QPushButton(Notices)
        self.btnNext.setStyleSheet("background-color: rgb(107, 107, 107);")
        self.btnNext.setGeometry(QtCore.QRect(710, 620, 271, 61))
        self.btnNext.setText("")
        self.btnNext.setObjectName("btnNext")
        btnNext.clicked.connect(self.btnNext_click)

        self.show()
        self.btnNext_click()

  def btnNext_click(self):
        if self.value < len(self.gotdata) - 1:
            self.value += 1


        

        self.retranslateUi(Notices)
        QtCore.QMetaObject.connectSlotsByName(Notices)

        #  @pyqtSlot()
    def buttonWindow1_onClick(self):
        # self.cams = Window()
        # self.cams.launch()
        self.value=-1
        ex.launch()
        # self.cams.show()
        self.close() 

         #     @pyqtSlot()
    def btnNext_click(self):
        if self.value < len(self.gotdata) - 1:
            self.value += 1


        _translate = QtCore.QCoreApplication.translate
        self.lblCurrent.setText(_translate("MainWindow", str(self.gotdata[self.value][0])))
        self.lblShowDe.setText(_translate("MainWindow", str(self.gotdata[self.value][1])))
        self.lblShowExp.setText(_translate("MainWindow", str(self.gotdata[self.value][2]))) 
        self.lblTopic.setText(_translate("MainWindow", str(self.gotdata[self.value][3]))) 
        self.lblContent.setPlainText(_translate("MainWindow", str(self.gotdata[self.value][4]))) 
        self.lblShowAcdyr.setText(_translate("MainWindow", str(self.gotdata[self.value][5]))) 


    def btnPrev_click(self):
        if self.value > 0:
            self.value -= 1


        _translate = QtCore.QCoreApplication.translate
        self.lblCurrent.setText(_translate("MainWindow", str(self.gotdata[self.value][0])))
        self.lblShowDe.setText(_translate("MainWindow", str(self.gotdata[self.value][1])))
        self.lblShowExp.setText(_translate("MainWindow", str(self.gotdata[self.value][2]))) 
        self.lblTopic.setText(_translate("MainWindow", str(self.gotdata[self.value][3]))) 
        self.lblContent.setPlainText(_translate("MainWindow", str(self.gotdata[self.value][4]))) 
        self.lblShowAcdyr.setText(_translate("MainWindow", str(self.gotdata[self.value][5]))) 

    def retranslateUi(self, Notices):
        _translate = QtCore.QCoreApplication.translate
        Notices.setWindowTitle(_translate("Notices", "Smart notice Board"))
        
        self.lblCurrent.setText(_translate("Notices", "01"))
        self.lblAvailable.setText(_translate("Notices", "05"))
        self.lblOutof.setText(_translate("Notices", "Out Of"))
        self.lblDep.setText(_translate("Notices", "Department     :"))
        self.lblAcdyr.setText(_translate("Notices", "Academic Year  :"))
        self.lblShowDe.setText(_translate("Notices", "Department of Computing"))
        self.lblShowAcdyr.setText(_translate("Notices", "Third Year"))
        self.lblExp.setText(_translate("Notices", "Expire Date      :"))
        self.lblShowExp.setText(_translate("Notices", "30/04/2020"))
        self.lblTopic.setText(_translate("Notices", "Evaluation Remaining On Group Project"))
        self.lblContent.setText(_translate("Notices", "The remaining evalution components of the project has been displyed in the LMS course.\n Deadline for dissertation will be on 23rd on April."))
        self.lblHint.setText(_translate("Notices", "Use hand gestures to navigate between notices"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Notices = QtWidgets.QDialog()
    ui = Ui_Notices()
    ui.setupUi(Notices)
    Notices.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uides.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 783)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nid = QtWidgets.QLabel(self.centralwidget)
        self.nid.setGeometry(QtCore.QRect(10, 20, 171, 61))
        self.nid.setObjectName("nid")
        self.dprt = QtWidgets.QLabel(self.centralwidget)
        self.dprt.setGeometry(QtCore.QRect(10, 120, 191, 31))
        self.dprt.setObjectName("dprt")
        self.expdt = QtWidgets.QLabel(self.centralwidget)
        self.expdt.setGeometry(QtCore.QRect(10, 170, 221, 16))
        self.expdt.setObjectName("expdt")
        self.tpc = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.tpc.setGeometry(QtCore.QRect(20, 280, 991, 91))
        self.tpc.setObjectName("tpc")
        self.cont = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cont.setGeometry(QtCore.QRect(20, 390, 991, 341))
        self.cont.setObjectName("cont")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 240, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nid.setText(_translate("MainWindow", "Notice"))
        self.dprt.setText(_translate("MainWindow", "Department"))
        self.expdt.setText(_translate("MainWindow", "Expires on"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

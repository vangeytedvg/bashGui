# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmMain(object):
    def setupUi(self, frmMain):
        frmMain.setObjectName("frmMain")
        frmMain.resize(342, 234)
        self.centralwidget = QtWidgets.QWidget(frmMain)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 131, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 60, 131, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        frmMain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(frmMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 30))
        self.menubar.setObjectName("menubar")
        frmMain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(frmMain)
        self.statusbar.setObjectName("statusbar")
        frmMain.setStatusBar(self.statusbar)

        self.retranslateUi(frmMain)
        QtCore.QMetaObject.connectSlotsByName(frmMain)

    def retranslateUi(self, frmMain):
        _translate = QtCore.QCoreApplication.translate
        frmMain.setWindowTitle(_translate("frmMain", "MainWindow"))
        self.pushButton.setText(_translate("frmMain", "Hello World 1"))
        self.pushButton_2.setText(_translate("frmMain", "Hello World 2"))

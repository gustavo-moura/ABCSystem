# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'overview.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuUsu_rio = QtWidgets.QMenu(self.menubar)
        self.menuUsu_rio.setObjectName("menuUsu_rio")
        self.menuSimula_es = QtWidgets.QMenu(self.menubar)
        self.menuSimula_es.setObjectName("menuSimula_es")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.menuUsu_rio.addAction(self.actionSair)
        self.menubar.addAction(self.menuUsu_rio.menuAction())
        self.menubar.addAction(self.menuSimula_es.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABC System"))
        self.menuUsu_rio.setTitle(_translate("MainWindow", "Usuário"))
        self.menuSimula_es.setTitle(_translate("MainWindow", "Simulações"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))


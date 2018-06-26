# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from overview import Ui_MainWindow
from queries2 import connection

#funcao para verificar se usuario e senha correspondem
def autentica(username, password):
    if username==password:
        return True
    else:
        return False


class Ui_Dialog(object):

    #Funcao utilizada para realizar a autenticacao do usuario no banco
    def login(self):

        #connection.connect()
    
        user = self.in_user.text()
        pwd = self.in_senha.text()

        autenticacao = connection.checkLogin(user, pwd)

        if autenticacao:
            print("User found")

            # abrir janela principal
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.window)
            self.window.show()

        else:
            print("User not found")



       
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 268)
        self.in_user = QtWidgets.QLineEdit(Dialog)
        self.in_user.setGeometry(QtCore.QRect(170, 100, 113, 20))
        self.in_user.setObjectName("in_user")
        self.in_senha = QtWidgets.QLineEdit(Dialog)
        self.in_senha.setGeometry(QtCore.QRect(170, 130, 113, 20))
        self.in_senha.setObjectName("in_senha")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 90, 47, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 130, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 200, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.logar = QtWidgets.QPushButton(Dialog)
        self.logar.setGeometry(QtCore.QRect(30, 200, 75, 23))
        self.logar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.logar.setObjectName("logar")

        self.logar.clicked.connect(self.login)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ABC System"))
        self.label.setText(_translate("Dialog", "Login:"))
        self.label_2.setText(_translate("Dialog", "Senha:"))
        self.label_3.setText(_translate("Dialog", "ABC System"))


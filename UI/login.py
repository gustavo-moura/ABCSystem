# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from overview import Ui_MainWindow
from queries2 import connection


class Ui_Dialog(object):

    #Funcao utilizada para realizar a autenticacao do usuario no banco
    def login(self):

        self.lb_mensagem.setText("")

        user = self.in_user.text()
        pwd = self.in_senha.text()

        tipoUser = connection.checkLogin(user, pwd)
        

        if (tipoUser == 1) or (tipoUser == 2) or (tipoUser == 3):
            print("User found")

            # abrir janela principal
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.user = user
            self.ui.tipoUser = tipoUser
            self.ui.setupUi(self.window)
            self.window.show()

        elif tipoUser == 4:
            self.lb_mensagem.setText("Este usuário não tem acesso ao sistema")
            print("User without system access")

        else:
            self.lb_mensagem.setText("Usuário ou senha incorretos")
            print("User not found")


        

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 268)
        self.in_user = QtWidgets.QLineEdit(Dialog)
        self.in_user.setGeometry(QtCore.QRect(180, 100, 113, 20))
        self.in_user.setObjectName("in_user")
        self.in_senha = QtWidgets.QLineEdit(Dialog)
        self.in_senha.setGeometry(QtCore.QRect(180, 130, 113, 20))
        self.in_senha.setObjectName("in_senha")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(130, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.logar = QtWidgets.QPushButton(Dialog)
        self.logar.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.logar.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.logar.setObjectName("logar")
        self.lb_mensagem = QtWidgets.QLabel(Dialog)
        self.lb_mensagem.setGeometry(QtCore.QRect(100, 150, 231, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lb_mensagem.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.lb_mensagem.setFont(font)
        self.lb_mensagem.setObjectName("lb_mensagem")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # custom
        self.logar.clicked.connect(self.login)
        self.lb_mensagem.setText("")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ABC System - Bem Vindo"))
        self.label.setText(_translate("Dialog", "Usuário:"))
        self.label_2.setText(_translate("Dialog", "Senha:"))
        self.label_3.setText(_translate("Dialog", "ABC System"))
        self.logar.setText(_translate("Dialog", "Conectar"))
        self.lb_mensagem.setText(_translate("Dialog", "Alguma mensagem para usuário"))


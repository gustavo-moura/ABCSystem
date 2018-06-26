# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'overview.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    id_relatorio = 0
    tipoUser = 3
    user = ""

    # Determina o que cada tipo de usuário pode visualizar
    def checkPermissoes(self):
        if self.tipoUser == 1:
            self.widget.close()
            self.actionR1.setEnabled(False)
            self.actionR2.setEnabled(False)
            self.actionR3.setEnabled(False)
            self.actionR4.setEnabled(False)
            self.actionR5.setEnabled(True)   #
            self.actionR6.setEnabled(True)   #
            self.actionR7.setEnabled(False)
            self.menuSim.setEnabled(False)


        elif self.tipoUser == 2:
            self.widget.close()
            self.actionR1.setEnabled(False)
            self.actionR2.setEnabled(False)
            self.actionR3.setEnabled(False)
            self.actionR4.setEnabled(False)
            self.actionR5.setEnabled(True)   #
            self.actionR6.setEnabled(True)   #
            self.actionR7.setEnabled(False)
            self.menuSim.setEnabled(True)    #

        elif self.tipoUser == 3:
            # Tem acesso a tudo
            self.actionR1.setEnabled(True)
            self.actionR2.setEnabled(True)
            self.actionR3.setEnabled(True)
            self.actionR4.setEnabled(True)
            self.actionR5.setEnabled(True)   #
            self.actionR6.setEnabled(True)   #
            self.actionR7.setEnabled(True)
            self.menuSim.setEnabled(True)


    # Define o que cada botão da interface executa
    def settriggers(self):
        self.widget_relatorio.close()

        self.actionR1.triggered.connect(self.click_actionR1)
        self.actionR2.triggered.connect(self.click_actionR2)
        self.actionR3.triggered.connect(self.click_actionR3)
        self.actionR4.triggered.connect(self.click_actionR4)
        self.actionR5.triggered.connect(self.click_actionR5)
        self.actionR6.triggered.connect(self.click_actionR6)
        self.actionR7.triggered.connect(self.click_actionR7)
        self.actionS1.triggered.connect(self.click_actionS1)
        self.actionS2.triggered.connect(self.click_actionS2)
        self.actionS3.triggered.connect(self.click_actionS3)

        self.lb_nomeuser.setText(self.user)
        self.lb_tipouser.setText(str(self.tipoUser))



    # ################# OVERVIEW
    def populaOverview(self):
        self.pop_top15()



    def pop_top15(self):
        self.tabledata = [[1234567890,2,3,4,5],
                          [6,7,8,9,10],
                          [11,12,13,14,15],
                          [16,17,18,19,20]]
        header = ['col_0', 'col_1', 'col_2', 'col_3', 'col_4']
        tablemodel = MyTableModel(self.tabledata, header, self)
        self.tb_3.setModel(tablemodel)
        vh = self.tb_3.verticalHeader()
        vh.setVisible(False)
        hh = self.tb_3.horizontalHeader()
        hh.setStretchLastSection(True)
        self.tb_3.resizeColumnsToContents()
        self.tb_3.resizeRowsToContents()



    # ################# CLICK

    # Standard para criação de relatório
    def criaRelatorio(self, id, titulo):
        self.widget.close()
        self.widget_relatorio.show()
        id_relatorio = id
        self.lb_titulo.setText(titulo)

    # Standard para criação de simulacao
    def criaRelatorio(self, id, titulo):
        self.widget.close()
        self.widget_relatorio.show()
        id_relatorio = id
        self.lb_titulo.setText(titulo)


    def click_actionR1(self, MainWindow):
        self.criaRelatorio(1, "Clientes com Cartões Vencidos")

    def click_actionR2(self, MainWindow):
        self.criaRelatorio(2, "Histórico de Departamento de Funcionários")

    def click_actionR3(self, MainWindow):
        self.criaRelatorio(3, "Dados de frete")

    def click_actionR4(self, MainWindow):
        self.criaRelatorio(4, "Informações das vendas anuais")

    def click_actionR5(self, MainWindow):
        self.criaRelatorio(5, "Top 15 produtos vendidos no semestre")

    def click_actionR6(self, MainWindow):
        self.criaRelatorio(6, "Produtos de vendas casadas")

    def click_actionR7(self, MainWindow):
        self.criaRelatorio(7, "Vendas por país")

    def click_actionS1(self, MainWindow):
        a=0

    def click_actionS2(self, MainWindow):
        a=0

    def click_actionS3(self, MainWindow):
        a=0



    # Chama funções ao final da construçao da interface
    def chamaFuncoes(self):
        self.settriggers()
        self.checkPermissoes()
        self.populaOverview()



    # ######### CONSTRUÇÃO DA INTERFACE

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1053, 1233)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lb_nomeuser = QtWidgets.QLabel(self.centralwidget)
        self.lb_nomeuser.setGeometry(QtCore.QRect(160, 10, 861, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.lb_nomeuser.setFont(font)
        self.lb_nomeuser.setObjectName("lb_nomeuser")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lb_tipouser = QtWidgets.QLabel(self.centralwidget)
        self.lb_tipouser.setGeometry(QtCore.QRect(50, 10, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.lb_tipouser.setFont(font)
        self.lb_tipouser.setObjectName("lb_tipouser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(40, 40, 1041, 611))
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1021, 591))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 261, 121))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(110, 60, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(190, 60, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.in_1_data = QtWidgets.QDateEdit(self.groupBox)
        self.in_1_data.setGeometry(QtCore.QRect(149, 20, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.in_1_data.setFont(font)
        self.in_1_data.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 21), QtCore.QTime(0, 0, 0)))
        self.in_1_data.setCalendarPopup(True)
        self.in_1_data.setObjectName("in_1_data")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lb_1_dia = QtWidgets.QLabel(self.groupBox)
        self.lb_1_dia.setGeometry(QtCore.QRect(30, 90, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lb_1_dia.setFont(font)
        self.lb_1_dia.setObjectName("lb_1_dia")
        self.lb_1_mes = QtWidgets.QLabel(self.groupBox)
        self.lb_1_mes.setGeometry(QtCore.QRect(110, 90, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lb_1_mes.setFont(font)
        self.lb_1_mes.setObjectName("lb_1_mes")
        self.lb_1_ano = QtWidgets.QLabel(self.groupBox)
        self.lb_1_ano.setGeometry(QtCore.QRect(190, 90, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lb_1_ano.setFont(font)
        self.lb_1_ano.setObjectName("lb_1_ano")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 261, 201))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(50, 60, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(180, 60, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.in_2_data = QtWidgets.QDateEdit(self.groupBox_2)
        self.in_2_data.setGeometry(QtCore.QRect(169, 20, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.in_2_data.setFont(font)
        self.in_2_data.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 21), QtCore.QTime(0, 0, 0)))
        self.in_2_data.setCalendarPopup(True)
        self.in_2_data.setObjectName("in_2_data")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(50, 20, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.lb_2_m1 = QtWidgets.QLabel(self.groupBox_2)
        self.lb_2_m1.setGeometry(QtCore.QRect(50, 90, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lb_2_m1.setFont(font)
        self.lb_2_m1.setObjectName("lb_2_m1")
        self.lb_2_a1 = QtWidgets.QLabel(self.groupBox_2)
        self.lb_2_a1.setGeometry(QtCore.QRect(180, 90, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lb_2_a1.setFont(font)
        self.lb_2_a1.setObjectName("lb_2_a1")
        self.lb_2_m2 = QtWidgets.QLabel(self.groupBox_2)
        self.lb_2_m2.setGeometry(QtCore.QRect(50, 120, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lb_2_m2.setFont(font)
        self.lb_2_m2.setObjectName("lb_2_m2")
        self.lb_2_m3 = QtWidgets.QLabel(self.groupBox_2)
        self.lb_2_m3.setGeometry(QtCore.QRect(50, 150, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lb_2_m3.setFont(font)
        self.lb_2_m3.setObjectName("lb_2_m3")
        self.lb_2_a2 = QtWidgets.QLabel(self.groupBox_2)
        self.lb_2_a2.setGeometry(QtCore.QRect(180, 120, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lb_2_a2.setFont(font)
        self.lb_2_a2.setObjectName("lb_2_a2")
        self.lb_2_a3 = QtWidgets.QLabel(self.groupBox_2)
        self.lb_2_a3.setGeometry(QtCore.QRect(180, 150, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.lb_2_a3.setFont(font)
        self.lb_2_a3.setObjectName("lb_2_a3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 10, 261, 331))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.tb_3 = QtWidgets.QTableView(self.groupBox_3)
        self.tb_3.setGeometry(QtCore.QRect(10, 21, 241, 301))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tb_3.setFont(font)
        self.tb_3.setObjectName("tb_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 350, 261, 231))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.tb_4 = QtWidgets.QTableView(self.groupBox_4)
        self.tb_4.setGeometry(QtCore.QRect(10, 50, 241, 171))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tb_4.setFont(font)
        self.tb_4.setObjectName("tb_4")
        self.in_4_data = QtWidgets.QDateEdit(self.groupBox_4)
        self.in_4_data.setGeometry(QtCore.QRect(190, 20, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.in_4_data.setFont(font)
        self.in_4_data.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 21), QtCore.QTime(0, 0, 0)))
        self.in_4_data.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.in_4_data.setCalendarPopup(True)
        self.in_4_data.setObjectName("in_4_data")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(71, 20, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(280, 350, 261, 231))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.tb_5 = QtWidgets.QTableView(self.groupBox_5)
        self.tb_5.setGeometry(QtCore.QRect(10, 50, 241, 171))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tb_5.setFont(font)
        self.tb_5.setObjectName("tb_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_6.setGeometry(QtCore.QRect(550, 10, 261, 151))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.tb_6 = QtWidgets.QTableView(self.groupBox_6)
        self.tb_6.setGeometry(QtCore.QRect(10, 21, 241, 121))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.tb_6.setFont(font)
        self.tb_6.setObjectName("tb_6")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_7.setGeometry(QtCore.QRect(550, 170, 461, 201))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_16 = QtWidgets.QLabel(self.groupBox_7)
        self.label_16.setGeometry(QtCore.QRect(250, 20, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.in_7_data = QtWidgets.QDateEdit(self.groupBox_7)
        self.in_7_data.setGeometry(QtCore.QRect(369, 20, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.in_7_data.setFont(font)
        self.in_7_data.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 21), QtCore.QTime(0, 0, 0)))
        self.in_7_data.setCalendarPopup(True)
        self.in_7_data.setObjectName("in_7_data")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_8.setGeometry(QtCore.QRect(550, 380, 461, 201))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setObjectName("groupBox_8")
        self.in_8_data = QtWidgets.QDateEdit(self.groupBox_8)
        self.in_8_data.setGeometry(QtCore.QRect(389, 20, 61, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.in_8_data.setFont(font)
        self.in_8_data.setDateTime(QtCore.QDateTime(QtCore.QDate(2018, 6, 21), QtCore.QTime(0, 0, 0)))
        self.in_8_data.setCurrentSection(QtWidgets.QDateTimeEdit.YearSection)
        self.in_8_data.setCalendarPopup(True)
        self.in_8_data.setObjectName("in_8_data")
        self.label_15 = QtWidgets.QLabel(self.groupBox_8)
        self.label_15.setGeometry(QtCore.QRect(270, 20, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.widget_relatorio = QtWidgets.QWidget(self.centralwidget)
        self.widget_relatorio.setEnabled(True)
        self.widget_relatorio.setGeometry(QtCore.QRect(10, 40, 831, 491))
        self.widget_relatorio.setObjectName("widget_relatorio")
        self.tb_relatorio = QtWidgets.QTableView(self.widget_relatorio)
        self.tb_relatorio.setGeometry(QtCore.QRect(20, 80, 681, 301))
        self.tb_relatorio.setSortingEnabled(False)
        self.tb_relatorio.setObjectName("tb_relatorio")
        self.in_pesquisa = QtWidgets.QLineEdit(self.widget_relatorio)
        self.in_pesquisa.setGeometry(QtCore.QRect(20, 50, 181, 20))
        self.in_pesquisa.setObjectName("in_pesquisa")
        self.pesquisar = QtWidgets.QPushButton(self.widget_relatorio)
        self.pesquisar.setGeometry(QtCore.QRect(210, 50, 75, 23))
        self.pesquisar.setObjectName("pesquisar")
        self.lb_titulo = QtWidgets.QLabel(self.widget_relatorio)
        self.lb_titulo.setGeometry(QtCore.QRect(20, 20, 681, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.lb_titulo.setFont(font)
        self.lb_titulo.setObjectName("lb_titulo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 21))
        self.menubar.setObjectName("menubar")
        self.menuUser = QtWidgets.QMenu(self.menubar)
        self.menuUser.setObjectName("menuUser")
        self.menuSim = QtWidgets.QMenu(self.menubar)
        self.menuSim.setObjectName("menuSim")
        self.menuRel = QtWidgets.QMenu(self.menubar)
        self.menuRel.setObjectName("menuRel")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSair = QtWidgets.QAction(MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionR1 = QtWidgets.QAction(MainWindow)
        self.actionR1.setObjectName("actionR1")
        self.actionR2 = QtWidgets.QAction(MainWindow)
        self.actionR2.setObjectName("actionR2")
        self.actionR3 = QtWidgets.QAction(MainWindow)
        self.actionR3.setObjectName("actionR3")
        self.actionR4 = QtWidgets.QAction(MainWindow)
        self.actionR4.setObjectName("actionR4")
        self.actionR5 = QtWidgets.QAction(MainWindow)
        self.actionR5.setObjectName("actionR5")
        self.actionR6 = QtWidgets.QAction(MainWindow)
        self.actionR6.setObjectName("actionR6")
        self.actionR7 = QtWidgets.QAction(MainWindow)
        self.actionR7.setObjectName("actionR7")
        self.actionS1 = QtWidgets.QAction(MainWindow)
        self.actionS1.setObjectName("actionS1")
        self.actionS2 = QtWidgets.QAction(MainWindow)
        self.actionS2.setObjectName("actionS2")
        self.actionS3 = QtWidgets.QAction(MainWindow)
        self.actionS3.setObjectName("actionS3")
        self.actionCr_ditos = QtWidgets.QAction(MainWindow)
        self.actionCr_ditos.setObjectName("actionCr_ditos")
        self.menuUser.addAction(self.actionSair)
        self.menuUser.addSeparator()
        self.menuUser.addAction(self.actionCr_ditos)
        self.menuSim.addAction(self.actionS1)
        self.menuSim.addAction(self.actionS2)
        self.menuSim.addAction(self.actionS3)
        self.menuRel.addAction(self.actionR1)
        self.menuRel.addAction(self.actionR2)
        self.menuRel.addAction(self.actionR3)
        self.menuRel.addAction(self.actionR4)
        self.menuRel.addAction(self.actionR5)
        self.menuRel.addAction(self.actionR6)
        self.menuRel.addAction(self.actionR7)
        self.menubar.addAction(self.menuUser.menuAction())
        self.menubar.addAction(self.menuRel.menuAction())
        self.menubar.addAction(self.menuSim.menuAction())
        self.label_6.setBuddy(self.in_1_data)
        self.label_13.setBuddy(self.in_2_data)
        self.label_14.setBuddy(self.in_4_data)
        self.label_16.setBuddy(self.in_7_data)
        self.label_15.setBuddy(self.in_8_data)
        self.lb_titulo.setBuddy(self.in_1_data)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.in_1_data, self.in_2_data)
        MainWindow.setTabOrder(self.in_2_data, self.tb_3)
        MainWindow.setTabOrder(self.tb_3, self.in_4_data)
        MainWindow.setTabOrder(self.in_4_data, self.tb_4)
        MainWindow.setTabOrder(self.tb_4, self.tb_5)
        MainWindow.setTabOrder(self.tb_5, self.tb_6)
        MainWindow.setTabOrder(self.tb_6, self.in_7_data)
        MainWindow.setTabOrder(self.in_7_data, self.in_8_data)

        self.chamaFuncoes()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ABC System"))
        self.label.setText(_translate("MainWindow", "Usuário:"))
        self.lb_nomeuser.setText(_translate("MainWindow", "John Doe"))
        self.label_3.setText(_translate("MainWindow", "Tipo:"))
        self.lb_tipouser.setText(_translate("MainWindow", "3"))
        self.groupBox.setTitle(_translate("MainWindow", "Total Vendido"))
        self.label_2.setText(_translate("MainWindow", "Dia"))
        self.label_4.setText(_translate("MainWindow", "Mês"))
        self.label_5.setText(_translate("MainWindow", "Ano"))
        self.label_6.setText(_translate("MainWindow", "Selecione o período:"))
        self.lb_1_dia.setText(_translate("MainWindow", "99999"))
        self.lb_1_mes.setText(_translate("MainWindow", "99999"))
        self.lb_1_ano.setText(_translate("MainWindow", "99999"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Top 3 Funcionários"))
        self.label_11.setText(_translate("MainWindow", "Mês"))
        self.label_12.setText(_translate("MainWindow", "Ano"))
        self.in_2_data.setDisplayFormat(_translate("MainWindow", "MM/yyyy"))
        self.label_13.setText(_translate("MainWindow", "Selecione o período:"))
        self.lb_2_m1.setText(_translate("MainWindow", "Jair"))
        self.lb_2_a1.setText(_translate("MainWindow", "Nair"))
        self.lb_2_m2.setText(_translate("MainWindow", "Jaer"))
        self.lb_2_m3.setText(_translate("MainWindow", "Jaur"))
        self.lb_2_a2.setText(_translate("MainWindow", "Neir"))
        self.lb_2_a3.setText(_translate("MainWindow", "Noir"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Top 15 Produtos Mais Vendidos"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Melhores clientes do Ano"))
        self.in_4_data.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.label_14.setText(_translate("MainWindow", "Selecione o período:"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Melhores clientes Ever"))
        self.groupBox_6.setTitle(_translate("MainWindow", "!!! Produtos acabando !!!"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Total Vendido por Mês"))
        self.label_16.setText(_translate("MainWindow", "Selecione o período:"))
        self.in_7_data.setDisplayFormat(_translate("MainWindow", "MM/yyyy"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Total Vendido por Ano"))
        self.in_8_data.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.label_15.setText(_translate("MainWindow", "Selecione o período:"))
        self.pesquisar.setText(_translate("MainWindow", "Pesquisar"))
        self.lb_titulo.setText(_translate("MainWindow", "Relatório Bla bla bla"))
        self.menuUser.setTitle(_translate("MainWindow", "Usuário"))
        self.menuSim.setTitle(_translate("MainWindow", "Simulações"))
        self.menuRel.setTitle(_translate("MainWindow", "Relatórios"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionR1.setText(_translate("MainWindow", "R1 - Clientes com cartões vencidos"))
        self.actionR2.setText(_translate("MainWindow", "R2 - Histórico de departamento de funcionários"))
        self.actionR3.setText(_translate("MainWindow", "R3 - Dados de frete"))
        self.actionR4.setText(_translate("MainWindow", "R4 - Informações das vendas anuais"))
        self.actionR5.setText(_translate("MainWindow", "R5 - Top 15 produtos vendidos no semestre"))
        self.actionR6.setText(_translate("MainWindow", "R6 - Produtos de vendas casadas"))
        self.actionR7.setText(_translate("MainWindow", "R7 - Vendas por país"))
        self.actionS1.setText(_translate("MainWindow", "S1 - Produtos"))
        self.actionS2.setText(_translate("MainWindow", "S2 - Subcategoria"))
        self.actionS3.setText(_translate("MainWindow", "S3 - Venda"))
        self.actionCr_ditos.setText(_translate("MainWindow", "Créditos"))


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None):
        """
        Args:
            datain: a list of lists\n
            headerdata: a list of strings
        """
        QAbstractTableModel.__init__(self, None)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        if len(self.arraydata) > 0: 
            return len(self.arraydata[0]) 
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def setData(self, index, value, role):
        pass         # not sure what to put here

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()

    def sort(self, Ncol, order):
        """
        Sort table by given column number.
        """
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=operator.itemgetter(Ncol))       
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))
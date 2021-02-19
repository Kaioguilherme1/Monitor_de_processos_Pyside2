# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Monitor_processos_IUEwwIoF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 593)
        MainWindow.setMinimumSize(QSize(800, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.backgrund = QFrame(self.centralwidget)
        self.backgrund.setObjectName(u"backgrund")
        self.backgrund.setStyleSheet(u"background-color:  #131B1F;")
        self.backgrund.setFrameShape(QFrame.NoFrame)
        self.backgrund.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.backgrund)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.backgrund)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 40))
        self.top.setMaximumSize(QSize(16777215, 40))
        self.top.setStyleSheet(u"background-color: #38393B;")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Title = QFrame(self.top)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(0, 40))
        self.Title.setMaximumSize(QSize(16777215, 40))
        self.Title.setStyleSheet(u"background-color: #38393B;")
        self.Title.setFrameShape(QFrame.StyledPanel)
        self.Title.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.Title)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Titulo = QLabel(self.Title)
        self.Titulo.setObjectName(u"Titulo")
        font = QFont()
        font.setFamily(u"Lucida Sans Unicode")
        font.setPointSize(20)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet(u"color: #47ACDE;")

        self.gridLayout_2.addWidget(self.Titulo, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.Title)

        self.top_bts = QFrame(self.top)
        self.top_bts.setObjectName(u"top_bts")
        self.top_bts.setMinimumSize(QSize(0, 40))
        self.top_bts.setMaximumSize(QSize(100, 40))
        self.top_bts.setStyleSheet(u"background-color: #38393B;")
        self.top_bts.setFrameShape(QFrame.NoFrame)
        self.top_bts.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_bts)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bts_minimize = QPushButton(self.top_bts)
        self.bts_minimize.setObjectName(u"bts_minimize")
        self.bts_minimize.setMinimumSize(QSize(20, 20))
        self.bts_minimize.setMaximumSize(QSize(20, 20))
        self.bts_minimize.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.bts_minimize.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"	background-color: #05F29B;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(56, 57, 59);\n"
"    }")
        self.bts_minimize.setIconSize(QSize(8, 8))

        self.horizontalLayout_2.addWidget(self.bts_minimize)

        self.bts_maximize = QPushButton(self.top_bts)
        self.bts_maximize.setObjectName(u"bts_maximize")
        self.bts_maximize.setMinimumSize(QSize(20, 20))
        self.bts_maximize.setMaximumSize(QSize(20, 20))
        self.bts_maximize.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.bts_maximize.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"	background-color: #F2FF05;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(56, 57, 59);\n"
"    }")
        self.bts_maximize.setIconSize(QSize(8, 8))

        self.horizontalLayout_2.addWidget(self.bts_maximize)

        self.bts_close = QPushButton(self.top_bts)
        self.bts_close.setObjectName(u"bts_close")
        self.bts_close.setMinimumSize(QSize(20, 20))
        self.bts_close.setMaximumSize(QSize(20, 20))
        self.bts_close.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.bts_close.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"	background-color: #D11D26;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(56, 57, 59);\n"
"    }")
        self.bts_close.setIconSize(QSize(8, 8))

        self.horizontalLayout_2.addWidget(self.bts_close)


        self.horizontalLayout.addWidget(self.top_bts)


        self.verticalLayout_2.addWidget(self.top)

        self.Home_page = QStackedWidget(self.backgrund)
        self.Home_page.setObjectName(u"Home_page")
        self.Home_page.setStyleSheet(u"backgroud: none;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_12 = QVBoxLayout(self.page_home)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_center = QFrame(self.page_home)
        self.frame_center.setObjectName(u"frame_center")
        self.frame_center.setMinimumSize(QSize(700, 400))
        self.frame_center.setMaximumSize(QSize(900, 600))
        self.frame_center.setFrameShape(QFrame.StyledPanel)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Frame_Cpu = QFrame(self.frame_center)
        self.Frame_Cpu.setObjectName(u"Frame_Cpu")
        self.Frame_Cpu.setMinimumSize(QSize(250, 400))
        self.Frame_Cpu.setMaximumSize(QSize(200, 350))
        self.Frame_Cpu.setStyleSheet(u"QFrame {\n"
"	background:  none;	\n"
"	\n"
"\n"
"    }\n"
"")
        self.Frame_Cpu.setFrameShape(QFrame.NoFrame)
        self.Frame_Cpu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Frame_Cpu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.progres_fund_cpu = QFrame(self.Frame_Cpu)
        self.progres_fund_cpu.setObjectName(u"progres_fund_cpu")
        self.progres_fund_cpu.setMinimumSize(QSize(250, 250))
        self.progres_fund_cpu.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 125px;\n"
"	background-color: rgba(85, 170, 255, 0.10);\n"
"}")
        self.progres_fund_cpu.setFrameShape(QFrame.StyledPanel)
        self.progres_fund_cpu.setFrameShadow(QFrame.Raised)
        self.Porcent_circle_cpu = QFrame(self.progres_fund_cpu)
        self.Porcent_circle_cpu.setObjectName(u"Porcent_circle_cpu")
        self.Porcent_circle_cpu.setGeometry(QRect(0, 0, 250, 250))
        self.Porcent_circle_cpu.setMinimumSize(QSize(250, 250))
        self.Porcent_circle_cpu.setMaximumSize(QSize(250, 250))
        self.Porcent_circle_cpu.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 125px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.749 rgba(170, 0, 255, 0), stop:0.75 rgba(242, 255, 5, 255));\n"
"}")
        self.Porcent_circle_cpu.setFrameShape(QFrame.StyledPanel)
        self.Porcent_circle_cpu.setFrameShadow(QFrame.Raised)
        self.cicler = QFrame(self.Porcent_circle_cpu)
        self.cicler.setObjectName(u"cicler")
        self.cicler.setGeometry(QRect(10, 10, 230, 230))
        self.cicler.setMinimumSize(QSize(230, 230))
        self.cicler.setMaximumSize(QSize(230, 230))
        self.cicler.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 115px;\n"
"	background-color: #131B1F;\n"
"}\n"
"QFrame:hover{\n"
"	background:  #38393B;\n"
"}")
        self.cicler.setFrameShape(QFrame.StyledPanel)
        self.cicler.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.cicler)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.cicler)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(20)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background-color: none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.Vcpu_usage = QLabel(self.cicler)
        self.Vcpu_usage.setObjectName(u"Vcpu_usage")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(26)
        self.Vcpu_usage.setFont(font2)
        self.Vcpu_usage.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background-color: none;")
        self.Vcpu_usage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.Vcpu_usage)

        self.label_3 = QLabel(self.cicler)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(11)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background-color: none;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)


        self.verticalLayout_3.addWidget(self.progres_fund_cpu)

        self.FDados = QFrame(self.Frame_Cpu)
        self.FDados.setObjectName(u"FDados")
        self.FDados.setEnabled(True)
        self.FDados.setMinimumSize(QSize(200, 100))
        self.FDados.setMaximumSize(QSize(200, 170))
        self.FDados.setStyleSheet(u"QFrame{\n"
"	background: none;\n"
"}")
        self.FDados.setFrameShape(QFrame.StyledPanel)
        self.FDados.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.FDados)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FDesquedo = QFrame(self.FDados)
        self.FDesquedo.setObjectName(u"FDesquedo")
        self.FDesquedo.setMinimumSize(QSize(90, 0))
        self.FDesquedo.setStyleSheet(u"background: none;\n"
"border: none;")
        self.FDesquedo.setFrameShape(QFrame.StyledPanel)
        self.FDesquedo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.FDesquedo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.FDesquedo)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.FDesquedo)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.label_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.label_6 = QLabel(self.FDesquedo)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")

        self.verticalLayout_4.addWidget(self.label_6)


        self.horizontalLayout_3.addWidget(self.FDesquedo)

        self.FDdireito = QFrame(self.FDados)
        self.FDdireito.setObjectName(u"FDdireito")
        self.FDdireito.setMinimumSize(QSize(80, 50))
        self.FDdireito.setMaximumSize(QSize(90, 16777215))
        self.FDdireito.setStyleSheet(u"background: none;\n"
"border: none;")
        self.FDdireito.setFrameShape(QFrame.StyledPanel)
        self.FDdireito.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.FDdireito)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.Vcpu_freq = QLabel(self.FDdireito)
        self.Vcpu_freq.setObjectName(u"Vcpu_freq")
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(10)
        self.Vcpu_freq.setFont(font4)
        self.Vcpu_freq.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.Vcpu_freq.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.Vcpu_freq)

        self.Vcpu_freqMax = QLabel(self.FDdireito)
        self.Vcpu_freqMax.setObjectName(u"Vcpu_freqMax")
        self.Vcpu_freqMax.setFont(font4)
        self.Vcpu_freqMax.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.Vcpu_freqMax.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.Vcpu_freqMax)

        self.Vcpu_freqMin = QLabel(self.FDdireito)
        self.Vcpu_freqMin.setObjectName(u"Vcpu_freqMin")
        self.Vcpu_freqMin.setFont(font4)
        self.Vcpu_freqMin.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.Vcpu_freqMin.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.Vcpu_freqMin)


        self.horizontalLayout_3.addWidget(self.FDdireito)


        self.verticalLayout_3.addWidget(self.FDados, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.Frame_Cpu)

        self.Frame_Memory = QFrame(self.frame_center)
        self.Frame_Memory.setObjectName(u"Frame_Memory")
        self.Frame_Memory.setMinimumSize(QSize(250, 400))
        self.Frame_Memory.setMaximumSize(QSize(200, 350))
        self.Frame_Memory.setStyleSheet(u"QFrame {\n"
"	background:  none;	\n"
"	\n"
"\n"
"    }\n"
"")
        self.Frame_Memory.setFrameShape(QFrame.NoFrame)
        self.Frame_Memory.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Frame_Memory)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.progres_fund_memoria = QFrame(self.Frame_Memory)
        self.progres_fund_memoria.setObjectName(u"progres_fund_memoria")
        self.progres_fund_memoria.setMinimumSize(QSize(250, 250))
        self.progres_fund_memoria.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 125px;\n"
"	background-color: rgba(85, 170, 255, 0.10);\n"
"}")
        self.progres_fund_memoria.setFrameShape(QFrame.StyledPanel)
        self.progres_fund_memoria.setFrameShadow(QFrame.Raised)
        self.Porcent_circle_memoria = QFrame(self.progres_fund_memoria)
        self.Porcent_circle_memoria.setObjectName(u"Porcent_circle_memoria")
        self.Porcent_circle_memoria.setGeometry(QRect(0, 0, 250, 250))
        self.Porcent_circle_memoria.setMinimumSize(QSize(250, 250))
        self.Porcent_circle_memoria.setMaximumSize(QSize(250, 250))
        self.Porcent_circle_memoria.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 125px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.749 rgba(170, 0, 255, 0), stop:0.75 rgba(242, 255, 5, 255));\n"
"}")
        self.Porcent_circle_memoria.setFrameShape(QFrame.StyledPanel)
        self.Porcent_circle_memoria.setFrameShadow(QFrame.Raised)
        self.cicler_3 = QFrame(self.Porcent_circle_memoria)
        self.cicler_3.setObjectName(u"cicler_3")
        self.cicler_3.setGeometry(QRect(10, 10, 230, 230))
        self.cicler_3.setMinimumSize(QSize(230, 230))
        self.cicler_3.setMaximumSize(QSize(230, 230))
        self.cicler_3.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 115px;\n"
"	background-color: #131B1F;\n"
"}\n"
"QFrame:hover{\n"
"	background:  #38393B;\n"
"}")
        self.cicler_3.setFrameShape(QFrame.StyledPanel)
        self.cicler_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.cicler_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_19 = QLabel(self.cicler_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background-color: none;")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_19)

        self.Vmemory_usage = QLabel(self.cicler_3)
        self.Vmemory_usage.setObjectName(u"Vmemory_usage")
        self.Vmemory_usage.setFont(font2)
        self.Vmemory_usage.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background-color: none;")
        self.Vmemory_usage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.Vmemory_usage)

        self.label_21 = QLabel(self.cicler_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background-color: none;")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_21)


        self.verticalLayout_11.addWidget(self.progres_fund_memoria)

        self.FDados_3 = QFrame(self.Frame_Memory)
        self.FDados_3.setObjectName(u"FDados_3")
        self.FDados_3.setEnabled(True)
        self.FDados_3.setMinimumSize(QSize(200, 100))
        self.FDados_3.setMaximumSize(QSize(200, 170))
        self.FDados_3.setStyleSheet(u"QFrame{\n"
"	background: none;\n"
"}")
        self.FDados_3.setFrameShape(QFrame.StyledPanel)
        self.FDados_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.FDados_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.FDesquedo_3 = QFrame(self.FDados_3)
        self.FDesquedo_3.setObjectName(u"FDesquedo_3")
        self.FDesquedo_3.setMinimumSize(QSize(90, 0))
        self.FDesquedo_3.setStyleSheet(u"background: none;\n"
"border: none;")
        self.FDesquedo_3.setFrameShape(QFrame.StyledPanel)
        self.FDesquedo_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.FDesquedo_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_22 = QLabel(self.FDesquedo_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font3)
        self.label_22.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.label_22.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.label_22)

        self.label_23 = QLabel(self.FDesquedo_3)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(100, 0))
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.label_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.label_23)

        self.label_24 = QLabel(self.FDesquedo_3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font3)
        self.label_24.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")

        self.verticalLayout_14.addWidget(self.label_24)


        self.horizontalLayout_5.addWidget(self.FDesquedo_3)

        self.FDdireito_3 = QFrame(self.FDados_3)
        self.FDdireito_3.setObjectName(u"FDdireito_3")
        self.FDdireito_3.setMinimumSize(QSize(80, 50))
        self.FDdireito_3.setMaximumSize(QSize(90, 16777215))
        self.FDdireito_3.setStyleSheet(u"background: none;\n"
"border: none;")
        self.FDdireito_3.setFrameShape(QFrame.StyledPanel)
        self.FDdireito_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.FDdireito_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.Vmemory_total = QLabel(self.FDdireito_3)
        self.Vmemory_total.setObjectName(u"Vmemory_total")
        self.Vmemory_total.setFont(font4)
        self.Vmemory_total.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.Vmemory_total.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.Vmemory_total)

        self.Vmemory_Alocado = QLabel(self.FDdireito_3)
        self.Vmemory_Alocado.setObjectName(u"Vmemory_Alocado")
        self.Vmemory_Alocado.setFont(font4)
        self.Vmemory_Alocado.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.Vmemory_Alocado.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.Vmemory_Alocado)

        self.Vmemory_Disponivel = QLabel(self.FDdireito_3)
        self.Vmemory_Disponivel.setObjectName(u"Vmemory_Disponivel")
        self.Vmemory_Disponivel.setFont(font4)
        self.Vmemory_Disponivel.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.Vmemory_Disponivel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.Vmemory_Disponivel)


        self.horizontalLayout_5.addWidget(self.FDdireito_3)


        self.verticalLayout_11.addWidget(self.FDados_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.Frame_Memory)

        self.Frame_Disco = QFrame(self.frame_center)
        self.Frame_Disco.setObjectName(u"Frame_Disco")
        self.Frame_Disco.setMinimumSize(QSize(250, 400))
        self.Frame_Disco.setMaximumSize(QSize(200, 350))
        self.Frame_Disco.setStyleSheet(u"QFrame {\n"
"	background:  none;	\n"
"	\n"
"\n"
"    }\n"
"")
        self.Frame_Disco.setFrameShape(QFrame.NoFrame)
        self.Frame_Disco.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.Frame_Disco)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.progres_fundcpu_2 = QFrame(self.Frame_Disco)
        self.progres_fundcpu_2.setObjectName(u"progres_fundcpu_2")
        self.progres_fundcpu_2.setMinimumSize(QSize(250, 250))
        self.progres_fundcpu_2.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 125px;\n"
"	background-color: rgba(85, 170, 255, 0.10);\n"
"}")
        self.progres_fundcpu_2.setFrameShape(QFrame.StyledPanel)
        self.progres_fundcpu_2.setFrameShadow(QFrame.Raised)
        self.Porcent_circle_disco = QFrame(self.progres_fundcpu_2)
        self.Porcent_circle_disco.setObjectName(u"Porcent_circle_disco")
        self.Porcent_circle_disco.setGeometry(QRect(0, 0, 250, 250))
        self.Porcent_circle_disco.setMinimumSize(QSize(250, 250))
        self.Porcent_circle_disco.setMaximumSize(QSize(250, 250))
        self.Porcent_circle_disco.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 125px;\n"
"	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0.749 rgba(170, 0, 255, 0), stop:0.75 rgba(242, 255, 5, 255));\n"
"}")
        self.Porcent_circle_disco.setFrameShape(QFrame.StyledPanel)
        self.Porcent_circle_disco.setFrameShadow(QFrame.Raised)
        self.cicler_2 = QFrame(self.Porcent_circle_disco)
        self.cicler_2.setObjectName(u"cicler_2")
        self.cicler_2.setGeometry(QRect(10, 10, 230, 230))
        self.cicler_2.setMinimumSize(QSize(230, 230))
        self.cicler_2.setMaximumSize(QSize(230, 230))
        self.cicler_2.setStyleSheet(u"QFrame{\n"
"	border: none;\n"
"	border-radius: 115px;\n"
"	background-color: #131B1F;\n"
"}\n"
"QFrame:hover{\n"
"	background:  #38393B;\n"
"}")
        self.cicler_2.setFrameShape(QFrame.StyledPanel)
        self.cicler_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.cicler_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_10 = QLabel(self.cicler_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background-color: none;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_10)

        self.Vdisco = QLabel(self.cicler_2)
        self.Vdisco.setObjectName(u"Vdisco")
        self.Vdisco.setFont(font2)
        self.Vdisco.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background-color: none;")
        self.Vdisco.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.Vdisco)

        self.label_12 = QLabel(self.cicler_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background-color: none;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_12)


        self.verticalLayout_7.addWidget(self.progres_fundcpu_2)

        self.FDados_2 = QFrame(self.Frame_Disco)
        self.FDados_2.setObjectName(u"FDados_2")
        self.FDados_2.setEnabled(True)
        self.FDados_2.setMinimumSize(QSize(200, 100))
        self.FDados_2.setMaximumSize(QSize(200, 170))
        self.FDados_2.setStyleSheet(u"QFrame{\n"
"	background: none;\n"
"}")
        self.FDados_2.setFrameShape(QFrame.StyledPanel)
        self.FDados_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.FDados_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.FDesquedo_2 = QFrame(self.FDados_2)
        self.FDesquedo_2.setObjectName(u"FDesquedo_2")
        self.FDesquedo_2.setMinimumSize(QSize(90, 0))
        self.FDesquedo_2.setStyleSheet(u"background: none;\n"
"border: none;")
        self.FDesquedo_2.setFrameShape(QFrame.StyledPanel)
        self.FDesquedo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.FDesquedo_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_13 = QLabel(self.FDesquedo_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_13)

        self.label_14 = QLabel(self.FDesquedo_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_9.addWidget(self.label_14)

        self.label_15 = QLabel(self.FDesquedo_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")

        self.verticalLayout_9.addWidget(self.label_15)


        self.horizontalLayout_4.addWidget(self.FDesquedo_2)

        self.FDdireito_2 = QFrame(self.FDados_2)
        self.FDdireito_2.setObjectName(u"FDdireito_2")
        self.FDdireito_2.setMinimumSize(QSize(80, 50))
        self.FDdireito_2.setMaximumSize(QSize(90, 16777215))
        self.FDdireito_2.setStyleSheet(u"background: none;\n"
"border: none;")
        self.FDdireito_2.setFrameShape(QFrame.StyledPanel)
        self.FDdireito_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.FDdireito_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.Vdisco_Total = QLabel(self.FDdireito_2)
        self.Vdisco_Total.setObjectName(u"Vdisco_Total")
        self.Vdisco_Total.setFont(font4)
        self.Vdisco_Total.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.Vdisco_Total.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.Vdisco_Total)

        self.Vdisco_Alocado = QLabel(self.FDdireito_2)
        self.Vdisco_Alocado.setObjectName(u"Vdisco_Alocado")
        self.Vdisco_Alocado.setFont(font4)
        self.Vdisco_Alocado.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.Vdisco_Alocado.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.Vdisco_Alocado)

        self.Vdisco_Disponivel = QLabel(self.FDdireito_2)
        self.Vdisco_Disponivel.setObjectName(u"Vdisco_Disponivel")
        self.Vdisco_Disponivel.setFont(font4)
        self.Vdisco_Disponivel.setStyleSheet(u"border: none;\n"
"color: #05F29B;\n"
"background: none;")
        self.Vdisco_Disponivel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.Vdisco_Disponivel)


        self.horizontalLayout_4.addWidget(self.FDdireito_2)


        self.verticalLayout_7.addWidget(self.FDados_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.Frame_Disco)


        self.verticalLayout_12.addWidget(self.frame_center, 0, Qt.AlignHCenter)

        self.Botton = QFrame(self.page_home)
        self.Botton.setObjectName(u"Botton")
        self.Botton.setMinimumSize(QSize(40, 40))
        self.Botton.setMaximumSize(QSize(16777215, 20))
        self.Botton.setStyleSheet(u"background-color: #38393B;")
        self.Botton.setFrameShape(QFrame.StyledPanel)
        self.Botton.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Botton)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.Botton)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame)

        self.Atualizar = QPushButton(self.Botton)
        self.Atualizar.setObjectName(u"Atualizar")
        font5 = QFont()
        font5.setFamily(u"Tahoma")
        font5.setPointSize(12)
        self.Atualizar.setFont(font5)
        self.Atualizar.setStyleSheet(u"\n"
"QPushButton {\n"
"	color: #131B1F;\n"
"    border: none;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"	background-color: #F2FF05;\n"
"    padding: 5px;\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 255, 255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(56, 57, 59);\n"
"    }")

        self.horizontalLayout_7.addWidget(self.Atualizar)

        self.label_28 = QLabel(self.Botton)
        self.label_28.setObjectName(u"label_28")
        font6 = QFont()
        font6.setFamily(u"Arial")
        self.label_28.setFont(font6)
        self.label_28.setStyleSheet(u"color: #47ACDE;")
        self.label_28.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_28)


        self.verticalLayout_12.addWidget(self.Botton)

        self.Home_page.addWidget(self.page_home)
        self.page_credts = QWidget()
        self.page_credts.setObjectName(u"page_credts")
        self.Home_page.addWidget(self.page_credts)

        self.verticalLayout_2.addWidget(self.Home_page)


        self.verticalLayout.addWidget(self.backgrund)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.Home_page.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"Monitor de Processos", None))
#if QT_CONFIG(tooltip)
        self.bts_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimizar", None))
#endif // QT_CONFIG(tooltip)
        self.bts_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.bts_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximizar", None))
#endif // QT_CONFIG(tooltip)
        self.bts_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.bts_close.setToolTip(QCoreApplication.translate("MainWindow", u"Fechar", None))
#endif // QT_CONFIG(tooltip)
        self.bts_close.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.Vcpu_usage.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Uso de CPU", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CPU Freq:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CPU Freq. Max:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CPU Freq. Min:", None))
        self.Vcpu_freq.setText(QCoreApplication.translate("MainWindow", u"1000mhz", None))
        self.Vcpu_freqMax.setText(QCoreApplication.translate("MainWindow", u"1000mhz", None))
        self.Vcpu_freqMin.setText(QCoreApplication.translate("MainWindow", u"1000mhz", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Memoria", None))
        self.Vmemory_usage.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Uso de memoria", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Alocado:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Disponivel:", None))
        self.Vmemory_total.setText(QCoreApplication.translate("MainWindow", u"1000mhz", None))
        self.Vmemory_Alocado.setText(QCoreApplication.translate("MainWindow", u"1000mhz", None))
        self.Vmemory_Disponivel.setText(QCoreApplication.translate("MainWindow", u"1000mhz", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Disco C:", None))
        self.Vdisco.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Aloca\u00e7\u00e3o", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Alocado:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Disponivel:", None))
        self.Vdisco_Total.setText(QCoreApplication.translate("MainWindow", u"1000mhz", None))
        self.Vdisco_Alocado.setText(QCoreApplication.translate("MainWindow", u"1000mhz", None))
        self.Vdisco_Disponivel.setText(QCoreApplication.translate("MainWindow", u"1000mhz", None))
        self.Atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar Dados", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"created by kaio Guilherme.", None))
    # retranslateUi


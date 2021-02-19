import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QCoreApplication, QDate, QDateTime, QEvent, QMetaObject, QObject, QPoint, QPropertyAnimation, QRect, QSize, QTime, QTimer, QUrl, Qt
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# Importação das funções
from ui_Monitor_processos_IU import Ui_MainWindow
from Func_monitor import *
from funcoes_ui import *
import time
from asyncio.runners import run

# variaveis globais



    
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #===================================fuções de do programa====================================
        def atualizar_dados(self):
            # dados cpu
            FuncoesUI.progressBarValue(self, cpu(3), self.ui.Porcent_circle_cpu, "rgba(242, 255, 5, 255)") # atualização da barra de progresso
            self.ui.Vcpu_usage.setText(str(cpu(3)) + " %") # porcentagem de uso
            self.ui.Vcpu_freq.setText(cpu(0))
            self.ui.Vcpu_freqMax.setText(cpu(2))
            self.ui.Vcpu_freqMin.setText(cpu(1))

            # dados da memoria Ram

            FuncoesUI.progressBarValue(self,memoria(2), self.ui.Porcent_circle_memoria, "rgba(242, 255, 5, 255)")
            self.ui.Vmemory_usage.setText(str(memoria(2)) + " %") # porcentagem de uso
            self.ui.Vmemory_total.setText(memoria(0))
            self.ui.Vmemory_Alocado.setText(memoria(3))
            self.ui.Vmemory_Disponivel.setText(memoria(4))

            # dados do disco

            FuncoesUI.progressBarValue(self,disco(3), self.ui.Porcent_circle_disco, "rgba(242, 255, 5, 255)")
            self.ui.Vdisco.setText(str(disco(3)) + " %")
            self.ui.Vdisco_Total.setText(disco(0))
            self.ui.Vdisco_Alocado.setText(disco(1))
            self.ui.Vdisco_Disponivel.setText(disco(2))


        #=======================Funções de janela=================================
        # Função de mover janela
        def moveWindow(event):

            
            # restaura pagina quando tentar mover pagina maximizada
            if FuncoesUI.RetornaStatus(self) == 1:
                FuncoesUI.maximizacao(self)

            # Mover a pagina se clicar com o botão esquedo do mause

            # se estiver clicado com botão esquerdo do mause mover janela
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # Executa as definições da janela
        FuncoesUI.DefinicoesUi(self)
        atualizar_dados(self)
        # Define a barra de titulo
        self.ui.top.mouseMoveEvent = moveWindow

        

        #mostra a tela principal
        self.show()
        self.ui.Atualizar.clicked.connect(lambda: atualizar_dados(self))
        
        

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
    
    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


    
        
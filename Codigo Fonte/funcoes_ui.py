from Main import *

# Vareiaveis Globais

ESTADO_GLOBAL = 0

class FuncoesUI(MainWindow):
    # Funções de restauração de maxizimação
    def maximizacao(self):
        global ESTADO_GLOBAL
        status = ESTADO_GLOBAL

        # Se não estiver maximizado
        if status == 0:
            self.showMaximized()

            # Estado global recebe 1
            ESTADO_GLOBAL = 1

            
            self.ui.bts_maximize.setToolTip("Restaurar")
        else:
            ESTADO_GLOBAL = 0
            self.showNormal()
            self.ui.bts_maximize.setToolTip("Maximizar")

    # Definições de janela
    def DefinicoesUi(self):

        # remove barra de titulo
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    
    # Maximizar é restaurar
        self.ui.bts_maximize.clicked.connect(lambda: FuncoesUI.maximizacao(self))

        # Minimizar
        self.ui.bts_minimize.clicked.connect(lambda: self.showMinimized())

        # Fechar
        self.ui.bts_close.clicked.connect(lambda: self.close())

    # Função da barra de progresso
    def progressBarValue(self, value, widget, color):

        # PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
            border-radius: 125px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:270, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        # pegas o valores e conver para float
        # stop de 1.000 to 0.000
        progress = (100 - value) / 100.0

        # adiciona os novos valores
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # defini os valores maximos
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # adiciona os novos valores no styleshet
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # aplica o o novo syleshet
        widget.setStyleSheet(newStylesheet)


    ## Retorna status global se a janela esta minimizada ou maximizada
    def RetornaStatus(self):
        return ESTADO_GLOBAL
      
import sys
from PaginaInicio import *
from PyQt6.QtWidgets import QDialog, QApplication, QSplashScreen, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import Qt, QTimer
from Archivos import *



class Barra(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        # super().__init__()
        uic.loadUi("VentanaCarga.ui", self)
        # Imagen de Fondo
        # pixmap=QPixmap()
        self.contador = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)
    def loading(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.progressBar.setValue(self.contador)

        # CLOSE SPLASH SCREE AND OPEN APP
        if self.contador > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = PaginaInicio()
            archivo = Archivos()
            self.p
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.contador += 1


class PaginaInicio(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi("PaginaInicio.ui", self)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ventana = Barra()
    # Ventana.show()
    Ventana.show()
    # Ventana.progress()
    Ventana.loading()

    sys.exit(app.exec())

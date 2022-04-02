import sys
from tkinter import filedialog

from PyQt6.QtWidgets import QDialog, QApplication, QSplashScreen, QMainWindow
from PyQt6 import uic
from PyQt6.QtCore import Qt, QTimer



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
        global contador

        # SET VALUE TO PROGRESS BAR
        self.progressBar.setValue(self.contador)

        # CLOSE SPLASH SCREE AND OPEN APP
        if self.contador > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = PaginaProceso()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.contador += 1


class PaginaProceso(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi("pagina_proceso.ui", self)
        #------------------------- Paginas -----------------------------
        # Pagina 1
        self.btn_pag1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_Interplanar))
        # Pagina 2
        self.btn_pag2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_3d))
        # Pagina 3
        self.btn_pag3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pagina_otra))
        # Boton conectado a Opciones para abrir archivos
        self.btn_Opciones.clicked.connect(lambda: self.Abrir_archivos())

    def Abrir_archivos(self):
        abrir = filedialog.askopenfile(title="abrir", initialdir="C:/",
        filetypes=(("Archivos de Texto", "*.txt"), ("Archivos pdf", "*.pdf"),
        ("Hoja de cálculo Excel", "*.csv")))

        self.label_4(print(abrir.read()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ventana = Barra()
    # Ventana.show()
    Ventana.show()
    # Ventana.progress()
    Ventana.loading()
    sys.exit(app.exec())

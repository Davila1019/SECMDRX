# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VentanaCarga.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VentanaCarga(object):
    def __init__(self):
        self.label_description = None

    def setupUi(self, VentanaCarga):
        VentanaCarga.setObjectName("VentanaCarga")
        VentanaCarga.resize(680, 400)
        self.centralwidget = QtWidgets.QWidget(VentanaCarga)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadow = QtWidgets.QFrame(self.centralwidget)
        self.dropShadow.setStyleSheet("QFrame{\n"
"background-color: rgb(220, 207, 195);\n"
"color: rgb(216, 219, 255);\n"
"border-radius:10px;\n"
"}")
        self.dropShadow.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadow.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadow.setObjectName("dropShadow")
        self.label_Titulo = QtWidgets.QLabel(self.dropShadow)
        self.label_Titulo.setGeometry(QtCore.QRect(0, 80, 661, 124))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(70)
        font.setBold(False)
        font.setWeight(50)
        self.label_Titulo.setFont(font)
        self.label_Titulo.setStyleSheet("\n"
"color: rgb(94, 34, 47);")
        self.label_Titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Titulo.setObjectName("label_Titulo")
        self.label_Descripcion = QtWidgets.QLabel(self.dropShadow)
        self.label_Descripcion.setGeometry(QtCore.QRect(-1, 210, 661, 32))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_Descripcion.setFont(font)
        self.label_Descripcion.setStyleSheet("\n"
"color: rgb(159, 147, 140);")
        self.label_Descripcion.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Descripcion.setObjectName("label_Descripcion")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadow)
        self.progressBar.setGeometry(QtCore.QRect(40, 270, 581, 21))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    \n"
"    background-color: rgb(193, 179, 168);\n"
"    color: rgb(234, 217, 204);\n"
"    border-style:none;\n"
"    border-radius:10px;\n"
"    text-align:center;\n"
"\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.5, x2:1, y2:0.506, stop:0 rgba(86, 38, 67, 255), stop:1 rgba(156, 56, 78, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_Cargando = QtWidgets.QLabel(self.dropShadow)
        self.label_Cargando.setGeometry(QtCore.QRect(0, 295, 661, 32))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_Cargando.setFont(font)
        self.label_Cargando.setStyleSheet("\n"
"color: rgb(159, 147, 140);")
        self.label_Cargando.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Cargando.setObjectName("label_Cargando")
        self.verticalLayout.addWidget(self.dropShadow)
        VentanaCarga.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaCarga)
        QtCore.QMetaObject.connectSlotsByName(VentanaCarga)

    def retranslateUi(self, VentanaCarga):
        _translate = QtCore.QCoreApplication.translate
        VentanaCarga.setWindowTitle(_translate("VentanaCarga", "MainWindow"))
        self.label_Titulo.setText(_translate("VentanaCarga", "<strong> FLDS</strong>MDFR"))
        self.label_Descripcion.setText(_translate("VentanaCarga", "<strong>LA</strong> RIATA"))
        self.label_Cargando.setText(_translate("VentanaCarga", "<strong>Cargando...</strong>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VentanaCarga = QtWidgets.QMainWindow()
    ui = Ui_VentanaCarga()
    ui.setupUi(VentanaCarga)
    VentanaCarga.show()
    sys.exit(app.exec_())



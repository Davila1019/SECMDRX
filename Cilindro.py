import sys
import numpy as np
from Gui import*
from PyQt6 import QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class MiApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.grafica = Cilindro()
        self.ui.verticalLayout.addWidget(self.grafica)

class Cilindro(FigureCanvas):
    def __init__(self,parent = None):
       self.fig,self.ax = plt.subplots(facecolor='blue')
       super().__init__(self.fig)
       self.ax.grid()
       self.ax.margins(x=0)
       self.grafica_datos()


    def grafica_datos(self):
       plt.title("Grafica Prueba")

       fig = plt.figure()
       ax = Axes3D(fig)
       theta = np.arange(0, 2 * np.pi, 0.01)
       z_ = np.arange(0, 2, 0.01)
       r = np.sqrt(9)
       theta, z_ = np.meshgrid(theta, z_)
       x = r * np.cos(theta)
       y = r * np.sin(theta)
       z = z_
       ax.plot_surface(x, y, z, color='blue')
       plt.show()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Ventana = MiApp()
    Ventana.show()
    # Ventana.Cilindro()
    # Botones.show()
    # Ventana.progress()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')

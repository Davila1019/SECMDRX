import sys
from archivos.Archivos import Archivos
from clasificador.Knn import Knn
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from datetime import datetime,date
from tkinter import messagebox as mb
import errno
from scipy.signal import find_peaks, savgol_filter
import os

class Patron_U:
    def __init__(self):
        self._angle_2Theta = []
        self._intensity = []
        self._index_peaks = []
        self._final_peaks = []
        self._final_ind = [] #Lista que contiene los indices de miller
        self._class = {}
        self.name_class =''
        self._angle_peaks = []
        self.plt = None
        self.plt_dif = None
        self._data_suav = []

    @property
    def angle(self):
        print("@propiety class Patron_U method called")
        return self._angle_2Theta

    @angle.setter
    def angle(self, angulo):
        print("@angulos.setter class method called")
        self._angle_2Theta.append(angulo)

    @property
    def intensidad(self):
        print("@propiety class Patron_U method called")
        return self._intensity

    @property
    def final_ind(self):
        print("@propiety class Patron_U method called, get indices Miller")
        return self._final_ind

    @intensidad.setter
    def intensidad(self, intensidad):
        print("@intencidad.setter class method called")
        self._intensity.append(intensidad)

    def load_data(self):
        a = Archivos()
        try:
            data = a.abrir_Archivo()
        except KeyError:
            mb.showwarning("Formato invalido", "El archivo seleccionado no tiene el formato valido")
            return self.load_data()
        except FileNotFoundError:
            sys.exit()
        self._angle_2Theta = data[0]
        self._intensity = data[1]

    def add_peaks(self,plt):
        i = 0
        while i < len(self._data_suav):
            j = 0
            while j < len(self._index_peaks):
                if (i == self._index_peaks[j]):
                    plt.text(self._angle_2Theta[i] + 1, self._intensity[i] + 50, f'({self._final_ind[j]})', rotation=45)
                    j += 1
                else:
                    j += 1
            i += 1
        self.save_fig()


    def smooth_pattern(self):
        data = list(self._intensity)
        suav_1 = savgol_filter(data, 51, 1)  # Filtro de savitzky–golay X6 (suavizado de señal)
        suav_2 = savgol_filter(suav_1, 51, 1)
        suav_3 = savgol_filter(suav_2, 51, 1)
        suav_4 = savgol_filter(suav_3, 51, 1)
        suaV_5 = savgol_filter(suav_4, 51, 1)
        data_suav = savgol_filter(suaV_5, 51, 1)
        return data_suav

    def detectar_Picos(self):
        clas = Knn()
        clas.fit()
        self._data_suav = self.smooth_pattern()
        dat_p = pd.DataFrame(self._data_suav)
        des = list(dat_p.std())
        found_peaks = find_peaks(self._data_suav, height=(des[0]))
        self._index_peaks = list(found_peaks.__getitem__(0))
        self.get_angles_peaks(self._index_peaks)
        self._class = clas.classification(self._angle_peaks)
        self._final_ind = list(self._class.values())[0]
        self.plot_chart()
        self.name_class = list(self._class.keys())[0]
        #self.plt.show()

    def get_angles_peaks(self, index_peaks: list):
        tam = len(index_peaks)
        i = 0
        while i < tam:
            self._angle_peaks.append(self._angle_2Theta[self._index_peaks[i]])
            i += 1
    # Función para graficar (pruebas unitarias)

    def plot_chart(self):
        self.plt = Figure(figsize=(6, 6), dpi=100)

        self.plt_dif = self.plt.add_subplot(111)
        self.plt_dif.plot(self._angle_2Theta, self._intensity, c='g')
        self.add_peaks(self.plt_dif)
        self.plt_dif.set_ylabel('Intensidad(u.a.)')
        self.plt_dif.set_xlabel('2'r'$\theta$(grados)')
        metal = list(self._class.keys())[0]
        self.plt_dif.set_title(metal)


    def save_fig(self):
        try:
            os.makedirs('C:/SECMDRX/frames')
        except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
        try:
            self.plt.savefig('C:/SECMDRX/frames/difractogram.png', bbox_inches='tight')
        except OSError:
            mb.showerror('Error','Ocurrio un error en el sistema')





#p = Patron_U()
#p.load_data()
#p.detectar_Picos()

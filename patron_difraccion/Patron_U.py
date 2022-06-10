from archivos.Archivos import Archivos
from clasificador.Knn import Knn
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox as mb
from scipy.signal import find_peaks, savgol_filter


class Patron_U:
    def __init__(self):
        self._angle_2Theta = []
        self._intensity = []
        self._index_peaks = []
        self._final_peaks = []
        self._final_ind = []
        self._final_class = {}
        self._angle_peaks = []

    @property
    def angle(self):
        print("@propiety class method called")
        return self._angle_2Theta

    @angle.setter
    def angle(self, angulo):
        print("@angulos.setter class method called")
        self._angle_2Theta.append(angulo)

    @property
    def intensidad(self):
        print("@propiety class method called")
        return self._intensity

    @intensidad.setter
    def intensidad(self, intensidad):
        print("@intencidad.setter class method called")
        self._intensity.append(intensidad)

    def load_data(self):
        a = Archivos()
        try:
            data = a.abrir_Archivo()
        except KeyError:
            mb.showwarning("Formato invalido", "El archivo no tiene el formato valido")
            self.load_data()
        except FileNotFoundError:
            mb.askretrycancel("Cerrar","¿Desea terminar?",["Si","No"]) #pendiente
        self._angle_2Theta = data[0]
        self._intensity = data[1]

    def add_peaks(self, plt, data, index_peaks, final_ind):
        i = 0
        while i < len(data):
            j = 0
            while j < len(index_peaks):
                if (i == index_peaks[j]):
                    plt.text(self._angle_2Theta[i] + 1, self._intensity[i] + 50, f'({final_ind[j]}) \u03B8', rotation=90)
                    j += 1
                else:
                    j += 1
            i += 1

    def smooth_pattern(self):
        data = self._intensity
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
        data_suav = self.smooth_pattern()
        dat_p = pd.DataFrame(data_suav)
        des = list(dat_p.std())
        found_peaks = find_peaks(data_suav, height=(des[0]))
        self._index_peaks = list(found_peaks.__getitem__(0))
        self.get_angles_peaks(self._index_peaks)
        plt.figure(figsize=(9, 6))
        self._final_class = clas.classification(self._angle_peaks)
        self._final_ind = list(self._final_class.values())[0]
        self.plot_chart(plt)
        print(self._final_ind)
        self.add_peaks(plt, data_suav, self._index_peaks, self._final_ind)
        plt.show()

    def get_angles_peaks(self, index_peaks: list):
        tam = len(index_peaks)
        i = 0
        while i < tam:
            self._angle_peaks.append(self._angle_2Theta[self._index_peaks[i]])
            i += 1

    def plot_chart(self,plt):
        plt.plot(self._angle_2Theta, self._intensity)
        plt.ylabel('Intensidad(u.a.)')
        plt.xlabel('2'r'$\theta$(grados)')
        metal = list(self._final_class.keys())[0]
        plt.title(metal)
        plt.suptitle('Difractograma R-X')





p = Patron_U()
p.load_data()
p.detectar_Picos()

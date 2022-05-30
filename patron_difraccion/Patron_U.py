from archivos.Archivos import Archivos
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, savgol_filter

class Patron_U:
    def __init__(self):
        self._puser = dict([])
        self._angulos_2Theta = []
        self._intensidad = []

    @property
    def angulos(self):
        print("@propiety class method called")
        return self._angulos_2Theta

    @angulos.setter
    def angulos(self, angulo):
        print("@angulos.setter class method called")
        self._angulos_2Theta.append(angulo)

    @property
    def intensidad(self):
        print("@propiety class method called")
        return self._intensidad

    @intensidad.setter
    def intensidad(self, intensidad):
        print("@intencidad.setter class method called")
        self._intensidad.append(intensidad)

    def cargar_Datos(self):
        a = Archivos()
        data = a.abrir_Archivo()
        self._angulos_2Theta = data[0]
        self._intensidad = data[1]

    def agregar_picos(self, plt, data, index_peaks):
        i = 0
        while i < len(data):
            j = 0
            while j < len(index_peaks):
                if (i == index_peaks[j]):
                    plt.text(self._angulos_2Theta[i] + 1 , self._intensidad[i] + 50, f'111', rotation= 90)
                    j += 1
                else:
                    j += 1
            i += 1

    def suavizar_Patron(self):
        data = self._intensidad
        suav_1 = savgol_filter(data, 51, 1)  # Filtro de savitzky–golay X6 (suavizado de señal)
        suav_2 = savgol_filter(suav_1, 51, 1)
        suav_3 = savgol_filter(suav_2, 51, 1)
        suav_4 = savgol_filter(suav_3, 51, 1)
        suaV_5 = savgol_filter(suav_4, 51, 1)
        data_suav = savgol_filter(suaV_5, 51, 1)
        return data_suav

    def detectar_Picos(self):
        data_suav = self.suavizar_Patron()
        dat_p = pd.DataFrame(data_suav)
        des = list(dat_p.std())
        found_peaks = find_peaks(data_suav,height=(des[0]))
        peaks = list(found_peaks[1].values())
        index_peaks = list(found_peaks.__getitem__(0))
        peaks_tot = list(peaks[0])
        plt.figure(figsize=(9, 6))
        plt.plot(self._angulos_2Theta, self._intensidad)
        plt.ylabel('Intensidad(u.a.)')
        plt.xlabel('2'r'$\theta$(grados)')
        plt.suptitle('Difractograma R-X')
        self.agregar_picos(plt,data_suav,index_peaks)
        plt.show()


p = Patron_U()
p.cargar_Datos()
p.detectar_Picos()
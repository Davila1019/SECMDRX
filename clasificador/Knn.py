import math
import numpy as np

#
#       Implementación del algoritmo de clasificación supervisada Knn
#
#              (Clasificación mediante distancia euclidiana)
#
#       Se determinó que el valor de K sería igual al total de elementos dentro de las diferentes
#       listas de indices, esto para que la clasficación tenga un mayor porcentaje de acertación.
#
#

class Knn:
    def __init__(self):
        self._labels = ['Aluminio', 'Cobre', 'Hierro', 'Titanio', 'Metal no reconocido']
        self._distances = {self._labels[0]: math.inf, self._labels[1]: math.inf, self._labels[2]: math.inf, self._labels[3]: math.inf}
        self._data = {}
        self._result = {}
    def fit(self):
        # Índices de miller de Aluminio (Al)
        self._indicesAl = {38.769: '111', 44.716: '002', 65.090: '022', 78.220: '113',
                           82.427: '222'}
        # Índices de miller de Cobre (Cu)
        self._indicesCu = {37: '111', 43: '200', 64: '220', 77: '311'}
        # Índices de miller de Hierro (Fe)
        self._indicesFe = {44.5: '110', 54.954: '200', 82.245: '211', 98.958: '220',
                           116.521: '310'}
        #Indices de miller de Titanio (Ti)
        self._indicesTi = {36.7226:'101', 47.995: '102', 52.7762: '110', 66.42: '103'}

        self._result[self._labels[0]] = list(self._indicesAl.values())
        self._result[self._labels[1]] = list(self._indicesCu.values())
        self._result[self._labels[2]] = list(self._indicesFe.values())
        self._result[self._labels[3]] = list(self._indicesTi.values())


    def classification(self, peaks:list):
        tam = len(peaks)
        aux = 0
        if tam == 5:
            aux = 0
            j = 0
            for i in peaks:
                aux += math.pow(i - list(self._indicesAl.keys())[j], 2) #Calcular distancias a Aluminio
                j += 1
            aux = math.sqrt(aux)
            self._distances[self._labels[0]] = aux
            aux = 0
            j = 0
            for i in peaks:
                aux += math.pow(i - list(self._indicesFe.keys())[j], 2)#Calcular distancias a Hierro
                j += 1
            aux = math.sqrt(aux)
            self._distances[self._labels[2]] = aux
        elif tam == 4:
            j = 0
            for i in peaks:
                aux += math.pow(i - list(self._indicesCu.keys())[j], 2)
                j += 1
            aux = math.sqrt(aux)
            self._distances[self._labels[1]] = aux
            j = 0
            for i in peaks:
                aux += math.pow(i - list(self._indicesTi.keys())[j], 2)
                j += 1
            aux = math.sqrt(aux)
            self._distances[self._labels[3]] = aux
        else:
            return self._labels[4]

        return self.set_Class()



    def set_Class(self):
        short_dist = None
        res = {}
        for dist in list(self._distances.values()):
            if short_dist is None or dist < short_dist:
                short_dist = dist

        if short_dist in self._distances.values():
                clas = list(self._distances.keys())[list(self._distances.values()).index(short_dist)]
                if clas in self._result:
                    res[clas] = self._result.get(clas)
        return res

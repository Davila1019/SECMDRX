import pprint
import random
import matplotlib.pyplot as plt

class PatronT:
    def __init__(self):
        self._pteorico = dict([])
        self._indices_miller = []
        self._angulos_2Theta = []
        self._intensidad = []
        self.contador = 0.0

    @property
    def indicesM(self):
        print("@propiety class method called")
        return self._indices_miller

    @indicesM.setter
    def indicesM(self, indiceM):
        print("@indicesM.setter class method called")
        self._indices_miller.append(indiceM)

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

    @property
    def pteorico(self):
        print("@propiety class method called")
        return self._pteorico

    def imprimir_pteorico(self):
            pprint.pprint(self._pteorico)

    def definir_pteorico(self): # definimos un supuesto patrón de difracción teorico
        while self.contador < 90:
            aux = random.randint(400, 600)
            self._pteorico[self.contador] = aux
            self.contador = self.contador + 1

    def validar_pteorico(self): #validamos la posicion del angulo e insertamos la intesidad
        for angulo in self._pteorico.keys():
            i=0
            while i < len(self._angulos_2Theta):
                if angulo == round(self._angulos_2Theta[i],0):
                    self._pteorico[angulo] = self._intensidad[i]
                    i += 1
                else:
                    i += 1

    def agregar_indiceM(self,plt):
        for intensidad in self._pteorico.values():
            i=0
            while i < len(self._angulos_2Theta):
                plt.text(self._angulos_2Theta[i],self._intensidad[i], f'{self._indices_miller[i]}')
                i += 1

    def graficar_pteorico(self): #metódo para la graficación del difractograma
        plt.figure(figsize=(9, 6))
        plt.plot(self._pteorico.keys(),self._pteorico.values())
        plt.ylabel('Intensidad(u.a.)')
        plt.xlabel('2'r'$\theta$(grados)')
        plt.suptitle('Difractograma R-X')
        self.agregar_indiceM(plt)
        plt.show()


p = PatronT()
p.intensidad = 7144
p.intensidad = 5046
p.intensidad = 7656
p.intensidad = 10156
p.angulos = 36.7769
p.angulos = 47.5689
p.angulos = 79.1986
p.angulos = 84.3056
p.indicesM = 101
p.indicesM = 111
p.indicesM = 201
p.indicesM = 301
p.definir_pteorico()
p.imprimir_pteorico()
p.validar_pteorico()
p.imprimir_pteorico()
p.graficar_pteorico()

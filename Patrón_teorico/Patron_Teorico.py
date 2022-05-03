import pprint
import random
import collections

class PatronT:
    def __init__(self):
        self._pteorico = dict([])
        self._indices_miller = []
        self._angulos_2Theta = []
        self._intensidad = []
        self.contador = 20.0

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
        print("@indicesM.setter class method called")
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

    def definir_pteorico(self):
        num_ang = len(self._angulos_2Theta)
        while self.contador < 90:
            index = 0
            while index < num_ang:
                if  self._angulos_2Theta[index] - 0.019 < self.contador < self._angulos_2Theta[index] + 0.019:
                    self._pteorico[self.contador] = self._intensidad[index]
                    self.contador = self.contador + 0.019
                    index = index + 1
                    print('Aqui')
                else:
                    aux = random.randint(400, 600)
                    self._pteorico[self.contador] = aux
                    self.contador = self.contador + 0.019
                    index = index + 1


p = PatronT()
p.intensidad = 7144
p.intensidad = 5046
p.intensidad = 7656
p.intensidad = 10156
p.angulos = 36.7769
p.angulos = 47.5689
p.angulos = 79.1986
p.angulos = 84.3046

p.definir_pteorico()
#p.imprimir_pteorico()
p.validar_pteorico()
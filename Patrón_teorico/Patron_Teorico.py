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
        while self.contador <= 90:
            index = 0
            while index < num_ang:
                if self.contador != self._angulos_2Theta[index]:
                    aux = random.randint(400, 800)
                    self._pteorico[self.contador] = aux
                    self.contador = self.contador + 0.019
                    print(f'Aqui')
                    index = index + 1
                else:
                    self._pteorico[self.contador] = self._intensidad[self]
                    self.contador = self.contador + 0.019
                    print("Aqui estoy ciclado jejeje")
                    index = index + 1
p = PatronT()
p.intensidad = 7144
p.intensidad = 5046
p.angulos = 36.777
p.angulos = 47.56


p.definir_pteorico()
p.imprimir_pteorico()
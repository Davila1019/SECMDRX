import numpy as np
class Distancias:
    def __int__(self):
        self.resultado=[]
        self.resultadosen=[]
    def sen(self):
        for i in picos:
            angulo = np.radians(i/2)
            # resultado = np.sin(angulo)
            self.resultado=np.sin(angulo)
            print(f'El seno de:  {i} es: {self.resultado:.5}')
            continue
    def distancia(self):
        for i in picos:
            angulo = np.radians(i/2)
            dist= (amstrong/(2*np.sin(angulo)))
            print(f'Distancia interplanar del pico:  {i}, es: {dist:.4}')


amstrong = 1.541
picos = [38.5, 44.74, 65.134, 78.238]
distancia1=Distancias()
print(distancia1.distancia())

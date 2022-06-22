
import numpy as np
from indice.Cubo import Cubo
class parametros:
    def __init__(self):
        # Cobre = 1,43,Titanio= ,Aluminio= ,hierro=
        self.parametros=0
        self.radioA=0
         # 1-aluminiom 2-Titanio, 3-Cobre, 4- Hierro
    def parametros_red(self):
        if opcion==1:
            print("Metal Aluminio")
            print("Cubico Centrado en Cara")
            self.radioA=0.143
            calcular_parametro= (4*self.radioA)/pow(2,0.5)
            print(f'El parametro de red del Aluminio es de:{calcular_parametro:.4}')
        elif opcion==2:
            print("Metal Titanio")
            print("Cubico Centrado en Cuerpo")
            self.radioA = 0.144
            calcular_parametro = (4 * self.radioA) / pow(3, 0.5)
            print(f'El parametro de red del Titanio es de:{calcular_parametro:.4}')
        elif opcion==3:
            print("Metal Cobre")
            print("Cubico Centrado en Cara")
            self.radioA = 0.128
            calcular_parametro = (4 * self.radioA) / pow(2, 0.5)
            print(f'El parametro de red del Cobre es de:{calcular_parametro:.4}')
        elif opcion==4:
            print("Metal Hierro")
            print("Cubico Centrado en Cuerpo")
            self.radioA = 0.124
            calcular_parametro = (4 * self.radioA) / pow(3, 0.5)
            print(f'El parametro de red del Titanio es de:{calcular_parametro:.4}')

opcion = 4
parametro1= parametros()
print(parametro1.parametros_red())


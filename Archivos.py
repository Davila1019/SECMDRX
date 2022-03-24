from tkinter import *
from tkinter import filedialog
class Archivos:

    def abrirArchivo(self):
        archivo = filedialog.askopenfile(title="abrir", initialdir="C:/", filetypes=(("Archivos de Texto","*.txt"),("Archivos pdf","*.pdf"),("Hoja de cálculo Excel","*.csv")))
        total_lines = sum(1 for line in archivo)
        for total_lines in archivo:
            print(archivo.readline())
        print(total_lines)

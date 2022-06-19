from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog


# import CargaArchivosChido

class Interfaz2:
    def __init__(self):
        self.int2 = Tk()

        self.int2.overrideredirect(True)  # Quitar barra de título
        # int3.geometry('400x200')
        self.width_of_window = 200
        self.height_of_window = 150
        self.screen_width = self.int2.winfo_screenwidth()
        self.screen_height = self.int2.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.int2.geometry(
            "%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.bg = PhotoImage(file="Fondo.png")

        self.canvas1 = Canvas(self.int2, width=400,
                              height=200)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.bg,
                                  anchor="nw")
        self.var = IntVar()

        self.titulo = ttk.Label(self.int2, text="Datos con los que cuenta: ")
        self.btn = ttk.Radiobutton(self.int2, text="Patrón de difracción", variable=self.var, value=1,
                                   command=self.Evento_Seleccion)
        self.btn2 = ttk.Radiobutton(self.int2, text="Picos de difracción", variable=self.var, value=2,
                                    command=self.Evento_Seleccion)
        self.btn_aceptar = ttk.Button(self.int2, text="Aceptar", command=self.Evento_Aceptar)
        self.btn_cancelar = ttk.Button(self.int2, text="Cancelar", command=exit)


        self.titulo.place(x=10, y=10)
        self.btn.place(x=10, y=40)
        self.btn2.place(x=10, y=80)
        self.btn_aceptar.place(x=110, y=120)
        self.btn_cancelar.place(x=10, y=120)

        self.int2.mainloop()

    def Evento_Seleccion(self):
        elige = self.var.get()
        if elige == 1:
            print("Elección 1")
        elif elige == 2:
            print("Elección 2")
        else:
            print("Debe elegir una opción")
        pass
        return elige

    def Evento_Aceptar(self):
        self.datos = self.Evento_Seleccion()
        print(f'La elección fue: {self.datos}')
        if self.datos == 1:
            q = Tk()
            q.title('Main window')
            q.geometry('427x250')
            l1 = Label(q, text='ADD TEXT HERE ', fg='grey', bg=None)
            l = ('Calibri (Body)', 24, 'bold')
            l1.config(font=l)
            l1.place(x=80, y=100)
            q.mainloop()
            return messagebox.showinfo('PythonGuides', 'Elegiste interfaz patrón de difracción')

        elif self.datos == 2:
            return messagebox.showinfo('PythonGuides', 'Elegiste interfaz picos de difracción')
        else:
            return messagebox.showinfo('PythonGuides', 'No se eligió ninguna interfaz')


def main():
    window = Interfaz2()
    return 0


if __name__ == '__main__':
    main()

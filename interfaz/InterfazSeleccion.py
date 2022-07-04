from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog
from InterfazCargaArchivos import VentanaCargaArchivos
from InterfazCargaDatos import VentanaDatos

class VentanaSeleccion:
    def __init__(self):
        self.ventana_selec = Tk()
        self.ventana_selec.withdraw()
        self.ventana_selec.title('SECMDRX')
        self.ventana_selec.iconbitmap("../resourses/images/logo-ipn.ico")
        self.ventana_selec.resizable(False, False)
        self.width_of_window = 250
        self.height_of_window = 150
        self.screen_width = self.ventana_selec.winfo_screenwidth()
        self.screen_height = self.ventana_selec.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.ventana_selec.geometry(
            "%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.bg = PhotoImage(file="images/Fondo.png")

        self.canvas1 = Canvas(self.ventana_selec, width=400,
                              height=200)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.bg,
                                  anchor="nw")
        self.var = IntVar()
        self.bg_azul = '#249794' #Azul
        self.common_fg = '#ffffff'

        self.titulo = tk.Label(self.ventana_selec, text="Datos con los que cuenta: ", background="white", foreground="#249794")

        self.btn = tk.Radiobutton(self.ventana_selec, text="Patrón de difracción", fg=self.bg_azul, bg=self.common_fg,
                             activebackground=self.common_fg, activeforeground=self.bg_azul, selectcolor=self.common_fg,
                             variable=self.var, value=1, command=self.evento_Seleccion)

        self.btn2 = tk.Radiobutton(self.ventana_selec, text="Picos de difracción", fg=self.bg_azul, bg=self.common_fg,
                              activebackground=self.common_fg, activeforeground=self.bg_azul, selectcolor=self.common_fg, variable=self.var, value=2,
                              command=self.evento_Seleccion)

        self.btn_aceptar = tk.Button(self.ventana_selec, text="Aceptar", command=self.evento_Aceptar, width=12, height=1,
                                background="#249794", foreground="white")

        self.btn_cancelar = tk.Button(self.ventana_selec, text="Cancelar", command=exit, width=12, height=1,
                                      background="#249794", foreground="white")

        # rad_button.place(x=10, y=10)
        self.titulo.place(x=10, y=10)
        self.btn.place(x=10, y=40)
        self.btn2.place(x=10, y=80)
        self.btn_aceptar.place(x=150, y=120)
        self.btn_cancelar.place(x=10, y=120)
        self.ventana_selec.deiconify()
        self.ventana_selec.mainloop()

    def evento_Seleccion(self):
        elige = self.var.get()
        if elige == 1:
            print("Elección 1")
        elif elige == 2:
            print("Elección 2")
        else:
            print("Debe elegir una opción")
        pass
        return elige

    def evento_Aceptar(self):
        self.datos = self.evento_Seleccion()
        if self.datos == 1:
            self.ventana_selec.destroy()
            self.load = VentanaCargaArchivos()

        elif self.datos == 2:
            self.ventana_selec.destroy()
            self.data = VentanaDatos()
        else:
            return messagebox.showinfo('Nota', 'Debe de seleccionar una opción para continuar.')


def main():
    window = VentanaSeleccion()
    return 0


if __name__ == '__main__':
    main()

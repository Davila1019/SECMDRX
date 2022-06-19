from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font as f


class Patron:

    def __init__(self):
        self.int3 = Tk()
        self.int3.overrideredirect(True)  # Quitar barra de título
        # int3.geometry('400x200')
        self.width_of_window = 400
        self.height_of_window = 200
        self.screen_width = self.int3.winfo_screenwidth()
        self.screen_height = self.int3.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.int3.geometry(
            "%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.bg = PhotoImage(file="Fondo.png")
        self.canvas1 = Canvas(self.int3, width=500,
                              height=200)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.bg,
                                  anchor="nw")
        self.label_explorar = tk.Label(self.int3, font="black", text='Archivo no seleccionado...',
                                       foreground="#12636A", background="white")
        self.label_amstrong = tk.Label(self.int3, font="black", text='Valor Amstrong: ',
                                       foreground="#12636A", background="white")
        self.amstrong = tk.Entry(self.int3, width=10, font="black",
                                 foreground="white", background="#249794", border=False)
        self.btn_explorar = tk.Button(self.int3, text='Abrir Archivo..', command=self.evento_abrir, width=12,
                                      height=1, background="#249794", foreground="white")
        self.btn_cerrar = tk.Button(self.int3, text="Cancelar", command=exit, width=12, height=1,
                                    background="#249794", foreground="white")
        self.btn_guardar = tk.Button(self.int3, text="Guardar", command=self.evento_guardar, width=12, height=1,
                                     background="#249794", foreground="white")
        self.label_explorar.place(x=10, y=20)
        self.label_amstrong.place(x=10, y=100)
        self.amstrong.place(x=285, y=100)
        self.btn_explorar.place(x=285, y=15)
        self.btn_cerrar.place(x=285, y=160)
        self.btn_guardar.place(x=10, y=160)
        self.int3.mainloop()

    def evento_abrir(self):
        filename = filedialog.askopenfilename(initialdir="/", title="Seleccionar un documento",
                                                        filetypes=(
                                                            ("Archivos", "*.txt*"), ("Todos los archivos", "*.*")))
        self.label_explorar.configure(text="Archivo abierto: \n" + filename)

    def evento_guardar(self):
        print("Si guarda")


def main():
    window=Patron()
    return 0

if __name__ == '__main__':
    main()

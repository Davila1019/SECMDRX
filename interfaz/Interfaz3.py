import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# import CargaArchivosChido

def validate(char, entry_value):
    if char in '1234567890.':  # esto es para validar solo numeros escritos aqui
        return True
    else:
        print('invalid: {s}'.format(s=char))
        messagebox.showinfo('Nota', 'Agregar solo números')
        return False

class Interfaz3:
    def __init__(self):
        self.combo_indice = None
        self.int2 = Tk()

        self.int2.overrideredirect(True)  # Quitar barra de título
        # int3.geometry('400x200')
        self.width_of_window = 550
        self.height_of_window = 300
        self.screen_width = self.int2.winfo_screenwidth()
        self.screen_height = self.int2.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.int2.geometry(
            "%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))
        self.bg = PhotoImage(file="Fondo1.png")

        self.canvas1 = Canvas(self.int2, width=500,
                              height=300)
        self.canvas1.pack(fill="both", expand=True)
        self.canvas1.create_image(0, 0, image=self.bg,
                                  anchor="nw")
        bg_azul = '#249794'  # Azul
        self.label_titulo = ttk.Label(self.int2, font="black", text="Agregar picos de difracción ", background="white",
                                      foreground=bg_azul)
        self.btn_agregar = tk.Button(self.int2, text="+", command=self.Evento_agregar, width=4, height=1,
                                     background="#249794", foreground="white")
        self.entry_amstrong = tk.Entry(self.int2, width=10, font="black",
                                       foreground="white", background="#249794", border=False)
        self.label_amstrong = ttk.Label(self.int2, font="black", text="Valor de Amstrong", background="white",
                                        foreground=bg_azul)
        self.btn_aceptar = tk.Button(self.int2, text="Aceptar", command=self.Evento_aceptar, width=12, height=1,
                                     background="#249794", foreground="white")
        self.btn_cancelar = tk.Button(self.int2, text="Cancelar", command=exit, width=12, height=1,
                                      background="#249794", foreground="white")
        # Eliminar Externo
        self.btn_eliminar = tk.Button(self.int2, text="x", command=self.Evento_eliminar, width=4, height=1,
                                      background="#249794", foreground="white")
        # self.Barra = tk.Scale(self.int2, from_=0, to=42)
        # self.Barra.place(x=450,y=50)
        self.posicion = 50
        self.click = 1
        self.btn_agregar.place(x=480, y=10)
        self.label_titulo.place(x=10, y=10)
        self.entry_amstrong.place(x=450, y=220)
        self.label_amstrong.place(x=280, y=220)
        self.btn_aceptar.place(x=447, y=270)
        self.btn_cancelar.place(x=10, y=270)
        self.btn_eliminar.place(x=420, y=10)
        self.int2.mainloop()

    def Evento_agregar(self):
        if self.click == 1:
            vcmd = (self.int2.register(validate), '%S', '%P')
            self.entry_pico = tk.Entry(self.int2, width=10, font="black", foreground="white", background="#249794",
                                       border=False, validate='key', validatecommand=vcmd)

            self.label_pico = tk.Label(self.int2, font='black', text='Angulo del pico', background="white",
                                       foreground="#249794")
            self.label_indice = tk.Label(self.int2, font='black', text='Indice de Miller', background="white",
                                         foreground="#249794")
            self.combo_indice = ttk.Combobox(self.int2,values=["111", "222", "022", "310"], width=10, validate='key', validatecommand=vcmd,state="readonly")
            self.combo_indice.current(0)
            self.label_pico.place(x=10, y=self.posicion)
            self.entry_pico.place(x=140, y=self.posicion)
            self.label_indice.place(x=250, y=self.posicion)
            self.combo_indice.place(x=380, y=self.posicion)
            self.click += 1
            self.posicion += 30
        elif self.click == 2:
            vcmd = (self.int2.register(validate), '%S', '%P')
            self.entry_pico2 = tk.Entry(self.int2, width=10, font="black", foreground="white", background="#249794",
                                        border=False, validate='key', validatecommand=vcmd)
            self.label_pico2 = tk.Label(self.int2, font='black', text='Angulo del pico', background="white",
                                        foreground="#249794")
            self.label_indice2 = tk.Label(self.int2, font='black', text='Indice de Miller', background="white",
                                          foreground="#249794")
            self.combo_indice2 = ttk.Combobox(self.int2, values=["111", "222", "022", "310"], width=10, validate='key',
                                             validatecommand=vcmd, state="readonly")
            self.combo_indice2.current(0)
            self.label_pico2.place(x=10, y=self.posicion)
            self.entry_pico2.place(x=140, y=self.posicion)
            self.label_indice2.place(x=250, y=self.posicion)
            self.combo_indice2.place(x=380, y=self.posicion)
            self.click += 1
            self.posicion += 30
        elif self.click == 3:
            vcmd = (self.int2.register(validate), '%S', '%P')
            self.entry_pico3 = tk.Entry(self.int2, width=10, font="black", foreground="white", background="#249794",
                                        border=False, validate='key', validatecommand=vcmd)
            self.label_pico3 = tk.Label(self.int2, font='black', text='Angulo del pico', background="white",
                                        foreground="#249794")
            self.label_indice3 = tk.Label(self.int2, font='black', text='Indice de Miller', background="white",
                                          foreground="#249794")
            self.combo_indice3 = ttk.Combobox(self.int2, values=["111", "222", "022", "310"], width=10, validate='key',
                                             validatecommand=vcmd, state="readonly")
            self.combo_indice3.current(0)
            self.label_pico3.place(x=10, y=self.posicion)
            self.entry_pico3.place(x=140, y=self.posicion)
            self.label_indice3.place(x=250, y=self.posicion)
            self.combo_indice3.place(x=380, y=self.posicion)
            self.click += 1
            self.posicion += 30
        elif self.click == 4:
            vcmd = (self.int2.register(validate), '%S', '%P')
            self.entry_pico4 = tk.Entry(self.int2, width=10, font="black", foreground="white", background="#249794",
                                        border=False, validate='key', validatecommand=vcmd)
            self.label_pico4 = tk.Label(self.int2, font='black', text='Angulo del pico', background="white",
                                        foreground="#249794")
            self.label_indice4 = tk.Label(self.int2, font='black', text='Indice de Miller', background="white",
                                          foreground="#249794")
            self.combo_indice4 = ttk.Combobox(self.int2, values=["111", "222", "022", "310"], width=10, validate='key',
                                             validatecommand=vcmd, state="readonly")
            self.combo_indice4.current(0)
            self.label_pico4.place(x=10, y=self.posicion)
            self.entry_pico4.place(x=140, y=self.posicion)
            self.label_indice4.place(x=250, y=self.posicion)
            self.combo_indice4.place(x=380, y=self.posicion)
            self.click += 1
            self.posicion += 30
        elif self.click == 5:
            vcmd = (self.int2.register(validate), '%S', '%P')
            self.entry_pico5 = tk.Entry(self.int2, width=10, font="black", foreground="white", background="#249794",
                                        border=False, validate='key', validatecommand=vcmd)
            self.label_pico5 = tk.Label(self.int2, font='black', text='Angulo del pico', background="white",
                                        foreground="#249794")
            self.label_indice5 = tk.Label(self.int2, font='black', text='Indice de Miller', background="white",
                                          foreground="#249794")
            self.combo_indice5 = ttk.Combobox(self.int2, values=["111", "222", "022", "310"], width=10, validate='key',
                                             validatecommand=vcmd, state="readonly")
            self.combo_indice5.current(0)
            self.label_pico5.place(x=10, y=self.posicion)
            self.entry_pico5.place(x=140, y=self.posicion)
            self.label_indice5.place(x=250, y=self.posicion)
            self.combo_indice5.place(x=380, y=self.posicion)
            self.click += 1
            self.posicion += 30

        print("Click Agregar", self.click)

    def Evento_eliminar(self):
        if self.click == 6:
            self.label_pico5.place_forget()
            self.entry_pico5.place_forget()
            self.label_indice5.place_forget()
            self.combo_indice5.place_forget()
            self.click -= 1
            self.posicion -= 30
        elif self.click == 5:
            self.label_pico4.place_forget()
            self.entry_pico4.place_forget()
            self.label_indice4.place_forget()
            self.combo_indice4.place_forget()
            self.click -= 1
            self.posicion -= 30
        elif self.click == 4:
            self.label_pico3.place_forget()
            self.entry_pico3.place_forget()
            self.label_indice3.place_forget()
            self.combo_indice3.place_forget()
            self.click -= 1
            self.posicion -= 30
        elif self.click == 3:
            self.label_pico2.place_forget()
            self.entry_pico2.place_forget()
            self.label_indice2.place_forget()
            self.combo_indice2.place_forget()
            self.click -= 1
            self.posicion -= 30
        elif self.click == 2:
            self.label_pico.place_forget()
            self.entry_pico.place_forget()
            self.label_indice.place_forget()
            self.combo_indice.place_forget()
            self.click -= 1
            self.posicion -= 30

        print("Click eliminar", self.click)

    def Evento_aceptar(self):
        print("Aceptó")


def main():
    window = Interfaz3()
    return 0


if __name__ == '__main__':
    main()

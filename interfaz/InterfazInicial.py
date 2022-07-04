from tkinter import ttk
from tkinter import *
from InterfazSeleccion import VentanaSeleccion

class VentanaInicial:

    def __init__(self):
        self.inicial = Tk()
        self.inicial.withdraw()
        width_of_window = 427
        height_of_window = 250
        self.inicial.title('SECMDRX')
        self.inicial.resizable(False, False)
        self.inicial.iconbitmap("../resourses/images/logo-ipn.ico")
        # Obtenemos altura y anchura de la pantalla
        screen_width = self.inicial.winfo_screenwidth()
        screen_height = self.inicial.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        self.inicial.geometry(
            "%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))


        self.s = ttk.Style()
        self.s.theme_use('clam')




        self.s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
        self.progress = ttk.Progressbar(self.inicial, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500,
                                        mode='determinate', )
        self.progress.place(x=-10, y=235)

        self.a = '#249794'
        # self.bg = PhotoImage(file="Fondo.png")
        # self.canvas1 = Canvas(self.w, width=400,
        #                       height=400)
        #
        # self.canvas1.pack(fill="both", expand=True)
        #
        # self.canvas1.create_image(0, 0, image=self.bg,anchor="nw")

        Frame(self.inicial, width=427, height=241, bg=self.a).place(x=0, y=0)  # 249794
        self.b1 = Button(self.inicial, width=10, height=1, text='Comenzar', command=self.ventana_carga, border=0,
                         fg=self.a, bg='white')
        self.b1.place(x=170, y=200)
        # Label
        #

        self.l1 = Label(self.inicial, text='SECMD', fg='white', bg=self.a)
        self.lst1 = ('Calibri (Body)', 18, 'bold')
        self.l1.config(font=self.lst1)
        self.l1.place(x=20, y=80)

        self.l2 = Label(self.inicial, text='RX', fg='white', bg=self.a)
        self.lst2 = ('Calibri (Body)', 18)
        self.l2.config(font=self.lst2)
        self.l2.place(x=109, y=82)

        self.l3 = Label(self.inicial, text='Simulador de Estructuras Cristalinas Metalicas de Difracción de Rayos X\nInsituto Politecnico Nacional', fg='white',
                        bg=self.a)
        self.lst3 = ('kalinga', 9)
        self.l3.config(font=self.lst3)
        self.l3.place(x=20, y=110)
        self.inicial.deiconify()
        self.inicial.mainloop()

    def ventana_carga(self):
        l4 = Label(self.inicial, text='Cargando...', fg='white', bg=self.a)
        lst4 = ('Calibri (Body)', 10)
        l4.config(font=lst4)
        l4.place(x=18, y=210)
        import time
        r = 0
        for i in range(100):
            self.progress['value'] = r
            self.inicial.update_idletasks()
            time.sleep(0.03)
            r = r + 1
        self.inicial.destroy()
        self.select_window = VentanaSeleccion()

if __name__ == '__main__':
    i = VentanaInicial()
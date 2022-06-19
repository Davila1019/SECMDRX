from tkinter import ttk
from tkinter import *


class Ventana:

    def __init__(self):
        self.w = Tk()
        self.width_of_window = 427
        self.height_of_window = 250
        # Obtenemos altura y anchura de la pantalla
        self.screen_width = self.w.winfo_screenwidth()
        self.screen_height = self.w.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.w.geometry(
            "%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, self.x_coordinate, self.y_coordinate))

        self.w.overrideredirect(1)

        self.s = ttk.Style()
        self.s.theme_use('clam')




        self.s.configure("red.Horizontal.TProgressbar", foreground='red', background='#4f4f4f')
        self.progress = ttk.Progressbar(self.w, style="red.Horizontal.TProgressbar", orient=HORIZONTAL, length=500,
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

        Frame(self.w, width=427, height=241, bg=self.a).place(x=0, y=0)  # 249794
        self.b1 = Button(self.w, width=10, height=1, text='Comenzar', command=self.ventana_carga, border=0,
                         fg=self.a, bg='white')
        self.b1.place(x=170, y=200)
        # Label
        #

        self.l1 = Label(self.w, text='SECMD', fg='white', bg=self.a)
        self.lst1 = ('Calibri (Body)', 18, 'bold')
        self.l1.config(font=self.lst1)
        self.l1.place(x=20, y=80)

        self.l2 = Label(self.w, text='RX', fg='white', bg=self.a)
        self.lst2 = ('Calibri (Body)', 18)
        self.l2.config(font=self.lst2)
        self.l2.place(x=109, y=82)

        self.l3 = Label(self.w, text='Simulador de estrucutras cristalinas de difracción de rayos X', fg='white',
                        bg=self.a)
        self.lst3 = ('kalinga', 9)
        self.l3.config(font=self.lst3)
        self.l3.place(x=20, y=110)
        self.w.mainloop()

    def new_win(self):
        # w.destroy()
        q = Tk()
        q.title('Main window')
        q.geometry('427x250')
        l1 = Label(q, text='ADD TEXT HERE ', fg='grey', bg=None)
        l = ('Calibri (Body)', 24, 'bold')
        l1.config(font=l)
        l1.place(x=80, y=100)
        q.mainloop()

    def ventana_carga(self):
        l4 = Label(self.w, text='Cargando...', fg='white', bg=self.a)
        lst4 = ('Calibri (Body)', 10)
        l4.config(font=lst4)
        l4.place(x=18, y=210)
        import time
        r = 0
        for i in range(100):
            self.progress['value'] = r
            self.w.update_idletasks()
            time.sleep(0.03)
            r = r + 1
        self.w.destroy()
        self.new_win()


def main():
    window = Ventana()
    return 0


if __name__ == '__main__':
    main()

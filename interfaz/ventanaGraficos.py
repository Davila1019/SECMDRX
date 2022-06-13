from tkinter import *
import tkinter as tk

from matplotlib.figure import Figure

from patron_difraccion.Patron_U import Patron_U
from  matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
class ChartWindow():
    def __init__(self):
        self._root = tk.Tk()
        x_ventana = self._root.winfo_screenwidth() // 2 - 900 // 2
        y_ventana = self._root.winfo_screenheight() // 2 - 600 // 2
        posicion = "900x600+"+str(x_ventana)+"+"+str(y_ventana)
        self._root.geometry(posicion)
        self._root.config(bg="#249794")
        self._root.title('SECMDRX')
        #self._root.overrideredirect(True)
        self._root.iconbitmap("../resourses/images/logo-ipn.ico")
        #clase Patron Usuario
        self._difraction = Patron_U()
        self._difraction.load_data() #abrir archivo
        self._difraction.detectar_Picos()

        #Clase isma
        self._difraction.final_ind


        self._root.rowconfigure(0,weight=2)
        self._root.columnconfigure(0,weight=1)

        self.createMenu() # Creamos la barra de menú
        self.createWidgets()

        self._root.mainloop()

    def createMenu(self):
        menubar = Menu(self._root)

        filemenu = Menu(menubar,tearoff=0)
        filemenu.add_command(label="Nueva simulación")
        filemenu.add_command(label="Crear reporte")
        filemenu.add_separator()
        filemenu.add_command(label="Salir",command=self._root.quit)

        helpmenu = Menu(menubar,tearoff=0)
        helpmenu.add_command(label="Manual de usuario")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...")

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Ayuda", menu=helpmenu)

        self._root.config(menu=menubar)



    def createWidgets(self):

        canvas = FigureCanvasTkAgg(self._difraction.plt, self._root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, rowspan=2)

        toolbarFrame = Frame(master=self._root)
        toolbarFrame.grid(row=2,column=0)
        toolbar = NavigationToolbar2Tk(canvas,toolbarFrame)



def main():
    window = ChartWindow()
    return 0

if __name__ == '__main__':
    main()
from tkinter import *
from tkinter.ttk import *
root = Tk()
root.title("SECMDRX")
root.geometry("1250x600")
root.config(bg="#FCFCD5")
root.iconbitmap("../resourses/images/logo-ipn.ico")
miFrame = Frame(root, width="1250", height="600")
miFrame.pack(expand="true")
miLabel = Label(miFrame,text="Simulador De Estructuras Cristalinas Metalicas De Difracción De Rayos X \nInstituto Politecnico Nacional")
miLabel.config(font="Montserrat", justify="center",anchor="center", background="#FCFCD5")
progress = Progressbar(root, orient=HORIZONTAL,length=750, mode='determinate')
def bar():
    import time
    i = 0
    while i < 750:
        if i != 749:
            progress['value'] = i
            root.update_idletasks()
            time.sleep(0.001)
            i += 1
        else:
            progress['value'] = 750
            root.update_idletasks()
            break

progress.pack(pady=50)
miLabel.pack()
bar()
root.mainloop()
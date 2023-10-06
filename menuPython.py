from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x500")
root.title("Menu Basico de Python")
root.resizable(False, False)

def abrirSegundaTela():
    root2 = Tk()
    root2.geometry("1000x1000")
    root2.title("Menu Basico de Python")
    frame2 = ttk.Frame(root2, padding=50)
    label2 = ttk.Label(frame, text="outro", background="blue", font="50", padding="10").grid(column=1, row=0)

frame = ttk.Frame(root, padding=50)

label = ttk.Label(frame, text="Menu InovaAcess", background="blue", font="50").grid(column=0, row=0)

ttk.Button(frame, text="Quit", command=root.destroy).grid(column=5, row=1)

ttk.Button(frame, text="Nova Operação", command = abrirSegundaTela).grid(column=2, row=1)

frame.grid()

root.mainloop()



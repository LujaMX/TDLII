from tkinter import END,messagebox
from tkinter import *
import tkinter as tk


root = tk.Tk()
root.title("Hola mundo")
root.config(width=700, height=500)

tk.Label(root, text="Código: ").place(x=140,y=30)
txtCodigo = Text(root,width=30, height=10)
txtCodigo.place(x=50,y=50)


btnMostrar=tk.Button(root,text= "Mostrar")
btnMostrar.place(x=320,y=120)
root.mainloop()

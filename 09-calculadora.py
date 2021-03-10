"""
CALCULADORA:
    - Dos campos de texto
    - 4 botones para las operaciones aritméticas
    - Mostrar resultado en una alerta
"""
from tkinter import *
from tkinter import messagebox as MessageBox


ventana = Tk()
ventana.title("Calculadora básica usando Tkinter")
ventana.config(
    bd = 25
)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

Label(ventana,text="Primer Número: ").pack()
Entry(ventana, textvariable=numero1)

Label(ventana,text="Segundo Número: ").pack()
Entry(ventana, textvariable=numero2)
Label(ventana, text="")
Button(ventana,text="Sumar").pack(side="left")
Button(ventana,text="Restar").pack(side="left")
Button(ventana,text="Multiplicar").pack(side="left")
Button(ventana,text="Dividir").pack(side="left")


ventana.mainloop()
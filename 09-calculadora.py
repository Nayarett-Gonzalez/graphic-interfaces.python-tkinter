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
ventana.geometry("400x400")
ventana.config(
    bd = 25
)

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()


marco = Frame(ventana,width=250,height=250)
marco.config(
    bd=5,
    relief=SOLID,
    padx=15,
    pady=15
)
marco.pack(side=TOP,anchor=CENTER)
marco.pack_propagate(False)

Label(marco,text="Primer Número: ").pack()
Entry(marco, textvariable=numero1,justify="center").pack()

Label(marco,text="Segundo Número: ").pack()
Entry(marco, textvariable=numero2,justify="center").pack()
Label(marco, text="")

Button(marco,text="Sumar").pack(side="left",fill=X, expand=YES)
Button(marco,text="Restar").pack(side="left",fill=X, expand=YES)
Button(marco,text="Multiplicar").pack(side="left",fill=X, expand=YES)
Button(marco,text="Dividir").pack(side="left",fill=X, expand=YES)



ventana.mainloop()
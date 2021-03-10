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
def sumar():
    resultado.set(float(numero1.get())+float(numero2.get()))
    mostrarResultado()

def restar():
    resultado.set(float(numero1.get())-float(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(float(numero1.get())*float(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(float(numero1.get())/float(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    MessageBox.showinfo("Resultado", f"El resultado de la operación es {resultado.get()}")
    # Borramos los números ingresados despues de realizar alguna de las operaciones
    numero1.set("")
    numero2.set("")






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

Button(marco,text="Sumar",command=sumar).pack(side="left",fill=X, expand=YES)
Button(marco,text="Restar",command=restar).pack(side="left",fill=X, expand=YES)
Button(marco,text="Multiplicar",command=multiplicar).pack(side="left",fill=X, expand=YES)
Button(marco,text="Dividir",command=dividir).pack(side="left",fill=X, expand=YES)



ventana.mainloop()
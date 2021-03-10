from tkinter import *
from tkinter import messagebox as MessageBox

ventana= Tk()
ventana.config(
    bd=70
)

def sacarAlerta():
    # MessageBox.showinfo("Alerta", "Hola soy Pilar")
    #  MessageBox.showwarning("Alerta", "Hola soy Pilar")
    MessageBox.showerror("Alerta", "ERROR")
def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Quieres seguir ejecutando la aplicación")
    if resultado != "yes":
        MessageBox.showinfo("Chaoooo", f"Adios {nombre}")
        ventana.destroy()
# La función cuando se llama con command no lleva paréntesis
Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()


# La función cuando se llama con command no lleva paréntesis
Button(ventana, text="Salir", command=lambda:salir("Pilar")).pack()

ventana.mainloop()
from tkinter import *

ventana= Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter | Pilar Goonzález")


# Texto Encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Pilar G")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans",18),
    padx=10,
    pady=10
)

encabezado.pack(side=LEFT, anchor=NW)

ventana.mainloop()
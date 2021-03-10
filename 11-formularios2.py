from tkinter import *

ventana = Tk()
ventana.geometry("800x300")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    bg="green",
    fg="white",
    font=("Consolas",20)
)

encabezado.pack(side=TOP,anchor=N,fill=X,expand=YES)

# Botones check
# Radio buttons
# Option Menu

ventana.mainloop()
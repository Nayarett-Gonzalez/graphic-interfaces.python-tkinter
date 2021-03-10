from tkinter import *

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    padx=15,
    pady=15,
    bg="green",
    fg="white",
    font=("Consolas",20)
)

# encabezado.pack(side=TOP,anchor=N,fill=X,expand=YES)
encabezado.grid(row=0,column=0,columnspan=5,sticky=W)

def mostrarProfesion():
    texto=""

    if web.get():
        texto += "Desarrollo web"

    if movil.get():
        if web.get():
            texto += " y desarrollo móvil"
        else:
            texto += "Desarrollo móvil"

    mostrar.config(text=texto,bg="green",fg="white")

web=IntVar()
movil=IntVar()
# Botones check (checkbox en HTML)
# Label(ventana,text="¿A qué te dedicas?").pack()
Label(ventana,text="¿A qué te dedicas?").grid(row=1,column=0,sticky=W)
Checkbutton(ventana, text="Desarrollo web",variable=web, onvalue=1,offvalue=0,command=mostrarProfesion).grid(row=2,column=0,sticky=W)
Checkbutton(ventana, text="Desarrollo móvil",variable=movil, onvalue=1, offvalue=0,command=mostrarProfesion).grid(row=3,column=0,sticky=W)


mostrar = Label(ventana)
mostrar.grid(row=4,column=0)

# Radio buttons

def marcar():
    marcado.config(
        # text=opcion.get()
        text=""
    )
opcion =StringVar()
opcion.set(None)

Label(ventana,text="¿Cuál es tu género?").grid(row=5)
Radiobutton(ventana,text="Masculino",value="Masculino",variable=opcion,command=marcar).grid(row=6)
Radiobutton(ventana,text="Femenino",value="Femenino",variable=opcion,command=marcar).grid(row=7)
marcado =Label(ventana)
marcado.grid(row=8)


# Option Menu

ventana.mainloop()
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
# Grid de 12 columnas(en el columnspan inicial)
encabezado.grid(row=0,column=0,columnspan=12,sticky=W)

# Label para el campo (nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1,column=0,sticky=W,padx=5, pady=5)

# Campo de texto (nombre)
campo_texto = Entry(ventana)
# sticky fija el campo de texto a la izquierda
campo_texto.grid(row=1,column=1,sticky=W,padx=5,pady=5)
campo_texto.config(justify="right",state="normal")

# Label para el campo (apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2,column=0,sticky=W,padx=5, pady=5)
# Campo de texto (apellidos)
campo_texto = Entry(ventana)
# sticky fija el campo de texto a la izquierda
campo_texto.grid(row=2,column=1,sticky=W,padx=5,pady=5)
# Justificado derecha; el texto ingresado aparece desde la derecha, state: disabled (ex)
campo_texto.config(justify="right",state="normal")

# Label para el campo (descripción)
label = Label(ventana, text="Descripción")
label.grid(row=3,column=0,sticky=W,padx=5, pady=5)

# Campo de texto GRANDE (descripción)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1,sticky=N,padx=5, pady=5)
campo_grande.config(
    width=30,
    height=5,
    font=("Arial",12),
    padx=15,
    pady=15
)

ventana.mainloop()
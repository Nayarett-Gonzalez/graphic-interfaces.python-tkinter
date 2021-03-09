from tkinter import *

ventana = Tk()

ventana.title("Marcos | Master en Python")
ventana.geometry("500x500")

# Marco padre superior
marco_padre = Frame(ventana, width=250,height=250)
# marco_padre.config(
#     bg="lightblue",
#     # bd=5,
#     # relief= SOLID
# )
marco_padre.pack(side=TOP,anchor=N,fill=X, expand=YES) # Necesario para que se vea el marco

# Marco 1 superior
marco = Frame(marco_padre, width=150,height=150)
marco.config(
    bg="red",bd=2,
    # relief=SOLID
    relief="raised"
)
marco.pack(side=LEFT) # Necesario para que se vea el marco
# Para que no se alteren las dimensiones del marco con el texto que se le incluirá
marco.pack_propagate(False)

# Para incluir texto
texto = Label(marco,text="Primer Marco")
texto.config(
    bg = "red",
    fg = "white",
    # padx=15,
    # pady=15,
    font = ("Arial",10),
    height=10,
    width=10,
    # bd=1,
    # relief=SOLID,
)
texto.pack(anchor=CENTER,fill=Y, expand=YES)


# Marco 2 superior
marco = Frame(marco_padre, width=150,height=150)
marco.config(
    bg="green",bd=2,
    relief=SOLID
)
marco.pack(side=RIGHT) # Necesario para que se vea el marco
# Para que no se alteren las dimensiones del marco con el texto que se le incluirá
marco.pack_propagate(False)
# Para incluir texto
Label(marco,text="Segundo Marco").pack(side=TOP,anchor=NE)

######################################################
# Marco Padre Inferior
marco_padre = Frame(ventana, width=150,height=150)
# marco_padre.config(
#     bg="#199845"
#     # bd=5,
#     # relief="raised"
# )
marco_padre.pack(side=BOTTOM,anchor=S,fill=X, expand=YES) # Necesario para que se vea el marco

# Marco 3 
marco = Frame(marco_padre, width=150,height=150)
marco.config(
    bg="blue",bd=2,
    relief=SOLID
)
marco.pack(side=LEFT) # Necesario para que se vea el marco
# Para que no se alteren las dimensiones del marco con el texto que se le incluirá
marco.pack_propagate(False)
# Para incluir texto
Label(marco,text="Tercer Marco").pack(side=BOTTOM,anchor=SW)

# Marco 4 
marco = Frame(marco_padre, width=150,height=150)
marco.config(
    bg="pink",bd=2,
    relief=SOLID
)
marco.pack(side=RIGHT) # Necesario para que se vea el marco
# Para que no se alteren las dimensiones del marco con el texto que se le incluirá
marco.pack_propagate(False)
# Para incluir texto
Label(marco,text="Cuarto Marco").pack(side=BOTTOM,anchor=SE)
ventana.mainloop()
from tkinter import *

ventana = Tk()

ventana.title("Marcos | Master en Python")
ventana.geometry("700x700")

# Marco padre superior
marco_padre = Frame(ventana, width=250,height=250)
# marco_padre.config(
#     bg="lightblue",
#     # bd=5,
#     # relief= SOLID
# )
marco_padre.pack(side=TOP,anchor=N,fill=X, expand=YES) # Necesario para que se vea el marco

# Marco 1 superior
marco = Frame(marco_padre, width=250,height=250)
marco.config(
    bg="red",bd=2,
    # relief=SOLID
    relief="raised"
)
marco.pack(side=LEFT) # Necesario para que se vea el marco

# Marco 2 superior
marco = Frame(marco_padre, width=250,height=250)
marco.config(
    bg="green",bd=2,
    relief=SOLID
)
marco.pack(side=RIGHT) # Necesario para que se vea el marco

# Marco Padre Inferior
marco_padre = Frame(ventana, width=250,height=250)
# marco_padre.config(
#     bg="#199845"
#     # bd=5,
#     # relief="raised"
# )
marco_padre.pack(side=BOTTOM,anchor=S,fill=X, expand=YES) # Necesario para que se vea el marco

# Marco 3 
marco = Frame(marco_padre, width=250,height=250)
marco.config(
    bg="blue",bd=2,
    relief=SOLID
)
marco.pack(side=RIGHT) # Necesario para que se vea el marco

# Marco 4 
marco = Frame(marco_padre, width=250,height=250)
marco.config(
    bg="pink",bd=2,
    relief=SOLID
)
marco.pack(side=LEFT) # Necesario para que se vea el marco


ventana.mainloop()
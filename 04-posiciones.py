from tkinter import *

ventana = Tk()
# ventana.geometry("700x500")
# Keyword parameter;keyword arguments
texto = Label(ventana,text="Bienvenido a mi programa")

# Parámetro fg=foreground
texto.config(
            fg = "white",
            bg ="#000000",
            padx=50, # Padding
            pady=20,
            font=("Consolas",30))
# Para mostrar cargar dentro de la ventana
texto.pack(side = TOP)

texto = Label(ventana,text="Estudiando")
texto.config(
            height=3,
            bg="red",
            font = ("Arial,18"),
            padx = 10,
            pady = 20,
            cursor ="spider")
texto.pack(side = TOP, fill = X, expand =YES)



texto = Label(ventana,text="Python") 
texto.config(
            height=3,
            bg="green",
            font = ("Arial,18"),
            padx = 10,
            pady = 20,
            cursor ="spider")
texto.pack(side=LEFT, fill = X, expand =YES)


texto = Label(ventana,text="Python")
texto.config(
            height=3,
            bg="yellow",
            font = ("Arial,18"),
            padx = 10,
            pady = 20,
            cursor ="spider")
texto.pack(side=LEFT, fill = X, expand =YES)

texto = Label(ventana,text="Python")
texto.config(
            height=3,
            bg="orange",
            font = ("Arial,18"),
            padx = 10,
            pady = 20,
            cursor ="spider")
texto.pack(side=LEFT, fill = X, expand =YES)


ventana.mainloop()
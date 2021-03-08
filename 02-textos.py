from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
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
texto.pack()

texto = Label(ventana,text="Estudiando")
texto.config(
            height=13,
            bg="red",
            font = ("Arial,18"),
            padx = 10,
            pady = 20,
            cursor ="spider")
texto.pack(anchor=SE)

def pruebas(nombre,apellidos, pais):
    return f"Hola {nombre} {apellidos}, noto que eres de  {pais}"


texto = Label(ventana,text=pruebas(nombre="Pilar",apellidos="González",pais="Chile")) #Puedo cambiar el orden de los parámetros en el método pruebas
texto.config(
            height=3,
            bg="green",
            font = ("Arial,18"),
            padx = 10,
            pady = 20,
            cursor ="spider")
texto.pack(anchor=NW)


texto = Label(ventana,text="Con Pilar")
texto.config(
            height=400,
            bg="orange",
            font = ("Arial,18"),
            padx = 10,
            pady = 20,
            cursor ="spider")
texto.pack(anchor=NW)

ventana.mainloop()
"""
Módulo para crear interfaces gráficas de usuario
"""
from tkinter import *
import os.path

# Crear ventana raíz (principal)
ventana = Tk()

# Colocando título de la ventana
ventana.title("Interfaz gráfica")

# Comprobar si existe archivo de ícono
ruta_icono = os.path.abspath(("./images/favicon.ico"))
if not os.path.isfile(ruta_icono):
    ruta_icono = os.path.abspath(("./images/favicon.ico"))

# Mostrar texto en el programa
texto = Label(ventana,text=ruta_icono)
texto.pack()

# Colocando un favicon a la ventana
ventana.iconbitmap(ruta_icono)

# Establezco el tamaño inicial de la ventana
ventana.geometry("750x450")

# Bloquear el tamaño de la ventana - No permite redimensionar la ventana
ventana.resizable(0,0)

# Puedo modificar el ancho de la ventana
ventana.resizable(0,1)

# Puedo modificar el alto de la ventana
ventana.resizable(1,0)
# Activar y mostrar la ventana hasta que se cierre - Este método debe activarse al final
ventana.mainloop()
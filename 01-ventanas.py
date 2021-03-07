"""
Módulo para crear interfaces gráficas de usuario
"""
from tkinter import *
# Crear ventana raíz (principal)
ventana = Tk()

# Colocando título de la ventana
ventana.title("Interfaz gráfica")

# Colocando un favicon a la ventana
ventana.iconbitmap("./images/favicon.ico")

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
from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = "Estudiando Python"
        self.icon = "./images/favicon.ico"
        self.icon_alt = "./images/favicon.ico"
        self.size = "770x470"
        self.resizable = False
    
    def cargar(self):
        ventana = Tk()
        self.ventana = ventana
        ventana.title(self.title)

        ruta_icono = os.path.abspath((self.icon))

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath((self.icon_alt))


        texto = Label(ventana,text=ruta_icono)
        texto.pack()
         # Establezco el tamaño inicial de la ventana
        ventana.geometry(self.size)
        # Colocando un favicon a la ventana
        ventana.iconbitmap(ruta_icono)

  

        if self.resizable:
            ventana.resizable(1,1)
        else:
            ventana.resizable(0,0)

    
    def addTexto(self,dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()

# Instanciando el objeto
programa = Programa()
programa.cargar()

programa.addTexto("Hola")

programa.addTexto("Soy un texto")
programa.addTexto("Bienvenido")
programa.addTexto("Soy Pili")
programa.addTexto("Sígueme en github")

programa.mostrar()
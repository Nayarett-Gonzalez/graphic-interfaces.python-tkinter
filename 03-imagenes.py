from tkinter import *
from PIL import Image,ImageTk

ventana = Tk()
ventana.geometry("700x500")

Label(ventana,text="Hola, soy Pilar!!!").pack(anchor=W)

image =Image.open("./images/blueToat.jpg")
render =ImageTk.PhotoImage(image)

Label(ventana, image=render).pack(anchor=E)



ventana.mainloop()
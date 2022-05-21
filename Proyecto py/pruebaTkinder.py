from tkinter import *

class Alumno: #se crea una clase
    def __init__(self,ventana): #se define una ventana
        self.ventana=ventana
        self.ventana.title("Hola mundo")
if __name__=="__main__": #que este script sea el principal
    ventana=Tk()
    aplicacion=Alumno(ventana)
    ventana.mainloop() #ciclo principal. Que refesca la ventana si hay un cambio.


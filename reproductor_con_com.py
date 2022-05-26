#Reproductor musica
#Importar librerias
from tkinter import* #tkinter funciona para la creacion de una interfaz grafica.
from tkinter import filedialog #Esta funcion nos permite abrir una carpeta(En este caso para abrir la la ubicacion de la musica)
from pygame import mixer  #Pygame sirve para cargar musica, reproducir sonidos y mezclador de sonidos.
#Definimos las caractisristicas de los botones y en que parte de la vantana se van a ubicar
class musica:
    def __init__(self,ventana): #_init_ sirve para Inicializar la ventana.
        ventana.geometry("280x300") #La variable "geometry" permite establecer el tamaño de la ventana emergente.
        ventana.title("Reproductor") #Titulo de la ventana.
        ventana.config(bg="#8F9CDA",bd="25") #Caracteristicas del fondo de la ventana. Marco de la ventana.

        ab=Button(ventana,text="Abrir",width=10,bg="#0a5cb8",relief="groove",bd="4",command=self.abrir)
        #la variable self, nos permite especificar y acceder a los atributos y metodos de la clase especificada
        ab.place(x=70,y=50)
        rep=Button(ventana,text="Reproducir",width=10,bg="#7f00b2",relief="groove",bd="4",command=self.reproducir)
        rep.place(x=70,y=90)
        pa=Button(ventana,text="Pausa",width=10,bg="#a21ad7",relief="groove",bd="4",command=self.pausa)
        pa.place(x=70,y=130)
        sg=Button(ventana,text="siguiente",width=10,bg="blue",relief="groove",bd="4",command=self.sigiente)
        sg.place(x=70,y=170)
        self.abri_musica=False 
        self.repro_musica=False #utilizamos el booleano "False", para que la musica no inicie cuando no le indicamo

    #Funciones
    #Programamos las funciones de cada boton y que tienen que hacer cada uno 
    def abrir(self):
        self.abri_musica=filedialog.askopenfilename()
    def reproducir(self):
        if self.abri_musica:
            mixer.init()
            mixer.music.load(self.abri_musica)
            mixer.music.play()
    def pausa(self):
        if self.repro_musica:
            mixer.music.pause()
            self.repro_musica=False
        else:
            mixer.music.unpause()
            self.repro_musica=True

ventana=Tk()
musica(ventana)#llamamos la clase junto con sus funciones, para que se ejecuten
ventana.mainloop()
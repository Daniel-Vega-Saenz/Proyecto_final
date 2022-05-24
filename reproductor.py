#Reproductor musica
#Importar librerias
from tkinter import* #tkinter funciona para la creacion de una interfaz grafica.
from tkinter import filedialog 
from pygame import mixer  #Pygame sirve para cargar musica, reproducir sonidos y mezclador de sonidos.

class musica:
    def __init__(self,ventana): #_init_ sirve para Inicializar la ventana.
        ventana.geometry("270x300") #Tamaño de la ventana emergente.
        ventana.title("Reproductor") #Titulo de la ventana.
        ventana.config(bg="#0069c0",bd="25") #Caracteristicas del fondo de la ventana. Marco de la ventana.

        abrir=Button(ventana,text="Abrir",width=10,bg="#2196f3",relief="groove",bd="4",command=abrir)
        abrir.place(x=60,y=50)
        reproducir=Button(ventana,text="Reproducir",width=10,bg="#7f00b2",relief="groove",bd="4",command=reproducir)
        reproducir.place(x=60,y=90)
        pause=Button(ventana,text="Pausa",width=10,bg="#ab3ed8",relief="groove",bd="4",command=pause)
        pause.place(x=60,y=130)
        self.abri_musica=False
        self.repro_musica=False

        def abrir(self):
            self.abri_musica=filedialog.askopenfilename()
        def reproducir(self):
            if self.abri_musica:
                mixer.music.load(self.abri_musica)
                mixer.music.play()
        def pause(self):
            if self.repro_musica:
                mixer.musica.pause()
                self.repro_musica=False
            else:
                mixer.music.unpause()
                self.repro_musica=True


ventana=Tk()
musica(ventana)
ventana.mainloop()
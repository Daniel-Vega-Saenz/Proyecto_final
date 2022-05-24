#Reproductor musica
#Importar librerias
from tkinter import* #tkinder nos sirve para crear la interface.
from tkinter import filedialog
from pygame import mixer

class musica:
    def __init__(self,ventana):
        ventana.geometry("270x300")
        ventana.title("Reproductor")
        ventana.config(bg="gray",bd="25")

        abrir=Button(ventana,text="Abrir",width=10,bg="yellow",relief="groove",bd="4")
        abrir.place(x=60,y=50)
        reproducir=Button(ventana,text="Reproducir",width=10,bg="blue",relief="groove",bd="4")
        reproducir.place(x=60,y=90)
        pause=Button(ventana,text="Pausa",width=10,bg="red",relief="groove",bd="4")
        pause.place(x=60,y=130)
        detener=Button(ventana,text="Detener",width=10,bg="white",relief="groove",bd="4")
        detener.place(x=60,y=170)
        self.abri_musica=False
        self.repro_musica=False

        def abrir(self):
            self.abri_musica=filedialog.askopenfilename()
        def reproducir(self):
            if self.abri_musica:
                mixer.music.load(self.abri_musica)
                mixer.music.play()
        def pausar(self):
            if self.repro_musica:
                mixer.musica.pause()
                self.repro_musica=False
            else:
                mixer.music.unpause()
                self.repro_musica=True
        def detener(self):
            mixer.music.stop()

ventana=Tk()
musica(ventana)
ventana.mainloop()
#Reproductor musica
#Importar librerias
from tkinter import* 
from tkinter import filedialog 
from pygame import mixer  

class musica:
    def __init__(self,ventana): 
        ventana.geometry("280x300") 
        ventana.title("Reproductor") 
        ventana.config(bg="#8F9CDA",bd="25") 

        ab=Button(ventana,text="Abrir",width=10,bg="#0a5cb8",relief="groove",bd="4",command=self.abrir)
        ab.place(x=70,y=50)
        rep=Button(ventana,text="Reproducir",width=10,bg="#7f00b2",relief="groove",bd="4",command=self.reproducir)
        rep.place(x=70,y=90)
        pa=Button(ventana,text="Pausa",width=10,bg="#a21ad7",relief="groove",bd="4",command=self.pausa)
        pa.place(x=70,y=130)
        sg=Button(ventana,text="siguiente",width=10,bg="blue",relief="groove",bd="4",command=self.sigiente)
        sg.place(x=70,y=170)
        self.abri_musica=False 
        self.repro_musica=False 

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
    def siguiente():
        #obtenerel numero de cancion que esta sonando
        proxima=ventana.curselection()
        proxima=proxima[0]=1
        cancion=ventana.get(proxima)
        cancion=f"{cancion}.MP3"
        cancion=f"{cancion}."
       
        
ventana=Tk()
musica(ventana)
ventana.mainloop()
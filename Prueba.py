
from cgi import parse_multipart
from tkinter import* 
from tkinter import filedialog 
import pygame
ventana=Tk() 
ventana.geometry("500x300") 
ventana.title("SpotyEan") 
ventana.config(bg="#8F9CDA",bd="25") 
pygame.mixer.init()

def añadir():
    canciones=filedialog.askopenfilenames(filetypes=(("mp3","*.mp3"),("all files","*.*")))
    for cancion in canciones:
        cancion=cancion.replace("C:/Users/dinel/Escritorio/Musica","")
        cancion=cancion.replace(".mp3","")

        pantalla.insert(END, cancion)

def play():
    cancion=pantalla.get(ACTIVE)
    cancion=f"{cancion}.mp3"
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

def stop():
    pygame.mixer.stop()
    pantalla.selection_clear(ACTIVE)

def siguiente():
    proxima=pantalla.curselection()
    proxima=proxima[0]+1
    cancion=pantalla.get(proxima)
    cancion=f"{cancion}.mp3"
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

    pantalla.selection_clear(0,END)
    pantalla.activate(proxima)
    last= None
    pantalla.selection_set(proxima,last)

def anterior():
    proxima=pantalla.curselection()
    proxima=proxima[0]-1
    cancion=pantalla.get(proxima)
    cancion=f"{cancion}.mp3"
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

    pantalla.selection_clear(0,END)
    pantalla.activate(proxima)
    last= None
    pantalla.selection_set(proxima,last)
global pausar
pausar=False
def pausa():
    global pausar
    if pausar:
        pygame.mixer.music.unpause()
        pausar=False
    else:
        pygame.mixer.music.pause()
        pausar=True

pantalla=Listbox(bg="#FF5733", fg="blue",width=60,selectbackground="white", selectforeground="black")
pantalla.pack(pady=20)
ag=Button(ventana,text="Abrir",width=10,bg="red",relief="groove",bd="4",command=añadir)
ag.place(x=1,y=190)
rep=Button(ventana,text="Reproducir",width=10,bg="#7f00b2",relief="groove",bd="4",command=play)
rep.place(x=100,y=190)
ant=Button(ventana,text="Anterior",width=10,bg="#a21ad7",relief="groove",bd="4",command=anterior)
ant.place(x=199,y=190)
sg=Button(ventana,text="Siguiente",width=10,bg="blue",relief="groove",bd="4",command=siguiente)
sg.place(x=298,y=190)
pa=Button(ventana,text="Pausa",width=10,bg="white",relief="groove",bd="4",command=pausa)
pa.place(x=397,y=190)
ventana.mainloop()

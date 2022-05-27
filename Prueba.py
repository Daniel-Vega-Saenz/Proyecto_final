#Reproductor de Música
#Importar librerias
from tkinter import* #tkinter funciona para la creacion de una interfaz grafica.
from tkinter import filedialog #Esta funcion nos permite abrir una carpeta(En este caso para abrir la la ubicacion de la musica)
import pygame#Pygame sirve para cargar musica, reproducir sonidos y mezclador de sonidos.

ventana=Tk() #Iniciamos una ventana que es la interface
ventana.geometry("500x300") #La variable "geometry" permite establecer el tamaño de la ventana emergente.
ventana.title("SpotyEan") #Titulo de la ventana.
ventana.config(bg="#191414",bd="25") #Caracteristicas del fondo de la ventana. Marco de la ventana.
pygame.mixer.init() #_init_ sirve para Inicializar la ventana.

def añadir(): #Se define variable para agregar musica.
    canciones=filedialog.askopenfilenames(filetypes=(("mp3","*.mp3"),("all files","*.*"))) #Funcion para buscar tipos de archivo en especifico.
    for cancion in canciones:
        cancion=cancion.replace(".mp3","") #Añadir canciones .mp3

        pantalla.insert(END, cancion)#Añadir el nombre del archivo que se añadio.

def play():
    cancion=pantalla.get(ACTIVE) #Devuelve un booleano cuando la cancion comienza su reproduccion.
    cancion=f"{cancion}.mp3" #Concatenar el nombre del archivo con .mp3
    pygame.mixer.music.load(cancion) #Cargar la cancion
    pygame.mixer.music.play() #Reproducir la cancion.

def siguiente():
    proxima=pantalla.curselection() #Seleccionar un elemento y tomarlo como la primera posicion.
    proxima=proxima[0]+1 #Se suma 1 a la posicion actual para poder cambiar la cancion.
    cancion=pantalla.get(proxima) #Cambia el booleano para cambiar a la siguiente cancion. 
    cancion=f"{cancion}.mp3" # Concatenar.
    pygame.mixer.music.load(cancion) #Cargar la siguente cancion.
    pygame.mixer.music.play() #Reproducir la siguiente cancion.

    pantalla.selection_clear(0,END)
    pantalla.activate(proxima)
    last= None 
    pantalla.selection_set(proxima,last)

def anterior():
    proxima=pantalla.curselection() #Seleccionar un elemento y tomarlo como la primera posicion.
    proxima=proxima[0]-1 #Se resta 1 a la posicion actual para poder cambiar la cancion.
    cancion=pantalla.get(proxima) #Cambia el booleano para cambiar a la siguiente cancion. 
    cancion=f"{cancion}.mp3" # Concatenar.
    pygame.mixer.music.load(cancion) #Cargar la siguente cancion
    pygame.mixer.music.play() #Reproducir la siguiente cancion.

    pantalla.selection_clear(0,END)
    pantalla.activate(proxima)
    last= None
    pantalla.selection_set(proxima,last)
global pausar #Se declara a pausa una varible global, para usarla en cualquier lugar del programa
pausar=False #Empieza en false para que no pause al iniciar la reproduccion.
def pausa():
    global pausar
    if pausar:
        pygame.mixer.music.unpause()
        pausar=False
    else:
        pygame.mixer.music.pause()
        pausar=True

pantalla=Listbox(bg="#1db954", fg="blue",width=60,selectbackground="white", selectforeground="black") #Se hace una listbox para poder visualisar las canciones de la mejor manera
pantalla.pack(pady=20)
ag=Button(ventana,text="Abrir",width=10,bg="#FFFFFF",relief="groove",bd="4",command=añadir) #Boton para llamar a la definicion de añadir.
ag.place(x=1,y=190) #Posicion de los botones con respecto a la pagina.
rep=Button(ventana,text="Reproducir",width=10,bg="#46cacc",relief="groove",bd="4",command=play) #Boton para llamar a la definicion de reproducir.
rep.place(x=100,y=190) #Posicion de los botones con respecto a la pagina.
ant=Button(ventana,text="Anterior",width=10,bg="#63bccc",relief="groove",bd="4",command=anterior) #Boton para llamar a la definicion de Anterior.
ant.place(x=199,y=190) #Posicion de los botones con respecto a la pagina.
sg=Button(ventana,text="Siguiente",width=10,bg="#cdb3d6",relief="groove",bd="4",command=siguiente) #Boton para llamar a la definicion de siguiente.
sg.place(x=298,y=190) #Posicion de los botones con respecto a la pagina.
pa=Button(ventana,text="Pausa",width=10,bg="#e7b7c7",relief="groove",bd="4",command=pausa) #Boton para llamar a la definicion de pausa.
pa.place(x=397,y=190) #Posicion de los botones con respecto a la pagina.
ventana.mainloop() #Hace que la ventana se quede abierta hasta que el usuario haga algo.

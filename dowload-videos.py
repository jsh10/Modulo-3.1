from logging import root
from pytube import YouTube
from tkinter import *

def accion():
    enlace=videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

root = Tk()
root.config(bd=20)
root.title("Descargar videos")

videos = Entry(root)
videos.grid(row=2, column=2)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=3)

root.mainloop()
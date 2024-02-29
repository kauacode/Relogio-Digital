from tkinter import *
from datetime import datetime

import pyglet

pyglet.font.add_file("C:\Users\kauab\OneDrive\Documentos\relogio\digital-7.ttf")

cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca

janela = Tk()
janela.title("")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor1)

def relogio():
    tempo = datetime.now()

    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")

    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, text="", font=("digital-7", 80), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="", font=("digital-7", 20), bg=cor1, fg=cor2)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()

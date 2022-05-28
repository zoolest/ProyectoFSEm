#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------
# 
# AUTORES
# Amezaga Campos Salvador
# González Cortés Jessica Alejandra
# Lincence: MIT
#
#------------------------------------------------

from tkinter import *
from tkinter import ttk
import os
import threading

#Función iniciar y ejecutar el emulador con el juego seleccionado
#------------------------------------------------
def games(game):
    os.system("mednafen /etc/RetroGaming/roms/" + game)
#------------------------------------------------

# Esta funcion reproduce el sonido seleccionado al iniciar el programa
#------------------------------------------------
def sonido():
    os.system("play /etc/RetroGaming/Audio.mp3")

threading.Thread(target=sonido).start()

os.system("xrandr -s 1152x864")
#------------------------------------------------

# Esta funcion perimite salir
#------------------------------------------------
def salir():
    os.system("sudo shutdown now")
#------------------------------------------------

#Con tkinter construimos la interfaz grafica
#------------------------------------------------
raiz = Tk()
raiz.title("RETRO GAMING")
raiz.attributes("-fullscreen",True)
raiz.resizable(1,1)
raiz.config(bg="azure")
#------------------------------------------------

#Imagen que se colocara en el background del programa
imagen = PhotoImage(file="/etc/RetroGaming/Background.png")
Label(raiz, image=imagen, bd=0).pack()

# Botones que perimitirán la ejecución de cada uno de los juegos
#----------------------------------------------------------------------------------------------
Button(raiz,text="Hamtaro"           ,bg='red', fg= 'azure',command=lambda:games("Hamtaro.gbc")                                       ,width=15).place(x=400,y=100,anchor="center")#SI
Button(raiz,text="Bubble Bobble"    ,bg='red', fg= 'azure',command=lambda:games("BubbleBobble.gbc")                                 ,width=15).place(x=800,y=100,anchor="center")
Button(raiz,text="HarryPotter"           ,bg='red',  fg= 'azure',command=lambda:games("HarryPotter.gbc")                                ,width=15).place(x=400,y=150,anchor="center")
Button(raiz,text="Toy Story 2"           ,bg='red', fg= 'azure',command=lambda:games("ToyStory2.gbc")                                       ,width=15).place(x=800,y=150,anchor="center") #SI
Button(raiz,text="Kirby"            ,bg='red', fg= 'azure',command=lambda:games("KoroKoroKirby.gbc")                                ,width=15).place(x=400,y=200,anchor="center") #SI
Button(raiz,text="Mega Man"         ,bg='red',fg= 'azure',command=lambda:games("MegaManXtreme.gbc")                                ,width=15).place(x=800,y=200,anchor="center") #SI
Button(raiz,text="Monopoly"         ,bg='red', fg= 'azure',command=lambda:games("Monopoly.gbc")                                     ,width=15).place(x=400,y=250,anchor="center")
Button(raiz,text="Pokemon Red"      ,bg='red', fg= 'azure',command=lambda:games("PokemonRed.gb")                                    ,width=15).place(x=800,y=250,anchor="center")
Button(raiz,text="Looney Tunes"   ,bg='red',fg= 'azure',command=lambda:games("LooneyTunes.gbc")                         ,width=15).place(x=400,y=300,anchor="center")
Button(raiz,text="Resident Evil"    ,bg='red',fg= 'azure',command=lambda:games("ResidentEvilGaiden.gbc")                           ,width=15).place(x=800,y=300,anchor="center") #SI
Button(raiz,text="Shantae"          ,bg='red',fg= 'azure',command=lambda:games("Shantae.gbc")                                      ,width=15).place(x=400,y=350,anchor="center")
Button(raiz,text="Simpsons"         ,bg='red',fg= 'azure',command=lambda:games("SimpsonsThe-NightoftheLivingTreehouseofHorror.gbc"),width=15).place(x=800,y=350,anchor="center")
Button(raiz,text="Super Mario World",bg='red',fg= 'azure',command=lambda:games("Super_Mario_World.smc")                            ,width=15).place(x=400,y=400,anchor="center") #SI
Button(raiz,text="Tetris"           ,bg='red', fg= 'azure',command=lambda:games("Tetris.gb")                                        ,width=15).place(x=800,y=400,anchor="center")
Button(raiz,text="Tomb Raider"      ,bg='red', fg= 'azure',command=lambda:games("TombRaiderCurseoftheSword.gbc")                    ,width=15).place(x=600,y=450,anchor="center")

# Boton que permitira apagar la consola
#-------------------------------------------------------------------------------------------------------
Button(raiz,text="Apagar",bg='azure', fg='black',command=salir,width=15).place(x=600,y=500,anchor="center")
#--------------------------------------------------------------------------------------------------------

raiz.mainloop()

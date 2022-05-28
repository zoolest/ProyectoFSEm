#!/bin/bash

#Creacion de carpeta RetroGaming con super usuario, 
#instalacion de mednafen y movimiento de carpeta roms


sudo mkdir /etc/RetroGaming
sudo apt-get install mednafen -y
sudo cp -r ./roms/ /etc/RetroGaming

#Colocación de audio, instalacion de  bibliotecas,
#movimiento de imagenes de fondo y splash,
#ajuste de wallpaper
sudo cp ./Audio.mp3 /etc/RetroGaming/Audio.mp3
sudo apt install sox -y
sudo apt install libsox-fmt-mp3 -y
sudo cp ./grub /etc/default/grub
sudo update-grub
sudo cp ./splash.png /usr/share/plymouth/themes/pix/splash.png
sudo cp ./Fondo.png /etc/RetroGaming/Fondo.png
pcmanfm --set-wallpaper /etc/RetroGaming/Fondo.png
sudo xrandr -s 1152x864

#Movimiento de imagen background.png,RetroGaming.py y display.desktop 
sudo cp ./Background.png /etc/RetroGaming/Background.png
sudo cp ./RetroGaming.py /etc/RetroGaming
sudo cp ./display.desktop /etc/xdg/autostart/display.desktop

#Reinicio de maquina
sudo reboot
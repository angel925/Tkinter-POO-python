#Modulo Botenes.py
#crea los botones Button

#inportando el modulo tkinter para reconocimiento de los abritubos propios, EJ: Button,bg...
from tkinter import *

class Botones:

    def __init__(self,texto,largo,alto,fondo,lugarx,lugary,comando):
        self.texto = texto
        self.largo = largo
        self.alto = alto
        self.fondo = fondo
        self.comando = comando
        self.lugarx = lugarx
        self.lugary = lugary
    
#metodo para crear los botones.  
    def Botons(self):
        self.ventana = Button(text = (self.texto), width =( self.largo), height = (self.alto), 
        command = (self.comando), bg= (self.fondo)).place(x = (self.lugarx), y =( self.lugary))
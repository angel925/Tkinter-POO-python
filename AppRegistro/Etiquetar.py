#Modulo Etiquetar.py
#crea las etiquetas Label

#inportando el modulo tkinter para reconocimiento de los abritubos propios, EJ: Label,bg...
from tkinter import *


#clase Etiqueta
class Etiqueta:

    def __init__(self,texto,fondo,lugarx,lugary,fuente =("Cambria", 12)): 
        self.texto = texto
        self.fuente = fuente
        self.fondo = fondo
        self.lugarx = lugarx
        self.lugary = lugary
        # self.labels()

#metodo para hacer Label   
    def labels(self):    
       self.ventana = Label(text=(self.texto),font = (self.fuente),bg= (self.fondo)).place( x = (self.lugarx), y = (self.lugary))
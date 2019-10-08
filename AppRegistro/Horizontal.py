#Modulo Horizontal.py
#Traza la lineas depediendo de la ubicacion y los colores, 
#Creacionn de Labal para diseño


#inportando el modulo tkinter para reconocimiento de los abritubos propios, EJ: Entry,Label,geometry,title...
from tkinter import *

#creando una nueva clase
class Linea:

    
    def __init__(self,texto,fondo,alto,ancho,fuente =("Cambria", 14),fondodeletra = "black"): 
        self.texto = texto
        self.fondo = fondo
        self.alto = alto
        self.ancho = ancho
        self.fuente = fuente
        self.fondodeletra = fondodeletra
       
        
    def Horizons(self):    
       self.ventana = Label(text=(self.texto),font = (self.fuente),bg= (self.fondo),fg =(self.fondodeletra), width = (self.ancho), height = self.alto)
       self.ventana.pack()
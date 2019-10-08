#Modulo Ventana.py
#levantando la ventana 

#inportando el modulo tkinter para reconocimiento de los abritubos propios, EJ: geometry,title...
from tkinter import *

#clase ventana
class Ventana: 

    def __init__(self,dimensiones,fondo,titulo):
        self.dimensiones = dimensiones  
        self.fondo = fondo  
        self.titulo = titulo 
       
        
# metodo de la ventana
    def newventana(self): 
        self.ventana = Tk()
        self.ventana.geometry(self.dimensiones)
        self.ventana.config(bg=(self.fondo))
        self.ventana.title(self.titulo)

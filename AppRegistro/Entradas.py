#Modulo Entradas.py
#crea las entradas Entry

#inportando el modulo tkinter para reconocimiento de los abritubos propios, EJ: Entry, width...
from tkinter import *
#clase Entradas

class Entradas:

    def __init__(self,variable,largo,lugarx,lugary):
        self.variable = variable
        self.largo = largo
        self.lugarx = lugarx
        self.lugary = lugary

#metodo entrys        
    def entrys(self,):
        self.ventana = Entry(textvariable=(self.variable), width = (self.largo)).place(x = self.lugarx, y = self.lugary)
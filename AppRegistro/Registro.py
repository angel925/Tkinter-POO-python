#Modulo Registro.py
#Captura los parametros por teclado


#inportando el modulo tkinter para reconocimiento de los abritubos propios, EJ: StringVar()
from tkinter import *

#clase registro
class Registro:

    def __init__(self,Nombres,Documento,Fecha,Telefono,Direccion,Codigo,Descripcion):
        
        self.Nombres = StringVar()
        self.Documento = StringVar()
        self.Fecha =StringVar()
        self.Telefono = StringVar()
        self.Direccion = StringVar()
        self.Codigo = StringVar()
        self.Descripcion = StringVar()

        self.Nombres.get() 
        self.Documento.get()
        self.Fecha.get()
        self.Telefono.get()
        self.Direccion.get()
        self.Codigo.get()
        self.Descripcion.get()

        


#metodo para  los datos 
    def consultar(self):
        primerdato = self.Nombres.get() 
        segundodato = self.Documento.get()
        tercerdato = self.Fecha.get()
        cuartodato = self.Telefono.get()
        quintodato = self.Direccion.get()
        sextodato =  self.Codigo.get()
        septimodato = self.Descripcion.get()
        
       

        diccionario = {}
        diccionario["nombre"] = primerdato
        diccionario ["documento"]= segundodato
        diccionario  ["fecha"]= tercerdato
        diccionario ["direccion"]= cuartodato
        diccionario ["telefono"]= quintodato
        diccionario ["codigo de equipo"]= sextodato
        diccionario ["Estado de entrega"]= septimodato
    
        contener = []
        contener.append(diccionario)

#recorre el diccionario

    def Verificando(self,diccionario):
        for key in diccionario:
            print(diccionario[key])
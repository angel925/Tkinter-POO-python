#Programa:main.py | 
#Proposito:Registro, Laptos para inventariar sus entradas y descripsisones.
#Autor:Johan Smith | Johan Oyola Rivera
#5/10/2019

# Importando los modulos y sus clases 

from tkinter import *
from Ventana import Ventana
from Etiquetar import Etiqueta
from Entradas import Entradas
from Botones import Botones
from Horizontal import Linea
from Registro import Registro
from Registro import Registro as consultar

#Instancias

# Levantando la ventana tkinter con sus atributos
mywindow = Ventana("570x550","#000000","Campo Técnologico J J")
uno = mywindow.newventana()

encabezado = Linea("Registro del Equipo/PC,Escritorio","#00CD63","2","500",("Cambria",14),"Black")
en = encabezado.Horizons()

#levantando las etiquetas, Label

myetiqueta = Etiqueta("Nombres y Apellidos","white",22,70)
etiq = myetiqueta.labels()

myetiqueta2 = Etiqueta("Documento","white",22,130)
etiq2 = myetiqueta2.labels()

myetiqueta3 = Etiqueta("Fecha DD/MM/AA","white",22,190)
etiq3 = myetiqueta3.labels()

myetiqueta4 = Etiqueta("Télefono","white",300,70)
etiq4 = myetiqueta4.labels()

myetiqueta5 = Etiqueta("Dirección","white",300,130)
etiq5 = myetiqueta5.labels()

myetiqueta6 = Etiqueta("Codigo S/N","white",300,190)
etiq6 = myetiqueta6.labels()

myetiqueta7 = Etiqueta("Descripción del estado en que se recibe el equipo","white",22,270)
etiq7 = myetiqueta7.labels()

#definiendo los campos, Entry
#Capturando los datos ingresador por teclado con StringVar()

Nombres = StringVar()

entrada1 = Entradas(Nombres,"40",22,100)
en1 = entrada1.entrys()

Documento = StringVar()

entrada2 = Entradas(Documento,"40",22,160)
en2 = entrada2.entrys()

Fecha = StringVar()

entrada3 = Entradas(Fecha,"40",22,220)
en3 = entrada3.entrys()

Telefono = StringVar()

entrada4 = Entradas(Telefono,"40",300,220)
en4 = entrada4.entrys()

Direccion = StringVar()

entrada5 = Entradas(Direccion,"40",300,160)
en5 = entrada5.entrys()

Codigo = StringVar()

entrada6 = Entradas(Codigo,"40",300,100)
en6 = entrada6.entrys()

Descripcion = StringVar()

entrada7 = Entradas(Descripcion,"87",22,300)
en7 = entrada7.entrys()

#Recibiendo lo como parametros los datos ingresados por teclado

ver = Registro(Nombres,Documento,Fecha,Telefono,Direccion,Codigo,Descripcion)
ver1 = ver.consultar()
ver.consultar()

#Boton registrar que envia los datos a consultar()

boton1 = Botones("Registro Pc","30","2","#00CD63",327,440,consultar)
bn = boton1.Botons()

#Ciclo tkinter

mainloop()
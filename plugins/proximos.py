#.py para proximos dias
import math
from datetime import date
from datetime import datetime
from datetime import timedelta
def diaP():
    meses =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
	#obteniendo el promedio de los dias que puede durar el ciclo
    f = open("Duracion.txt",'r')
	#leyendo lineas
    for linea in f:
        duracion = str(linea)
    duracioS = duracion.split(',')
    suma = 0
    #sumando lo que contiene el arreglo duracios
    for i in range(len(duracioS)-1):
    	num = int(duracioS[i])
    	suma = suma + num
	#duracion del periodo redondeado.
    peri = round(suma/(len(duracioS)-1))
    f.close()
    ##---------Obteniendo fecha para sumarla--------
    f = open ("Fechas.txt",'r')
    for linea in f:
        fecha = str(linea)
    fechaS = fecha.split(',')
    num = len(fechaS)
    ultF = fechaS[-2]#es -2 porque uno es del espacio y otro de los lugares que manejan las listas
    fsep = ultF.split('-')
    f.close()
    dia = int(fsep[2])
    mes = int(fsep[1])
    anio = int(fsep[0])
    #creando una fecha con el string
    new_date1 = datetime(anio,mes,dia)
    #Sumando a la ultima fecha registrada la duración del periodo
    proximo = new_date1 + timedelta(days = peri)
    #obteniendo el mes de una forma mas amigable
    mesb = meses[int(proximo.month)-1]
    diaB = proximo.day
    today1= datetime.now()
    ##restamos hoy a la fecha que marca para dar diferentes mensajes
    DDC = (new_date1-today1).days
    if (DDC>3):
        return'say "Tu Proximo periodo llega aproximadamente el {} del {}"'.format(diaB,mesb)
    if (DDC==1):
    	return 'say "Es posible que tu periodo llegue mañana. Debes estar preparada."'
    if(DDC<0):
    	return 'say "Tu periodo está un poco retrasado, pero es normal, recuerda que dependiendo de tus rutina puede variar la duracion del ciclo"'




    
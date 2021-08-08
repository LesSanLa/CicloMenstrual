from datetime import date
from datetime import datetime
from datetime import timedelta

def registroF(*args):
    numD = str(args[0]) #obtenemos dia o fecha
    fechaD=numD.split("/")
    diaF = int(fechaD[0])
    mes = int(fechaD[1])
    anio = int(fechaD[2])
        #fecha para escritura en el archivo
    fechaB = fechaD[2]+"-"+fechaD[1]+"-"+fechaD[0]
        #creando una fecha con el string
    #new_date = datetime(anio,mes,diaF)
        ##--------Escribiendo las fecha en TXT----------------
    f = open ('Fechas.txt','a')
    f.write(str(fechaB))
    f.write(",")#reescribe todo el archivo
    f.close()
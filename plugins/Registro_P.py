from datetime import date
from datetime import datetime
from datetime import timedelta
import json
def guardarDia(): #menstruaste el dia de hoy
    meses =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    # para dar la fecha de forma mas amigable
    today = date.today() #la fecha es: año-mes-dia todo con numeros
	#abrimos el fichero
    f = open("/home/mayte/Desktop/ServicioSocial/CicloMenstrual/conversations/cicloMenstrual/is.json","r")
	#leemos los datos del fichero
    datos = f.read()
	#decodificación de json
    datosJson = json.loads(datos)
    dias = int(datosJson['duraP'])
    duracion=today + timedelta(days=dias)
    #sumamos los días que el json tiene guardado
    diaD = duracion.day
    mes = meses[int(duracion.month)-1]

    ##--------Escribiendo las fechas de inicio del periodo en txt----------------
    f = open ('Fechas.txt','a')
    f.write(str(today))
    f.write(",")#reescribe todo el archivo
    f.close()
    return 'say "Tu periodo durará (aproximadamente) hasta el {} de {}"'.format(diaD,mes)
##-------------Cuando no se inicia el periodo en el día que se abre el chatbot----------------

def diaDif(*args): 
    meses =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    numD = str(args[0]) #obtenemos dia o fecha
    lon = len(numD)
    f = open("/home/mayte/Desktop/ServicioSocial/CicloMenstrual/conversations/cicloMenstrual/is.json","r")
    #leemos los datos del fichero
    datos = f.read()
    #decodificación de json
    datosJson = json.loads(datos)
    dias = int(datosJson['duraP'])
    #today = date.today() #dia de hoy 
    if(lon<=2):
        today = date.today()
        numD=int(numD)
        #le restamos al dia de hoy los dias que se indica
        duracion=today - timedelta(days=numD)
        #escribimos la fecha en el txt
        f = open ('Fechas.txt','a')
        f.write(str(duracion))
        f.write(",")
        f.close()
        diaD = duracion.day
        mes = meses[int(duracion.month)-1]
        return 'say "Tu periodo comenzó el {} del {}"'.format(diaD,mes)
    if(lon>2):
        fechaD=numD.split("/")
        diaF = int(fechaD[0])
        mes = int(fechaD[1])
        anio = int(fechaD[2])
        #fecha para escritura en el archivo
        fechaB = fechaD[2]+"-"+fechaD[1]+"-"+fechaD[0]
        #creando una fecha con el string
        new_date1 = datetime(anio,mes,diaF)
        ##--------Escribiendo las fechas de inicio del periodo en txt----------------
        f = open ('Fechas.txt','a')
        f.write(str(fechaB))
        f.write(",")#reescribe todo el archivo
        f.close()
        #--------------Escribiendo la duración del ciclo-----------------------------
        day = datetime.now()
        dif= (day-new_date1).days
        dura=dias-dif
        if(dura<0):
            return 'say "Tu periodo pudo haber finalizado o seguir un día mas"'
        if(dura>0):
            duracion=today + timedelta(days=dura)
            #sumamos los días que el json tiene guardado
            diaD = duracion.day
            mes = meses[int(duracion.month)-1]
            return 'say "Tu periodo durará (aproximadamente) hasta el {} de {}"'.format(diaD,mes)








	


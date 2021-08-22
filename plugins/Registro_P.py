from datetime import date
from datetime import datetime
from datetime import timedelta
import json
def guardarDia(): #menstruaste el dia de hoy
    meses =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    # para dar la fecha de forma mas amigable
    today = date.today() #la fecha es: año-mes-dia todo con numeros
	#abrimos el fichero
    f = open("conversations/cicloMenstrual/is.json","r")
    #f = open("/home/ximena/ServicioSocial/ChatBotLesly/CicloMenstrual/is.json","r")
	#leemos los datos del fichero
    datos = f.read()
	#decodificación de json
    datosJson = json.loads(datos)
    dias = int(datosJson['duraP'])
    duracion=today + timedelta(days=dias)
    #sumamos los días que el json tiene guardado
    diaD = duracion.day
    mesb = meses[int(duracion.month)-1]

    ##--------Escribiendo las fechas de inicio del periodo en txt----------------
    f = open ('Fechas.txt','a')
    f.write(str(today))
    f.write(",")#reescribe todo el archivo
    f.close()
    ##------- Escribiendo la duracion---------------------
    f = open("Fechas.txt",'r')
    for linea in f:
        fecha = str(linea)
    #print(fecha)
    fechaS = fecha.split(',')
    num = len(fechaS)
    #print(num)
    ultF = fechaS[-3]#es -2 porque uno es del espacio y otro de los lugares que manejan las listas
    #print(ultF)
    fsep = ultF.split('-')
    #for i in range(len(fsep)):
    #       print(fsep[i])
    f.close()
    dia = int(fsep[2])
    mes = int(fsep[1])
    anio = int(fsep[0])
    #creando una fecha con el string
    new_date1 = datetime(anio,mes,dia)
    #print(new_date1)
    today1= datetime.now()
    ciclo = (today1-new_date1).days
    f = open("Duracion.txt",'a')
    f.write(str(ciclo))
    f.write(",")
    #print("duracion del ciclo {}".format(ciclo))
    f.close()
    return 'say "Tu periodo durará (aproximadamente) hasta el {} de {}"'.format(diaD,mesb)
##-------------Cuando no se inicia el periodo en el día que se abre el chatbot----------------

def diaDif(*args): 
    meses =["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    numD = str(args[0]) #obtenemos dia o fecha
    lon = len(numD)
    f = open("conversations/cicloMenstrual/is.json","r")
    #f = open("/home/ximena/ServicioSocial/ChatBotLesly/CicloMenstrual/is.json","r")
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
        mesb = meses[int(duracion.month)-1]
        ##-----Guardando los dias de diferencia------------
        f = open("Fechas.txt",'r')
        for linea in f:
            fecha = str(linea)
        fechaS = fecha.split(',')
        num = len(fechaS)
        ultF = fechaS[-3]
        #es -3 porque uno es del espacio y otro de los lugares que manejan las listas y el ultimo la fecha que guarda
        fsep = ultF.split('-')
        f.close()
        dia = int(fsep[2])
        mes = int(fsep[1])
        anio = int(fsep[0])
        #creando una fecha con el string
        new_date1 = datetime(anio,mes,dia)
        today1 = datetime.now()
        numD=int(numD)
        #le restamos al dia de hoy los dias que se indica
        duracion1=today1 - timedelta(days=numD)
        #calculando los dias de diferencia
        ciclo = (duracion1-new_date1).days
        f = open("Duracion.txt",'a')
        f.write(str(ciclo))
        f.write(",")
        f.close()
        return 'say "Tu periodo comenzó el {} del {}"'.format(diaD,mesb)
    if(lon>2):
        fechaD=numD.split("/")
        diaF = int(fechaD[0])
        mes = int(fechaD[1])
        anio = int(fechaD[2])
        #fecha para escritura en el archivo
        fechaB = fechaD[2]+"-"+fechaD[1]+"-"+fechaD[0]
        #creando una fecha con el string
        new_date = datetime(anio,mes,diaF)
        ##--------Escribiendo las fechas de inicio del periodo en txt----------------
        f = open ('Fechas.txt','a')
        f.write(str(fechaB))
        f.write(",")#reescribe todo el archivo
        f.close()
        #--------------Escribiendo la duración del ciclo-----------------------------
        f = open("Fechas.txt",'r')
        for linea in f:
            fecha = str(linea)
        fechaS = fecha.split(',')
        num = len(fechaS)
        ultF = fechaS[-3]
        #es -3 porque uno es del espacio y otro de los lugares que manejan las listas y el ultimo la fecha que guarda
        fsep = ultF.split('-')
        f.close()
        dia2 = int(fsep[2])
        mes2 = int(fsep[1])
        anio2 = int(fsep[0])
        #creando una fecha con el string
        new_date2 = datetime(anio2,mes2,dia2)
        #escribiendo la duracion en el txt que corresponde. 
        ciclo = (new_date-new_date2).days
        f = open("Duracion.txt",'a')
        f.write(str(ciclo))
        f.write(",")
        f.close()
        day = datetime.now()
        dif= (day-new_date).days
        dura=dias-dif
        if(dura<0):
            return 'say "Tu periodo pudo haber finalizado o seguir un día mas"'
        if(dura>0):
            duracion=today + timedelta(days=dura)
            #sumamos los días que el json tiene guardado
            diaD = duracion.day
            mes = meses[int(duracion.month)-1]
            return 'say "Tu periodo durará (aproximadamente) hasta el {} de {}"'.format(diaD,mes)








	


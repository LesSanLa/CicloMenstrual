from datetime import date
from datetime import datetime
from datetime import timedelta
import json
def guardarDia():
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
    #obtenemos el mes en palabra
    return 'say "Tu periodo durará hasta el {} de {}"'.format(diaD,mes)

    #Guardando la fecha en un archivo txt




	


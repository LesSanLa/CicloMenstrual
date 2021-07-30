#Pruebas de codigo en python
from datetime import date
from datetime import datetime
from datetime import timedelta
dia = input("ingresa el dia o numero:")
lon = len(dia)
if(lon<=2):
	dia=int(dia)
	today = date.today()
	duracion=today - timedelta(days=dia)
	duracion=str(duracion)	
	print("Tu periodo inicio el: {}".format(duracion))
if(lon>2):
	fechaD=dia.split("/")
	#for i in range(len(fechaD)):
		#print(fechaD[i])
	diaF = int(fechaD[0])
	mes = int(fechaD[1])
	anio = int(fechaD[2])
	fechaB = fechaD[2]+"-"+fechaD[1]+"-"+fechaD[2]
	print(fechaB)
	#creando una fecha con el string
	new_date = datetime(anio,mes,diaF)
	print(new_date)
	#obteniendo los dias diferentes 
	day = datetime.now()
	dif= (day-new_date).days
	print("dias {}".format(dif))


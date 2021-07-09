#código para obtener el metodo habitual

import json

def metodoHabitual():

	#abrimos el fichero
	f = open("/home/mayte/Desktop/ServicioSocial/CicloMenstrual/conversations/cicloMenstrual/is.json","r")
	#leemos los datos del fichero
	datos = f.read()
	#decodificación de json
	datosJson = json.loads(datos)

	#print (datosJson['metHab'])
	metodo = str(datosJson['metHab'])
	#pasamos todo a minusculas para poder comparar
	metodo = metodo.lower()
	if(metodo == 'copa menstrual'):
		return 'solve copaM'
	if (metodo == 'toalla desechable'):
		return 'solve toallaD'
	if (metodo == 'toalla ecologica'):
		return 'solve tEcolo'
	if (metodo == 'tampon'):
		return 'solve tampon'





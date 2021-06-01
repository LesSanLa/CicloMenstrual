#codigo en python para avisar de una alarma.
#copa menstrual
#falta implementar la alarma.
def c_Abundante(*args):
    horas_us = int(args[0])
    horas_camb = 6 - horas_us 
    if (horas_camb <= 0):
    	return 'say "Estás en el límite, deberas cambiarla lo antes posible para evirar derrames"'
    if (horas_camb == 2):
    	return 'say "Si es de las primeras veces que la usas, podrias cambiarla"'
    if (horas_camb >0):
        return 'say "En aproximadamente {} horas, deberás cambiarla"'.format(horas_camb)

def c_Medio(*args):
    horas_us = int(args[0])
    horas_camb1 = 8 - horas_us
    horas_cam2 = 12 - horas_us
    if (horas_cam2 <=0):
    	return 'say "Debes de cambiarla lo antes posible, no es recomendable estar mas de 12 horas"'
    if (horas_cam2 > 0 and horas_camb1 <=0):
    	return 'say "Podrías cambiarla para evitar derrames o esperar un poco más"'
    if (horas_camb1>0):
    	return 'say "Puede cambiarlo en {} hrs o {} hrs (sin pasar las 12 hrs)"'.format(horas_cam2,horas_camb1)

def c_Perdidas (*args):
    horas_us = int(args[0])
    horas_camb = 12 - horas_us
    if (horas_camb <=0):
    	return 'say "Debes cambiarla lo antes posible, para evitar infecciones"'
    if (horas_camb > 0):
    	return 'say "Deberás cambiarla en {} hrs"'.format(horas_camb)

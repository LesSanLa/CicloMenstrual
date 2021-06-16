#codigo en python para avisar de una alarma.
#copa menstrual
#falta implementar la alarma.
def c_Abundante(*args):
    horas_us = int(args[0])
    horas_camb = 6 - horas_us 
    if (horas_camb <= 0):
    	return 'say "Estás en el límite, deberas cambiarla lo antes posible para evirar derrames"'
    if (horas_camb == 2):
    	return 'say "podrias cambiarla ahora para sentirte más segura"'
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
#-----------------------------------------------------------------------------------------------------------------
#horas para la toalla ecologica
def E_Abundante(*args):
    horas_us = int(args[0])
    horas_camb = 4 - horas_us
    if (horas_camb <= 0):
        return 'say "Estás en el límite, deberas cambiarla lo antes posible para evirar derrames"'
    if (horas_camb == 2):
        return 'say "Recuerda checar tu toalla si te sientes muy humeda para evitar accidentes"'
    if (horas_camb >0):
        return 'say "En aproximadamente {} horas, deberás cambiarla"'.format(horas_camb)

def E_Moderado(*args):
    horas_us = int(args[0])
    horas_camb1 = 2 - horas_us
    horas_cam2 = 4 - horas_us
    if (horas_cam2 <=0):
        return 'say "Debes de cambiarla lo antes posible, no es recomendable estar más de 4 horas"'
    if (horas_cam2 > 0 and horas_camb1 <=0):
        return 'say "Podrías cambiarla para evitar derrames."'
    if (horas_camb1>0):
        return 'say "Puede cambiarlo en {} hrs o {} hrs (sin pasar las 4 hrs)"'.format(horas_cam2,horas_camb1)

def E_Perdidas (*args):
    horas_us = int(args[0])
    horas_camb = 4 - horas_us
    if (horas_camb <=0):
        return 'say "Debes cambiarla lo antes posible, para evitar infecciones"'
    if (horas_camb > 0):
        return 'say "Deberás cambiarla en {} hrs"'.format(horas_camb)
#---------------------------------------------------------------------------------------------------------------------------
#Toalla desechable.
def D_Abundante(*args):
    horas_us = int(args[0])
    horas_camb = 4 - horas_us
    if (horas_camb <= 0):
        return 'say "Estás en el límite, deberas cambiarla lo antes posible para evirar derrames"'
    if (horas_camb == 2):
        return 'say "Recuerda checar tu toalla si te sientes muy humeda para evitar accidentes"'
    if (horas_camb >0):
        return 'say "En aproximadamente {} horas, deberás cambiarla"'.format(horas_camb)

def D_Moderado(*args):
    horas_us = int(args[0])
    horas_camb1 = 2 - horas_us
    horas_cam2 = 4 - horas_us
    if (horas_cam2 <=0):
        return 'say "Debes de cambiarla lo antes posible, no es recomendable estar más de 4 horas"'
    if (horas_cam2 > 0 and horas_camb1 <=0):
        return 'say "Podrías cambiarla para evitar derrames."'
    if (horas_camb1>0):
        return 'say "Puede cambiarlo en {} hrs o {} hrs (sin pasar las 4 hrs)"'.format(horas_cam2,horas_camb1)

def D_Perdidas (*args):
    horas_us = int(args[0])
    horas_camb = 4 - horas_us
    if (horas_camb <=0):
        return 'say "Debes cambiarla lo antes posible, para evitar infecciones"'
    if (horas_camb > 0):
        return 'say "Deberás cambiarla en {} hrs"'.format(horas_camb)

#-------------------------------------------------------------------------------------------------------------------------
#Tampon
def tam_Abundante(*args):
    horas_us = int(args[0])
    horas_camb = 4 - horas_us 
    if (horas_camb <= 0): 
        return 'say "Estás en el límite, deberas cambiarlo lo antes posible para evirar derrames"'
    if (horas_camb == 2): 
        return 'say "¿Cómo te sientes?. Podrías cambiar tu tampon ahora o esperar un poco más."'
    if (horas_camb >0):
        return 'say "En aproximadamente {} horas, deberás cambiarla"'.format(horas_camb)

def tam_Moderado(*args):
    horas_us = int(args[0])
    horas_camb1 = 6 - horas_us
    horas_cam2 = 8 - horas_us
    if (horas_cam2 <=0):
        return 'say "Debes de cambiarlo lo antes posible, no es recomendable traer un tampon por más de 8 horas"'
    if (horas_cam2 > 0 and horas_camb1 <=0):
        return 'say "Podrías cambiarlo para evitar derrames o esperar un poco más"'
    if (horas_camb1>0):
        return 'say "Puede cambiarlo en {} hrs o {} hrs (sin pasar las 8 hrs)"'.format(horas_cam2,horas_camb1)

def tam_Perdidas (*args):
    horas_us = int(args[0])
    horas_camb = 8 - horas_us
    if (horas_camb <=0):
        return 'say "Debes cambiarla lo antes posible, para evitar infecciones"'
    if (horas_camb > 0): 
        return 'say "Deberás cambiarla en {} hrs"'.format(horas_camb)



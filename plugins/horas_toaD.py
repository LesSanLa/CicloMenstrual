#Codigo en python para avisar de una alarma.
#toalla desechable
#falta implementar la alarma.
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


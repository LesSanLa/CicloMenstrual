#código para horas de la toalla ecologica y deshechable.

def toallaE(*args):
    horas_us = int(args[0])
    horas_camb = 4 - horas_us 
    if (horas_camb <= 0):
    	return 'say "Cambia tu toalla lo antes posible, al ser ecologica no hay tanto riesgo de infección"'
    	
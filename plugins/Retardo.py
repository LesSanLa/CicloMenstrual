import time
def retardob():#retardo de dos segundos
    later = time.time() + 2
    later1 =  time.ctime(later)
    tiempo = time.ctime()
    while (tiempo < later1):
        tiempo = time.ctime()

def retardom():#retardo de 1 segundo
    later = time.time() + 1
    later1 =  time.ctime(later)
    tiempo = time.ctime()
    while (tiempo < later1):
        tiempo = time.ctime()

def retardoc():#retardo de cuatro segundos
    later = time.time() + 4
    later1 =  time.ctime(later)
    tiempo = time.ctime()
    while (tiempo < later1):
        tiempo = time.ctime()

def retardoO():#retardo de 8 segundos
    later = time.time() + 8
    later1 =  time.ctime(later)
    tiempo = time.ctime()
    while (tiempo < later1):
        tiempo = time.ctime()
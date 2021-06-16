import time

print("ingresa un tiempo:")
var = int(input())
#si el tiempo es en horas(para la alarma):
#var=var*3600
later = time.time() + var
later1 =  time.ctime(later)
tiempo = time.ctime()
while (tiempo < later1):
   tiempo = time.ctime()
#print ("hora:",later1)
print("ALARMA")
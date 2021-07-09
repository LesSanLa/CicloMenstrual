#código para obtener el metodo habitual

# aun no hace nada :C
import json

datos = {}
datos['datos'] = []

with open('is.json') as file:
    datos = json.load(file)

for client in datos['datos']:
    print('nombre:', client['name'])
    print('metodo habitual:', client['metHab'])
    print('Duración del periodo: ', client['duraP'])
    print(" ")
        
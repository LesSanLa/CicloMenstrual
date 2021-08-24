
from fastapi import FastAPI
from database import database as connection
app = FastAPI(title='BotAmalia',
					description='Chatbot de seguimiento ciclo menstrual',
					version='1.0 ')

@app.on_event('startup')
def starup():
	if connection.is_closed():
		connection.connect()

@app.on_event('shutdown')
def shutdown():
	if not connection.is_closed():
		connection.close()


@app.get('/')
async def index():
	return 'Soy Amalia, tu asistente para el seguimiento de tu ciclo menstrual, un gusto conocerte.'

@app.get('/Metodos')
async def metodos():
	return 'Tengo información sobre los siguientes metodos: copa ecologica, toalla ecologica, toalla desechable y tampon.'

@app.get('/Seguimiento')
async def seguimiento():
	return 'Puedo guardar información de tu periodo como comienzo, días fertiles y próximo inicio de tu menstruación. Además darte recordatorios.'

@app.get('/Malestares')
async def malestares():
	return 'Sección malestares.'

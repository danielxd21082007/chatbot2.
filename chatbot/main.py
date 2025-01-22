# This example requires the 'message_content' intent.

import discord
from bot_logic import *
from main_bot import *
from main_client import *

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('$bie'):
        await message.channel.send('Bie!')



# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)


# Una vez que el bot esté listo, ¡imprimirá su nombre!
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


# Cuando el bot reciba un mensaje, ¡enviará mensajes en el mismo canal!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('¡Hola! Soy un bot')
    elif message.content.startswith('$emoji'):
        await message.channel.send(gen_emoji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("No puedo procesar este comando, ¡lo siento!")

client.run('TOKEN')

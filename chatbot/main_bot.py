import discord
import os
import random
import requests

from discord.ext import commands
from bot_logic import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, long = 15):
    await ctx.send(gen_pass(long))

@bot.command()
async def meme(ctx):
    images = os.listdir("images") 
    image_name = random.choice(images)

    with open(f'images/{image_name}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command('pokemon')
def get_random_pokemon_data():
    # Elegimos un ID aleatorio para un Pokémon (1-1010 para todas las generaciones)
    pokemon_id = random.randint(1, 1010)
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "image": data["sprites"]["front_default"],
            "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}
        }
    else:
        return None

bot.run('TOKEN')

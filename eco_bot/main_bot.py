import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command('contaminacion')
async def contaminacion(ctx):
    await ctx.send('una de las principales consecuencias de la contaminación esque aquel regalo tan valioso (la naturaleza) que nos dió la vida sea destruido, solo por nuestra pereza, nuestra avaricia y gula.')
    with open (f'images/consecuencia.jpg', 'rb') as f:
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run('MTMxOTQ1MjU4MzgyMzI4MjI1Ng.G7IiL_.ALNPrVej9SktupH2zGNj_tLlAe9cR6F_Lv0QQ0')
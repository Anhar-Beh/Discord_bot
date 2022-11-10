import discord
import os
from discord.ext import commands

#ID of the bot, definition of the bot
TOKEN = 'OTEwMTkyMjQwMjkzNDYyMDU2.YZPQlA.On9Z6KNzOZpdqErjsrLmVyLf7IQ'

#permissions being set to all
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='//', intents=intents)

#Loading all the Cogs
for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])

#Printing stuff to know whether the bot is connected and is online
@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to the following guilds:')
    for guild in bot.guilds:
        print(f'- {guild.name}')

#runs the bot
bot.run(TOKEN)
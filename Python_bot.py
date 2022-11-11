import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='//', intents=intents)

#Loading all the Cogs
for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        bot.load_extension("cogs." + f[:-3])


command = ['- //commands', '- //rsp', '- //coinflip', '- //cleanup', '- //8ball', '- //connect4', '- //uttt']
##################################################################### Events ###############################################################################################################
@bot.event
async def on_ready():
    print(f'{bot.user.name} is connected to the following guilds:')
    for guild in bot.guilds:
        print(f'- {guild.name}')


    
#############################################################################################################################################################################################

######################################################## Commands ##########################################################################################################################

#displays all the robo bot commands
@bot.command(name = 'commands', help = 'displays all the commands Python Bot serves')
async def commands(ctx):
    user = await bot.fetch_user(910192240293462056)
    pfp = user.avatar_url
    embed = discord.Embed(
            title = 'Python Bot Commands',
            description = ('\n'.join(command)),
            colour = discord.Colour.dark_red()
            )
    embed.set_thumbnail(url = pfp)
    embed.set_footer(text = 'Please refer to the \"//help\" command for further information')
    await ctx.send(embed=embed)
    print(bot.commands)


############################################################################################################################################################################################
bot.run(TOKEN)

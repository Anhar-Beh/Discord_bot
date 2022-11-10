from discord.ext import commands

class greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = await member.create_dm()
        server = member.guild.name
        await channel.send(f"Welcome to {server}!\nI am Python the bot, you can check all my commands by typing \"//commands\"")


        
        
def setup(bot):
    bot.add_cog(greetings(bot))

    
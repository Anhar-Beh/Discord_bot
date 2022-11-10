from discord.ext import commands
import re


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        #collecting and comparing against the bad words in the file specified
        with open("cogs\\modules\\bad_words", "r") as f:
            if message.author != self.bot.user:#making sure it doesn't detect it from the bot
                data = f.readlines()
                for words in data:
                    word = words.strip('\n')
                    swear = re.compile(word)
                    check = swear.search(message.content.lower())
                    if check != None:
                        await message.delete()
                        await message.channel.send("Uh oh! " + message.author.name + " sent a message with a bad word\nHere is the message:\n||" + message.content + "||")

    @commands.command()
    async def ban(self, ctx):
        await ctx.send('Who do you think should be banned?')

        #Checks if the reply is not from the original caller of the program and if it is from the same channel
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            name = await self.bot.wait_for('message',timeout=20, check=check)
            await ctx.send('For what reason should they be banned?')

            #Checks if the reply is not from the original caller of the program and if it is from the same channel
            def check(msg):
                return msg.author == ctx.author and msg.channel == ctx.channel

            try:
                reason = await self.bot.wait_for('message',timeout=20, check=check)
                channel = await ctx.guild.owner.create_dm()
                server = ctx.guild.name
                await channel.send(ctx.author.name + " thinks " + name.content + " should be banned in " + server)
                await channel.send("Reasoning:\n" + reason.content)

            except:
                await ctx.send('too slow, try again')
        except:
            await ctx.send('too slow, try again')

        

def setup(bot):
    bot.add_cog(moderation(bot))

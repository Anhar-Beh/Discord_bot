from discord.ext import commands
import asyncio
import random



class features(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Coin flip simulator
    @commands.command(name = 'coinflip', help = 'simulate flipping a coin with complete unbiased random')
    async def coin_flip(self, ctx):
        await ctx.send('https://tenor.com/view/coin-toss-coin-toss-gif-5017733')
        await asyncio.sleep(1)
        await ctx.send(random.choice(['Heads', 'Tails']))

    #post 2 gifs to cover the screen
    @commands.command(name = 'cleanup', help = 'Will post three gifs to cover up whatever abomination was on the screen')
    async def clean_up(self, ctx):
        await ctx.send('https://tenor.com/view/get-this-shit-out-club-penguin-mop-just-let-me-get-rid-of-the-shit-post-above-gif-17264103')
        await ctx.send('https://tenor.com/view/get-this-shit-out-club-penguin-mop-just-let-me-get-rid-of-the-shit-post-above-gif-17264103')
        await ctx.send('https://tenor.com/view/pussy-rub-cleaning-window-window-clean-cat-clean-cute-gif-16940085')

    #8ball
    @commands.command(name = '8ball', help = 'A magic 8-ball that will answer any question')
    async def _8ball(self, ctx):
        _8ball_ans = []
        with open("cogs\modules\\8_ball", "r") as f:
            data = f.readlines()
            for lines in data:
                _8ball_ans.append(lines)
        await ctx.send('https://tenor.com/view/eight-ball-gif-10769378')
        await asyncio.sleep(3)
        await ctx.send(random.choice(_8ball_ans))

    

def setup(bot):
    bot.add_cog(features(bot))
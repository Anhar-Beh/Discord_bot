import discord
import asyncio
import os
import random
import re
from discord.ext import commands
import Games_Decider as GD
import Rock_Paper_Scissor as RPS
import Connect_4 as C4

TOKEN = 'ODE0MTM2Nzc1NDk2MzAyNjgz.YDZd9Q.SEYFfP3CSmNAeg6deX4dD11mOP8'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

gay = re.compile('gay')
rejus_bot = re.compile('|')
n = re.compile('nigga')
n2 = re.compile('nigger')

threat = ['I saw that', 'What you deleting bro', 'I know', 'What you doing boy?', 'Anhar may not know, but I know', 'I\'m always watching you', 'Very sus', 'hmmm interesting']
command = ['!commands','!gamedecider', '!rockpaperscissors', '!coinflip', '!cleanup', '!8ball', '!connect4', '!gaycount', '!ncount', '!c4leaderboard']
_8ball_ans = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Cannot predict now.', 'Concentrate and ask again.', 'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.'] 
##################################################################### Events ###############################################################################################################
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name='Abnormal title')
    print(
        f'{bot.user.name} is connected to the following guild:\n'
        f'{guild.name}'
    )

@bot.event
async def on_message(message):
    #ish ish ishhhhh
    if message.content.lower().startswith('ish'):
        await message.delete()
        await message.channel.send('https://tenor.com/view/mahathir-tunm-tun-ppbm-bersatu-harapan-gif-9852425')
    #terbaikkk
    if message.content.lower().startswith('terbaikkk'):
        await message.delete()
        await message.channel.send('https://tenor.com/view/tunm-mahathir-tun-bersatu-ppbm-gif-9852429')
    if gay.search(message.content.lower()) != None and message.content.lower() != '!gaycount':
        try:
            count = []
            with open('Gay_count.txt','r') as r:
                info = r.readlines()
                for row in info:
                    cleanUp = row.strip('\n').split(',')
                    count.append([cleanUp[0], cleanUp[1]])
            with open('Gay_count.txt','w') as w:
                found = False
                for row in count:
                    if row[0].lower() == message.author.nick.lower():
                        row[1] = str(int(row[1])+1)
                        found = True
                        w.write(row[0] + ',' + row[1] + '\n')
                if found == False:
                    w.write(message.author.nick + ',' + str(1) + '\n')
        except:
            print('In the dms')
    if n.search(message.content.lower()) != None and n2.search(message.content.lower()) != None and message.content.lower() != '!ncount':
        try:
            count = []
            with open('n_count.txt','r') as r:
                info = r.readlines()
                for row in info:
                    cleanUp = row.strip('\n').split(',')
                    count.append([cleanUp[0], cleanUp[1]])
            with open('n_count.txt','w') as w:
                found = False
                for row in count:
                    if row[0].lower() == message.author.nick.lower():
                        row[1] = str(int(row[1])+1)
                        found = True
                        w.write(row[0] + ',' + row[1] + '\n')
                if found == False:
                    w.write(message.author.nick + ',' + str(1) + '\n')
        except:
            print('In the dms')
                
## In case rejus betrays me ##################################################
##    if message.author.name == 'Emeraldsheep':
##        await message.channel.send('This clown is speaking lmao')
##
##    if message.author.name == 'Banthar':
##        def check(msg):
##            return msg.author.name == 'Rejus\' Bot'
##
##        try:
##            answer = await bot.wait_for('message',timeout = 10, check=check)
##            await answer.delete()
##        except:
##            print('false alarm')
##    if message.content == '|shrek':
##        def check(msg):
##            return msg.author.name == 'Rejus\' Bot'
##
##        try:
##            answer = await bot.wait_for('message',timeout = 10, check=check)
##            await answer.delete()
##        except:
##            print('false alarm')
##    if message.content == '!cleanup':
##        def check(msg):
##            return msg.author.name == 'Rejus\' Bot'
##
##        try:
##            answer = await bot.wait_for('message',timeout = 10, check=check)
##            await answer.delete()
##        except:
##            print('false alarm')
###############################################################################
        
    await bot.process_commands(message)
    
@bot.event
async def on_message_delete(message):
    if message.author.name != bot.user.name and message.content.lower() != 'terbaikkk' and message.content.lower() != 'ish' and rejus_bot.search(message.content.lower()) != True:
        await message.author.send(random.choice(threat))
        print(message.author.nick + ' deleted the message \"' + message.content + '\"')
        
    await bot.process_commands(message)

#############################################################################################################################################################################################

######################################################## Commands ##########################################################################################################################
#Game Decider
@bot.command(name = 'gamedecider', help = 'Draws a game from a lottery created by an algorithm designed to encourage playing games that hasn\'t been played in a while. Reply with yes or no')
async def game_decider(ctx):
    if ctx.guild.name == 'Abnormal title':
        #Retrieving data and creating the lottery
        data = GD.read_data()
        lottery = GD.lottery_creation(data)
        #Display percentages of each game
        percent = []
        for game in data:
            percent.append(game[0] + ': ' + str(game[1]) + '/' + str(len(lottery)))
        embed = discord.Embed(
            title = 'Games percentages',
            description = ('\n'.join(percent)),
            colour = discord.Colour.dark_red()
            )
        await ctx.send(embed=embed)
        await ctx.send('Do you want to roll?')

        #Checks if the reply is from the original caller of the program and if it is from the same channel
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        try:
            answer = await bot.wait_for('message',timeout=20, check=check)
            #If the user wanted to roll
            if answer.content.lower() == 'yes':
                chosen = random.choice(lottery)
                await ctx.send('It has been Decided, Don\'t cry.\n\n' + chosen)

                #If the user is not satisfied
                stop = False
                while stop == False:
                    await ctx.send('Do you want to reroll?')
                    try:
                        answer = await bot.wait_for('message', timeout=20, check=check)
                        if answer.content.lower() == 'yes':
                            chosen = random.choice(lottery)
                            await ctx.send('It has been Decided, Don\'t cry.\n' + chosen)
                        elif answer.content.lower() == 'no':
                            GD.save_data(chosen,data)
                            stop = True
                            await ctx.send('Save file updated')
                        else:
                            await ctx.channel.send('Invalid answer. Answer correctly you schmuck')
                    #Error message display if the user took too long to answer 
                    except:
                        await ctx.send('Time has ran out to answer')
                        
            #if the user did not wanted to roll
            elif answer.content.lower() == 'no':
                await ctx.send('Alrighty then')
            #restart percentages
            elif answer.content.lower() == 'restart percentages' and answer.author.nick == 'Anhar':
                os.remove('Data.txt')
                await ctx.send('Percentages have been refreshed')
            #Invalid inputs
            else:
                await ctx.send('invalid answer. Restart the program peasant')
        #Error message display if the user took too long to answer    
        except:
            await ctx.send('Time has ran out to answer')

#Rock Paper Scissors
@bot.command(name = 'rockpaperscissors', help = 'Classis game of rock paper scissors')
async def rsp(ctx):
    if ctx.guild.name == 'Abnormal title':
        await ctx.send('Whoever wants to play, say \"me\"')
        count = 0

        #Checks if the reply is not from the original caller of the program and if it is from the same channel
        def check(msg):
            return msg.author != ctx.author and msg.channel == ctx.channel and count < 2 and msg.content.lower() == 'me'

        try:
            answer = await bot.wait_for('message',timeout=20, check=check)
            count += 1
            await ctx.author.send('Choose between rock, paper or scissors')
            await answer.author.send('Choose between rock, paper or scissors')

            #checks the answers are from the players 
            def check(msg):
                return msg.author.name == ctx.author.name or msg.author.name == answer.author.name
        
            try:
                answer1 = await bot.wait_for('message',timeout=20, check=check)
                answer2 = await bot.wait_for('message',timeout=20, check=check)
                winner = RPS.compare(answer1.content.lower(),answer1.author.name, answer2.content.lower(),answer2.author.name)
                #Compares the results and find the winner or if it is a tie
                if winner == ctx.author.name:
                    await ctx.send(ctx.author.nick + ' won!')
                elif winner == answer.author.name:
                    await ctx.send(answer.author.nick + ' won!')
                elif winner == 'It\'s a tie!':
                    await ctx.send('It\'s a tie!')
                else:
                    await ctx.send('One of you twats couldn\'t spell, try again')
            except:
                await ctx.send('One of you was too slow, try again')
        except:
            await ctx.send('No one wanted to play, get some friends')
            
#Coin flip simulator
@bot.command(name = 'coinflip', help = 'simulate flipping a coin with complete unbiased random')
async def coin_flip(ctx):
    await ctx.send('https://tenor.com/view/coin-toss-coin-toss-gif-5017733')
    await asyncio.sleep(1)
    await ctx.send(random.choice(['Heads', 'Tails']))

#displays all the robo bot commands
@bot.command(name = 'commands', help = 'displays all the commands Robo Bot serves')
async def commands(ctx):
    embed = discord.Embed(
            title = 'Robo Bot Commands',
            description = ('\n'.join(command)),
            colour = discord.Colour.dark_red()
            )
    await ctx.send(embed=embed)

#post 2 gifs to cover the screen
@bot.command(name = 'cleanup', help = 'Will post two gifs to cover up whatever abomination was on the screen')
async def clean_up(ctx):
    await ctx.send('https://tenor.com/view/get-this-shit-out-club-penguin-mop-just-let-me-get-rid-of-the-shit-post-above-gif-17264103')
    await ctx.send('https://tenor.com/view/pussy-rub-cleaning-window-window-clean-cat-clean-cute-gif-16940085')

#8ball
@bot.command(name = '8ball', help = 'A magic 8-ball that will answer any question')
async def _8ball(ctx):
    await ctx.send('https://tenor.com/view/eight-ball-gif-10769378')
    await asyncio.sleep(3)
    await ctx.send(random.choice(_8ball_ans))

#Connect 4
@bot.command(name = 'connect4', help = 'A two player game where you place coins until one colour has 4 of their coins stacked contiguously in any direction')
async def connect_4(ctx):
    if ctx.guild.name == 'Abnormal title':
        await ctx.send('Whoever wants to play, say \"me\"')
        count = 0

        #Checks if the reply is not from the original caller of the program and if it is from the same channel
        def check(msg):
            return msg.author != ctx.author and msg.channel == ctx.channel and count < 2 and msg.content.lower() == 'me'
        try:
            player = await bot.wait_for('message',timeout=20, check=check)
            count += 1
            #chooses who starts
            await ctx.send('Heads blue starts, Tails red starts')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/coin-toss-coin-toss-gif-5017733')
            turn = random.choice([':red_circle:',':blue_circle:'])
            await asyncio.sleep(1)
            if turn == ':blue_circle:':
                    await ctx.send('Heads')
            else:
                await ctx.send('Tails')
            await asyncio.sleep(1)
            board = C4.get_board()
            game_over = False
            temp_board = []
            for row in board:
                temp_board.append(''.join(row)+'\n')
            embed = discord.Embed(
            title = f'{ctx.author.nick}(blue)/{player.author.nick}(red)',
            description = (''.join(temp_board)),
            colour = discord.Colour.dark_red()
            )
            await ctx.send(embed=embed)

            while game_over == False:
                await ctx.send('Place your ' + turn + ', from 1-7')
                if turn == ':blue_circle:':
                    player_turn = ctx.author.nick
                else:
                    player_turn = player.author.nick
                    
                def check(msg):
                    return msg.author.nick == player_turn and msg.channel == ctx.channel

                try:
                    answer = await bot.wait_for('message',timeout = 120, check=check)
                    if answer.content.lower() == 'forfeit':
                        if answer.author.nick == player.author.nick:
                            await ctx.send(f'**{ctx.author.nick} wins by forfeit**')
                            game_over = True
                            C4.save(ctx.author.nick, player.author.nick)
                            break
                        else:
                            await ctx.send(f'**{player.author.nick} wins by forfeit**')
                            game_over = True
                            C4.save(player.author.nick, ctx.author.nick)
                            break
                    try:
                        move = C4.check_move(board, (int(answer.content)-1))
                        if move == False:
                            await ctx.send('invalid move, Column has been filled.')
                        else:
                            board[int(move)][int(answer.content)-1] = turn
                            turn = C4.change_turn(turn)
                            temp_board = []
                            for row in board:
                                temp_board.append(''.join(row)+'\n')
                            embed = discord.Embed(
                            title = f'{ctx.author.nick}(blue)/{player.author.nick}(red)',
                            description = (''.join(temp_board)),
                            colour = discord.Colour.dark_red()
                            )
                            await ctx.send(embed=embed)
                            if C4.check_win(board) == ':blue_circle:':
                                await ctx.send(f'**{ctx.author.nick} won**')
                                game_over = True
                                C4.save(ctx.author.nick, player.author.nick)
                            elif C4.check_win(board) == ':red_circle:':
                                await ctx.send(f'**{player.author.nick} won**')
                                game_over = True
                                C4.save(player.author.nick, ctx.author.nick)
                            elif C4.check_win(board) == 'Tie':
                                await ctx.send('**It\'s a tie**')
                                game_over = True
                    except:
                        await ctx.send('Invalid input, stop being a fool')
                except:
                    await ctx.send('Ran out of time, Game over')
                    game_over = True
                                   
        except:
            await ctx.send('No one wanted to play, get some friends')

#Gay count because rejus says it way too much
@bot.command(name = 'gaycount', help = 'This is a count of how many times the word \"gay\" has been said')
async def gay_count(ctx):
    if ctx.guild.name == 'Abnormal title':
        count = []
        gay_list = []
        with open('Gay_count.txt','r') as r:
            info = r.readlines()
            for row in info:
                cleanUp = row.strip('\n').split(',')
                count.append([cleanUp[0], cleanUp[1]])
        for row in count:
            gay_list.append(row[0] + ' has said \"gay\" ' + row[1] + ' times')
        embed = discord.Embed(
                title = 'Gay count',
                description = ('\n'.join(gay_list)),
                colour = discord.Colour.dark_red()
                )
        await ctx.send(embed=embed)

#N word count cuz josh asked for it
@bot.command(name = 'ncount', help = 'This is a count of how many times the word \"nigga\" has been said')
async def n_count(ctx):
    if ctx.guild.name == 'Abnormal title':
        count = []
        n_list = []
        with open('n_count.txt','r') as r:
            info = r.readlines()
            for row in info:
                cleanUp = row.strip('\n').split(',')
                count.append([cleanUp[0], cleanUp[1]])
        for row in count:
            n_list.append(row[0] + ' has said the N word ' + row[1] + ' times')
        embed = discord.Embed(
                title = 'N word count',
                description = ('\n'.join(n_list)),
                colour = discord.Colour.dark_red()
                )
        await ctx.send(embed=embed)

#Connect 4 leaderboard
@bot.command(name = 'c4leaderboard' , help = 'displays the Connect 4 leaderboard')
async def connect4_leaderboard(ctx):
    if ctx.guild.name == 'Abnormal title':
        await ctx.send('Choose between "overall" or say someone\'s name')

        #Checks if the reply is not from the original caller of the program and if it is from the same channel
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        #try:
        answer = await bot.wait_for('message',timeout = 30, check=check)
        if answer.content.lower() == 'overall':
            scores = C4.load(answer.content)
            embed = discord.Embed(
                title = 'Connect 4 Leaderboard',
                description = ('\n'.join(scores)),
                colour = discord.Colour.dark_red()
                )
            await ctx.send(embed=embed)
            
        else:
            if C4.load(answer.content.lower()) == None:
                await ctx.send('Person does not exist or they have played 0 games')
            else:
                person = C4.load(answer.content.lower())
                for member in ctx.guild.members:
                    try:
                        if member.nick.lower() == answer.content.lower():
                            user = member.nick
                            pfp = member.avatar_url
                    except:
                        print('false')
                total = person[2]
                wins = 0
                loss = 0
                count = 0
                for i in range(3, len(person)):
                    count += 1
                    try:
                        wins += int(person[i])
                    except:
                        print('name founded instead of number')
                loss = int(total) - wins
                count = count//2
                if total == '0':
                    ratio = '0'
                elif loss == 0:
                    ratio = str(wins)
                else:
                    ratio = str(round((wins/loss),2))
                embed = discord.Embed(
                title = ('__' + user + '__'),
                description = ('Total games: ' + person[2] + '\nTotal wins: ' + str(wins) + '\nW/L ratio: ' + ratio),
                colour = discord.Colour.dark_red()
                )
                embed.set_thumbnail(url = pfp)
                embed.set_author(name = 'Connect 4 leaderboard')
                for i in range(0,count):
                    embed.add_field(name = ('vs ' + person[i+3]), value = person[i+4], inline = True)
                await ctx.send(embed=embed)
        #except:
         #   await ctx.send('Ran out of time to answer')

        


############################################################################################################################################################################################
bot.run(TOKEN)

import discord
from discord.ext import commands
import sys
import asyncio
import random
sys.path.insert(1, 'cogs/modules')
import Rock_Paper_Scissor as RPS
import Ultimate_Tic_Tac_Toe as TTT
import Connect_4 as C4




class games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Rock Paper Scissor
    @commands.command(name = 'rsp', help = 'The classic game, Rock Paper Scissor')
    async def rsp(self, ctx):
        await ctx.send('Whoever wants to play, say \"me\"')
        count = 0

        #Checks if the reply is not from the original caller of the program and if it is from the same channel
        def check(msg):
            return msg.author != ctx.author and msg.channel == ctx.channel and count < 2 and msg.content.lower() == 'me'

        try:
            answer = await self.bot.wait_for('message',timeout=20, check=check)
            count += 1
            await ctx.author.send('Choose between rock, paper or scissors')
            await answer.author.send('Choose between rock, paper or scissors')

            #checks the answers are from the players 
            def check(msg):
                return msg.author.name == ctx.author.name or msg.author.name == answer.author.name

            try:
                answer1 = await self.bot.wait_for('message',timeout=20, check=check)
                answer2 = await self.bot.wait_for('message',timeout=20, check=check)
                winner = RPS.compare(answer1.content.lower(),answer1.author.name, answer2.content.lower(),answer2.author.name)
                #Compares the results and find the winner or if it is a tie
                if winner == ctx.author.name:
                    await ctx.send(ctx.author.name + ' won!')
                elif winner == answer.author.name:
                    await ctx.send(answer.author.name + ' won!')
                elif winner == 'It\'s a tie!':
                    await ctx.send('It\'s a tie!')
                else:
                    await ctx.send('One of you twats couldn\'t spell, try again')
            except:
                await ctx.send('One of you was too slow, try again')
        except:
            await ctx.send('No one wanted to play, get some friends')
    
    #Connect 4
    @commands.command(name = 'c4', help = 'The classic game where you are trying to allign 4 coins of the same colour either by vertical, horizontal or diagonal')
    async def connect_4(self, ctx):
        emoji = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '❌']
        await ctx.send('Whoever wants to play, say \"me\"')
        count = 0

        #Checks if the reply is not from the original caller of the program and if it is from the same channel
        def check(msg):
            return msg.author != ctx.author and msg.channel == ctx.channel and count < 2 and msg.content.lower() == 'me'

        try:
            player = await self.bot.wait_for('message',timeout=20, check=check)
            count += 1
            #chooses who starts
            await ctx.send(f'Heads {ctx.author.name} starts, Tails {player.author.name} starts')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/coin-toss-coin-toss-gif-5017733')
            turn = random.choice([':red_circle:',':blue_circle:'])
            await asyncio.sleep(1)
            if turn == ':blue_circle:':
                    await ctx.send('Heads')
            else:
                await ctx.send('Tails')
            await asyncio.sleep(2)
            board = C4.get_board()
            game_over = False
            temp_board = []
            for row in board:
                temp_board.append(''.join(row)+'\n')
            embed = discord.Embed(
            title = f'{ctx.author.name}:blue_circle:**/**{player.author.name}:red_circle:',
            description = (''.join(temp_board)),
            colour = discord.Colour.dark_red()
            )
            display = await ctx.send(embed=embed)
            for row in emoji:
                await display.add_reaction(row)
            tell = await ctx.send('Place your ' + turn + ', from 1-7')

            while game_over == False:
                await tell.edit(content = 'Place your ' + turn + ', from 1-7')
                if turn == ':blue_circle:':
                    player_turn = ctx.author
                else:
                    player_turn = player.author
                    
                def check(reaction, user):
                    return user == player_turn 

                try:
                    answer = await self.bot.wait_for('reaction_add',timeout = 120, check=check)
                    reaction = str(answer[0])
                    
                    if reaction == '❌':
                        if answer[1] == player.author:
                            await tell.edit(content = f'**{ctx.author.name} wins by forfeit**')
                            game_over = True
                            continue
                        else:
                            await tell.edit(content = f'**{player.author.name} wins by forfeit**')
                            game_over = True
                            continue
                    

                    try:
                        number = (int(reaction[0]) - 1)
                        move = C4.check_move(board, number)
                        if move == False:
                            await ctx.send('invalid move, Column has been filled.')
                        else:
                            board[int(move)][number] = turn
                            turn = C4.change_turn(turn)
                            temp_board = []
                            for row in board:
                                temp_board.append(''.join(row)+'\n')
                            embed = discord.Embed(
                            title = f'{ctx.author.name}:blue_circle:**/**{player.author.name}:red_circle:',
                            description = (''.join(temp_board)),
                            colour = discord.Colour.dark_red()
                            )
                            await display.edit(embed=embed)
                            await display.remove_reaction(reaction, player_turn)
                            if C4.check_win(board) == ':blue_circle:':
                                await tell.edit(content = f'**{ctx.author.name} won**')
                                game_over = True
                            elif C4.check_win(board) == ':red_circle:':
                                await tell.edit(content = f'**{player.author.name} won**')
                                game_over = True
                            elif C4.check_win(board) == 'Tie':
                                await tell.edit(content = '**It\'s a tie**')
                                game_over = True
                                
                    except:
                        await tell.edit(content = 'What a dumbass adding more emojis, repent for 5 seconds dipshit')
                        await asyncio.sleep(9)
                        await display.remove_reaction(reaction, player_turn)
                except:
                    await ctx.send('dude dashed, **Game over**')
                    game_over = True
                                        
        except:
            await ctx.send('No one wanted to play, get some friends')

    #Ultimate Tic Tac Toe
    @commands.command(name = 'uttt', help = 'A variation of Tic Tac Toe that consists of a 3x3 grid with individual 3x3 grids inside each square called big grid and small grid respectively. Like Tic Tac Toe, you win by having 3 contiguous symbols lined up horizontally, vertically or diagonally but this applies to both big and small grid and the objective is to win the big grid. When making a move in a small grid, you are influencing the opponents move by sending them to the corresponding small grid coordinates in the big grid. However, if you send the opponent to an already won small square then they can choose anywhere on the big grid to go.')
    async def uttt(self, ctx):
        await ctx.send('Whoever wants to play, say \"me\"')
        count = 0

        #Checks if the reply is not from the original caller of the program and if it is from the same channel
        def check(msg):
            return msg.author != ctx.author and msg.channel == ctx.channel and count < 2 and msg.content.lower() == 'me'
        
        try:
            emoji = ['1️⃣', '2️⃣', '3️⃣','🔁','❌']
            player = await self.bot.wait_for('message',timeout=20, check=check)
            count += 1
            #chooses who starts
            await ctx.send(f'Heads {ctx.author.name} starts, Tails {player.author.name} starts')
            await asyncio.sleep(1)
            await ctx.send('https://tenor.com/view/coin-toss-coin-toss-gif-5017733')
            turn = random.choice([':x:',':o:'])
            await asyncio.sleep(1)
            if turn == ':x:':
                    await ctx.send('Heads')
            else:
                await ctx.send('Tails')
            await asyncio.sleep(2)
            board = TTT.get_board()
            board_backend = TTT.get_backend()
            game_over = False
            mode = 'free'
            embed = discord.Embed(
            title = f'{ctx.author.name}:x:**/**{player.author.name}:o:',
            description = TTT.display(board),
            colour = discord.Colour.dark_red()
            )
            embed.set_footer(text = 'Pending...')
            display = await ctx.send(embed=embed)
            for row in emoji:
                await display.add_reaction(row)
            tell_mode = await ctx.send('You can move anywhere')
            ask = await ctx.send('Pending...')

            while game_over == False:
                if turn == ':x:':
                    player_turn = ctx.author
                else:
                    player_turn = player.author
                    
                embed = discord.Embed(
                title = f'{ctx.author.name}:x:**/**{player.author.name}:o:',
                description = TTT.display(board),
                colour = discord.Colour.dark_red()
                )
                embed.set_footer(text = f'It is {player_turn.name}\'s turn')
                await display.edit(embed=embed)
                

                if mode == 'free':
                    await tell_mode.edit(content = 'You can move anywhere')

                    try:
                        #Row
                        await ask.edit(content = 'Which big row?')

                        def check(reaction, user):
                            return user == player_turn 

                        answer = await self.bot.wait_for('reaction_add',timeout = 180, check=check)
                        reaction = str(answer[0])

                        if reaction == '❌':
                            if answer[1] == player.author:
                                await ask.edit(content = f'**{ctx.author.name} wins by forfeit**')
                                game_over = True
                                continue
                                
                            else:
                                await ask.edit(content = f'**{player.author.name} wins by forfeit**')
                                game_over = True
                                continue
                        if reaction == '🔁':
                            await ask.edit(content = 'Redoing...')
                            await asyncio.sleep(1)
                            await display.remove_reaction(reaction, player_turn)
                            continue
                                
                        try:
                            row = (int(reaction[0]) - 1)
                            await display.remove_reaction(reaction, player_turn)
                            
                            try:
                                #Col
                                await ask.edit(content = 'Which big column?')

                                def check(reaction, user):
                                    return user == player_turn 


                                answer = await self.bot.wait_for('reaction_add',timeout = 180, check=check)
                                reaction = str(answer[0])

                                if reaction == '❌':
                                    if answer[1] == player.author:
                                        await ask.edit(content = f'**{ctx.author.name} wins by forfeit**')
                                        game_over = True
                                        continue
                                        
                                    else:
                                        await ask.edit(content = f'**{player.author.name} wins by forfeit**')
                                        game_over = True
                                        continue
                                if reaction == '🔁':
                                    await ask.edit(content = 'Redoing...')
                                    await asyncio.sleep(1)
                                    await display.remove_reaction(reaction, player_turn)
                                    continue

                                try:
                                    col = (int(reaction[0]) - 1)
                                    await display.remove_reaction(reaction, player_turn)
                                    
                                    try:
                                        #move_row
                                        await ask.edit(content = 'Which small row?')

                                        def check(reaction, user):
                                            return user == player_turn 


                                        answer = await self.bot.wait_for('reaction_add',timeout = 180, check=check)
                                        reaction = str(answer[0])

                                        if reaction == '❌':
                                            if answer[1] == player.author:
                                                await ask.edit(content = f'**{ctx.author.name} wins by forfeit**')
                                                game_over = True
                                                continue
                                                
                                            else:
                                                await ask.edit(content = f'**{player.author.name} wins by forfeit**')
                                                game_over = True
                                                continue
                                        if reaction == '🔁':
                                            await ask.edit(content = 'Redoing...')
                                            await asyncio.sleep(1)
                                            await display.remove_reaction(reaction, player_turn)
                                            continue

                                        try:
                                            move_row = (int(reaction[0]) - 1)
                                            await display.remove_reaction(reaction, player_turn)
                                            
                                            try:
                                                #move_col
                                                await ask.edit(content = 'Which small column?')

                                                def check(reaction, user):
                                                    return user == player_turn 


                                                answer = await self.bot.wait_for('reaction_add',timeout = 180, check=check)
                                                reaction = str(answer[0])

                                                if reaction == '❌':
                                                    if answer[1] == player.author:
                                                        await ask.edit(content = f'**{ctx.author.name} wins by forfeit**')
                                                        game_over = True
                                                        continue
                                                        
                                                    else:
                                                        await ask.edit(content = f'**{player.author.name} wins by forfeit**')
                                                        game_over = True
                                                        continue
                                                if reaction == '🔁':
                                                    await ask.edit(content = 'Redoing...')
                                                    await asyncio.sleep(1)
                                                    await display.remove_reaction(reaction, player_turn)
                                                    continue

                                                try:
                                                    move_col = (int(reaction[0]) - 1)
                                                    await display.remove_reaction(reaction, player_turn)

                                                    if board_backend[row][col] == ':black_large_square:':
                                                        if board[row][col][move_row][move_col] == ':black_large_square:':
                                                            board[row][col][move_row][move_col] = turn

                                                            if TTT.check_win(board[row][col]) == turn: # Check small grid win
                                                                board_backend[row][col] = turn
                                                                
                                                            if TTT.check_win(board_backend) == turn: #Check big grid win
                                                                if turn == ':x:':
                                                                    await ask.edit(content = f'**{ctx.author.name} won**')
                                                                else:
                                                                    await ask.edit(content = f'**{player.author.name} won**')
                                                                embed = discord.Embed(
                                                                title = f'{ctx.author.name}:x:**/**{player.author.name}:o:',
                                                                description = TTT.display(board),
                                                                colour = discord.Colour.dark_red()
                                                                )
                                                                embed.set_footer(text = f'It is {player_turn.name}\'s turn')
                                                                await display.edit(embed=embed)
                                                                game_over = True

                                                            small_tie = TTT.check_tie(board[row][col], 'small')     #Checks for tie  
                                                            big_tie = TTT.check_tie(board_backend, 'big')
                                                            
                                                            if small_tie != 'not tie':                  #Checks for small tie
                                                                board_backend[row][col] = 'tie'
                                                                
                                                            if big_tie != 'not tie':                    #Checks for big tie
                                                                if big_tie == 'tie':
                                                                    await ask.edit(content = 'Its a tie')
                                                                else:
                                                                    if big_tie == ':x:':
                                                                        await ask.edit(content = f'**{ctx.author.name} won**')
                                                                    else:
                                                                        await ask.edit(content = f'**{player.author.name} won**')
                                                                embed = discord.Embed(
                                                                title = f'{ctx.author.name}:x:**/**{player.author.name}:o:',
                                                                description = TTT.display(board),
                                                                colour = discord.Colour.dark_red()
                                                                )
                                                                embed.set_footer(text = f'It is {player_turn.name}\'s turn')
                                                                await display.edit(embed=embed)
                                                                game_over = True
                                                                
                                                            row = move_row
                                                            col = move_col
                                                            turn = TTT.change_turn(turn)
                                                            mode = TTT.check_mode(board_backend, row, col)
                                                            
                                                        else:
                                                            await ask.edit(content = 'Coordinate occupied')
                                                            await asyncio.sleep(2)

                                                    else:
                                                        await ask.edit(content = 'You are retarded, so retarded that you lose a turn')
                                                        await asyncio.sleep(5)
                                                        turn = TTT.change_turn(turn)
                                                except:
                                                    await ask.edit(content = 'What a dumbass adding a different emoji, repent for 5 seconds dipshit')
                                                    await asyncio.sleep(9)
                                                    await display.remove_reaction(reaction, player_turn)
                                            except:
                                                await ask.edit(content = 'Slow as a turtle, **Game Over**')
                                                game_over = True
                                        except:
                                            await ask.edit(content = 'What a dumbass adding a different emoji, repent for 5 seconds dipshit')
                                            await asyncio.sleep(9)
                                            await display.remove_reaction(reaction, player_turn)
                                    except:
                                        await ask.edit(content = 'Slower than a sloth, **Game Over**')
                                        game_over = True    
                                except:
                                    await ask.edit(content = 'What a dumbass adding a different emoji, repent for 5 seconds dipshit')
                                    await asyncio.sleep(9)
                                    await display.remove_reaction(reaction, player_turn)
                            except:
                                await ask.edit(content = 'Time caught up, **Game Over**')
                                game_over = True
                        except:
                            await ask.edit(content = 'What a dumbass adding a different emoji, repent for 5 seconds dipshit')
                            await asyncio.sleep(9)
                            await display.remove_reaction(reaction, player_turn)

                    except:
                        await ask.edit(content = 'Ran out of time, **Game Over**')
                        game_over = True

                else:
                    await tell_mode.edit(content  = ('row ' + str(row + 1) + ' and column ' + str(col + 1)))

                    
                    #move_row
                    await ask.edit(content = 'Which small row?')

                    def check(reaction, user):
                        return user == player_turn 

                    try:
                        answer = await self.bot.wait_for('reaction_add',timeout = 180, check=check)
                        reaction = str(answer[0])

                        if reaction == '❌':
                            if answer[1] == player.author:
                                await ask.edit(content = f'**{ctx.author.name} wins by forfeit**')
                                game_over = True
                                continue
                                
                            else:
                                await ask.edit(content = f'**{player.author.name} wins by forfeit**')
                                game_over = True
                                continue
                        if reaction == '🔁':
                            await ask.edit(content = 'Redoing...')
                            await asyncio.sleep(1)
                            await display.remove_reaction(reaction, player_turn)
                            continue

                        try:
                            move_row = (int(reaction[0]) - 1)
                            await display.remove_reaction(reaction, player_turn)

                            #move_col
                            await ask.edit(content = 'Which small column?')

                            def check(reaction, user):
                                return user == player_turn 

                            try:
                                answer = await self.bot.wait_for('reaction_add',timeout = 180, check=check)
                                reaction = str(answer[0])

                                if reaction == '❌':
                                    if answer[1] == player.author:
                                        await ask.edit(content = f'**{ctx.author.name} wins by forfeit**')
                                        game_over = True
                                        continue
                                        
                                    else:
                                        await ask.edit(content = f'**{player.author.name} wins by forfeit**')
                                        game_over = True
                                        continue
                                if reaction == '🔁':
                                    await ask.edit(content = 'Redoing...')
                                    await asyncio.sleep(1)
                                    await display.remove_reaction(reaction, player_turn)
                                    continue
                                try:    
                                    move_col = (int(reaction[0]) - 1)
                                    await display.remove_reaction(reaction, player_turn)
                                    
                                    if board[row][col][move_row][move_col] == ':black_large_square:':
                                        board[row][col][move_row][move_col] = turn
            
                                        
                                        if TTT.check_win(board[row][col]) == turn: # Check small grid win
                                            board_backend[row][col] = turn
                                        
                                        if TTT.check_win(board_backend) == turn: #check big win
                                            if turn == ':x:':
                                                await ask.edit(content = f'**{ctx.author.name} won**')
                                            else:
                                                await ask.edit(content = f'**{player.author.name} won**')
                                            embed = discord.Embed(
                                            title = f'{ctx.author.name}:x:**/**{player.author.name}:o:',
                                            description = TTT.display(board),
                                            colour = discord.Colour.dark_red()
                                            )
                                            embed.set_footer(text = f'It is {player_turn.name}\'s turn')
                                            await display.edit(embed=embed)
                                            game_over = True
                                            
                                        small_tie = TTT.check_tie(board[row][col], 'small')     #Checks for tie  
                                        big_tie = TTT.check_tie(board_backend, 'big')
                                        
                                        if small_tie != 'not tie':                  #Checks for small tie
                                            board_backend[row][col] = 'tie'
                                            
                                        if big_tie != 'not tie':                    #Checks for big tie
                                            if big_tie == 'tie':
                                                await ask.edit(content = 'Its a tie')
                                            else:
                                                if big_tie == ':x:':
                                                    await ask.edit(content = f'**{ctx.author.name} won**')
                                                else:
                                                    await ask.edit(content = f'**{player.author.name} won**')
                                            embed = discord.Embed(
                                            title = f'{ctx.author.name}:x:**/**{player.author.name}:o:',
                                            description = TTT.display(board),
                                            colour = discord.Colour.dark_red()
                                            )
                                            embed.set_footer(text = f'It is {player_turn.name}\'s turn')
                                            await display.edit(embed=embed)
                                            game_over = True

                                            
                                        row = move_row
                                        col = move_col
                                        turn = TTT.change_turn(turn)
                                        mode = TTT.check_mode(board_backend, row, col)
                                        
                                    else:
                                        await ask.edit(content = 'Coordinate is occupied')
                                        await asyncio.sleep(2)

                                except:
                                    await ask.edit(content = 'What a dumbass adding a different emoji, repent for 5 seconds dipshit')
                                    await asyncio.sleep(9)
                                    await display.remove_reaction(reaction, player_turn)
                            except:
                                await ask.edit(content = 'Too slow, **Game Over**')
                                game_over = True
                        except:
                            await ask.edit(content = 'What a dumbass adding a different emoji, repent for 5 seconds dipshit')
                            await asyncio.sleep(9)
                            await display.remove_reaction(reaction, player_turn)
                    except:
                        await ask.edit(content = 'Slow ass peasant, **Game Over**')
                        game_over = True
                                            
        except:
            await ctx.send('No one wanted to play, get some friends')
    

def setup(bot):
    bot.add_cog(games(bot))

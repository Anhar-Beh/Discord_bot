import random
import re

def check_move(table, column):
    stop = False
    count = 5
    while stop == False:
        try:
            if table[count][column] == ':white_circle:':
                return (str(count))
            elif table[count][column] != ':white_circle:':
                count -= 1
        except:
            return (False)
        
def change_turn(player_turn):
    if player_turn == ':blue_circle:':
        return(':red_circle:')
    else:
        return(':blue_circle:')

def check_win(board):
    player1 = re.compile(':blue_circle::blue_circle::blue_circle::blue_circle:')
    player2 = re.compile(':red_circle::red_circle::red_circle::red_circle:')
    #If it is a tie
    count = 0
    for col in board[0]:
        if col != ':white_circle:':
            count +=1
        if count == 7:
            return('Tie')
    #horizontal
    for row in board:
        string = ''.join(row)
        search1 = player1.search(string)
        search2 = player2.search(string)
        if search1 != None:
            return(':blue_circle:')
        if search2 != None:
            return (':red_circle:')
    #vertical
    for c in range(0,7):
        col = []
        for r in range(0,6):
            col.append(board[r][c])
        string = ''.join(col)
        search1 = player1.search(string)
        search2 = player2.search(string)
        if search1 != None:
            return(':blue_circle:')
        if search2 != None:
            return (':red_circle:')
    #diagonal
    #diag1
    #first three north east diagonal        
    for i in range(4,7):
        diag = []
        for p in range(0,i):
            diag.append(board[p][(i-1)-p])
        string = ''.join(diag)
        search1 = player1.search(string)
        search2 = player2.search(string)
        if search1 != None:
            return(':blue_circle:')
        if search2 != None:
            return (':red_circle:')
    #other three north east diagonal
    for i in range(3,0,-1):
        diag = []
        coord = []
        for p in range(5,i-2,-1):
            coord.append(p)
        for a in range(i,7):
            diag.append(board[coord[(a-7)+len(coord)]][a])
        string = ''.join(diag)
        search1 = player1.search(string)
        search2 = player2.search(string)
        if search1 != None:
            return(':blue_circle:')
        if search2 != None:
            return (':red_circle:')
    #diag2
    #first three north west diagonal
    count = 3
    for i in range(4,7):
        diag = []
        for p in range(0,i):
                diag.append(board[p][p+count])
        count -=1
        string = ''.join(diag)
        search1 = player1.search(string)
        search2 = player2.search(string)
        if search1 != None:
            return(':blue_circle:')
        if search2 != None:
            return (':red_circle:')
    #first three north west diagonal
    count = 2
    for i in range(3,0,-1):
        diag = []
        for p in range(5,i-2,-1):
                diag.append(board[p][p-count])
        count -= 1
        string = ''.join(diag)
        search1 = player1.search(string)
        search2 = player2.search(string)
        if search1 != None:
            return(':blue_circle:')
        if search2 != None:
            return (':red_circle:')
            
def get_board():
    game_board = []
    for i in range(0,6):
        game_board.append([])
        for p in range(0,7):
            game_board[i].append(':white_circle:')
        
    return(game_board)


def save(winner, opponent):
    with open('Connect4_leaderboard.txt','r') as f:
        info = f.readlines()
        data = []
        for row in info:
            data.append(row.strip('\n').split(','))

    with open('Connect4_leaderboard.txt','w') as f:
        foundw = False
        foundl = False
        for row in data:
            if row[0] == winner:
                foundw = True
                foundop = False
                for i in range(0, len(row)):
                    if row[i] == 'total':
                        row[i+1] = str(int(row[i+1])+1)
                    if row[i] == opponent:
                        row[i+1] = str(int(row[i+1])+1)
                        foundop = True
                if foundop == False:
                    row.append(opponent)
                    row.append('1')
            if row[0] == opponent:
                foundl = True
                for i in range(0, len(row)):
                    if row[i] == 'total':
                        row[i+1] = str(int(row[i+1])+1)
                        
        if foundw == False:
            data.append([winner, 'total', '1', opponent, '1'])
        if foundl == False:
            data.append([opponent, 'total', '1'])

        for row in data:
            f.write(','.join(row))
            f.write('\n')
            
def load(specific):
    with open('Connect4_leaderboard.txt','r') as f:
        info = f.readlines()
        data= []
        for row in info:
            data.append(row.strip('\n').split(','))
            
        if specific == 'overall':
            try:
                leaderboard = []
                for row in data:
                    total = int(row[2])
                    wins = 0
                    loss = 0
                    for i in range(3, len(row)):
                        try:
                            wins += int(row[i])
                        except:
                            print('name founded instead of number')
                    loss = total - wins
                    if loss == 0:
                        ratio = wins
                        leaderboard.append(row[0] + ' has a W/L ratio of ' + str(ratio))
                    elif wins == 0:
                        ratio = 0
                        leaderboard.append(row[0] + ' has a W/L ratio of ' + str(ratio))
                    else:
                        ratio = str(round(wins/loss),2)
                        leaderboard.append(row[0] + ' has a W/L ratio of ' + str(ratio))
                        
                return (leaderboard)
            
            except:
                return (None)
        else:
            found = False
            for row in data:
                if row[0] == specific:
                    found = True
                    return (row)
                
            if found == False:
                return(None)
                
                    
                    
            
#############################################################################################################################################################################################    



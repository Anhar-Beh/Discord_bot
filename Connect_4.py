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
    win = (winner + '_lead\n')
    key = re.compile('_lead')
    with open('Connect4_leaderboard.txt','r') as f:
        info = f.readlines()
        count = 0
        attribute = []
        temp = []
        for row in info:
            if row == win:
                for i in range(count+1, count+6):
                    attribute.append(info[i].strip('\n').split(','))
                count += 1
                    
            else:
                if key.search(row) != None:
                    for i in range(count, count+6):
                        temp.append(info[i])
                count += 1
                
    with open('Connect4_leaderboard.txt','w') as f:
        f.write(winner + '_lead\n') 
        for row in attribute:
            if row[0] == 'total':
                row[1] = str(int(row[1]) + 1)
                
            if row[0] == opponent:
                row[1] = str(int(row[1]) + 1)
                 
            f.write(row[0] + ',' + row[1] + '\n')
        for row in temp:
            f.write(row)

def load(specific):
    key = re.compile('_lead')
    #to post all W/L
    if specific == 'overall':
        with open('Connect4_leaderboard.txt','r') as f:
            info = f.readlines()
            count = 0
            leader_board = []
            for row in info:
                temp = []
                wins = 0
                loss = 0
                if key.search(row) != None:
                    for i in range(1,6):
                        temp.append(info[count+i].strip('\n').split(','))
                    for i in range(2,6):
                        wins += int(temp[i-1][1])
                    loss = int(temp[0][1])-wins

                    try:
                        leader_board.append(row[0:-6] + ' has a W/L ratio of ' + str(round((wins/loss),2)))
                    except:
                        leader_board.append(row[0:-6] + ' has played 0 games')
                    count +=1
                else:
                    count += 1
            return(leader_board)
    else:
        with open('Connect4_leaderboard.txt','r') as f:
            info = f.readlines()
            count = 0
            person = []
            found = False
            for row in info:
                temp = []
                wins = 0
                loss = 0
                if key.search(row) != None:
                    if row[0:-6].lower() == specific:
                        for i in range(count+1, count+6):
                            person.append(info[i].strip('\n').split(','))
                            found = True
                        for i in range(1,6):
                            temp.append(info[count+i].strip('\n').split(','))
                        for i in range(2,6):
                            wins += int(temp[i-1][1])
                        loss = int(temp[0][1])-wins
                        person.append(str(wins))
                        person.append(str(loss))
                            
                    count += 1
                else:
                    count += 1
            if found == True:
                return(person)
            else:
                return('Invalid input, person does not exist')
################################################################################    



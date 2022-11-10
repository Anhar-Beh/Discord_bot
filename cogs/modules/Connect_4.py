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



                    
            
#############################################################################################################################################################################################    
print ('Connect 4 is online')


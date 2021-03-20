def get_board():
    board = []
    for i in range(0, 3):
        board.append([])
        for o in range(0,3):
            board[i].append([])
            for p in range(0,3):
                board[i][o].append([':black_large_square:', ':black_large_square:', ':black_large_square:'])
    return (board)

def get_backend():
    board_backend = []
    for i in range(0,3):
        board_backend.append([])
        for o in range(0,3):
            board_backend[i].append(':black_large_square:')
    return(board_backend)


############################################### Modules ############################################
#printing method to display the board
def display(board):
    temp = []
    temp2 = []
    temp3 = []
    for i in range(0, 3):
        temp.append([])
        temp2.append([])
        for o in range(0,3):
            temp[i].append([])
            for p in range(0,3):
                temp[i][o].append(''.join(board[i][p][o]))
            temp2[i].append(' '.join(temp[i][o]))
        temp3.append('\n'.join(temp2[i]))
    return ('\n\n'.join(temp3))


#checks if the player can move freely or with a certain big square   
def check_mode(backend, row, col):
    if backend[row][col] != ':black_large_square:':
        return ('free')
    else:
        return ('restricted')

#checks if the win conditions have been met  
def check_win(square):
    #checking diagonals
    if square[0][0] == square[1][1] == square[2][2]:
        if square[0][0] == ':x:':
            return (':x:')
        if square[0][0] == ':o:':
            return (':o:')           
    if square[0][2] == square[1][1] == square[2][0]:
        if square[0][2] == ':x:':
            return (':x:')
        if square[0][2] == ':o:':
            return (':o:')
                
    for i in range(0,3):
        
        #checking horizontals
        if square[i][0] == square[i][1] and square[i][2] == square[i][0]:
            if square[i][0] == ':x:':
                return (':x:')
            if square[i][0] == ':o:':
                return (':o:')
            
        #checking verticals
        if square[0][i] == square[1][i] and square [2][i] == square [0][i]:
            if square[0][i] == ':x:':
                return (':x:')
            if square[0][i] == ':o:':
                return (':o:')
            
#changes turn
def change_turn(player_turn):
    global turn
    if player_turn == ':x:':
        return (':o:')
    else:
        return (':x:')

def check_tie(square, define):
    for row in square:
        for col in row:
            if col == ':black_large_square:':
                return('not tie')

    if define == 'big':
        count_x = 0
        count_o = 0
        for row in square:
            for col in row:
                if col == ':x:':
                    count_x += 1
                elif col == ':o:':
                    count_o += 1
        if count_x == count_o:
            return ('tie')
        elif count_x > count_o:
            return (':x:')
        else:
            return (':o:')
    else:
        return ('tie')



                    
####################################################################################################
print ('Ultimate Tic Tac Toe online')
        

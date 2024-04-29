import copy

from Check_Functions import check_row, check_column, check_diag_1, check_diag_2, check_board, check_board_bool, create_board

def set_first_field (board, player):
    new_board = copy.deepcopy(board) #new_board=board and even new board=board[:] creates an alias, so the board itself would be changed!
    i = 0
    j = 0
    set = False
    while i < len(new_board) and not set: #-1 not necessesarry because < not <=
        while j < len(new_board[i]) and not set:
            if new_board [i][j] == '' or new_board [i][j] == ' ':
                new_board [i][j] = player
                set = True
            else:
                j +=1
        j = 0
        i += 1
    return new_board

def find_empty_fields(board):
    empty_fields = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            #print(board[i][j])
            if board [i][j] == '' or board [i][j] == ' ':
                position = (i,j)
                empty_fields.append(position) #!! with += the values are added seperately, not as tuples
    return empty_fields

def set_random_field(board, player):
    import random
    new_board = copy.deepcopy(board)
    empty_fields = find_empty_fields(board)
    if empty_fields == []:
        result = 'The given board is full'
    else:
        pick_field = random.randint(0, (len(empty_fields)-1)) #-1 because randint selects a<=x<=b
        field = empty_fields[pick_field]
        r, c = field
        new_board[r][c] = player
        result = new_board
    return result



def set_winner(board, player):
    #sets a winning field
    #Returns an unchanged board if that is not possible
    if check_board_bool(board, player):
        raise Warning('The player has won already')
    new_board = copy.deepcopy(board)
    empties = find_empty_fields(board)
    i = 0
    set = False #set should be replaced everywhere, seems to be buildin
    while i < len(empties) and not set:
        new_board[empties[i][0]][empties[i][1]] = player
        if check_board_bool(new_board, player):
            set = True
        else:
            new_board[empties[i][0]][empties[i][1]] = ''
            i+=1
    return new_board

def prevent_opponent(board, player):
    # set a field of player, so that the other player does not win IN THE NEXT step
    # Returns an unchanged board if that is not possible
    if player == 'x':
        opp = 'o'
    elif player == 'o':
        opp = 'x'
    else:
        raise ValueError('player has no correct symbol, use x or o')
    if check_board_bool(board, opp):
        raise Warning('The opponent has won already')
    new_board = copy.deepcopy(board)
    empties = find_empty_fields(board)
    i = 0
    set = False #set should be replaced everywhere, seems to be buildin
    while i < len(empties) and not set:
        new_board[empties[i][0]][empties[i][1]] = opp
        if check_board_bool(new_board, opp):
            new_board[empties[i][0]][empties[i][1]] = player
            set = True
        else:
            new_board[empties[i][0]][empties[i][1]] = ''
            i+=1
    return new_board

if __name__ == '__main__':
    #board = create_board(3)
    board = [['','o','o'],['x','o','x'],['x',' ',' ']]
    print(board)
    #print(set_first_field(board, 'x'))
    #print(board)
    #print(find_empty_fields(board))
    #print(set_random_field(board, 'x'))
    print(set_winner(board, 'x'))
    print(prevent_opponent(board, 'x'))

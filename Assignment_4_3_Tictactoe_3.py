from Class_4_1_Tictactoe2 import check_row, check_column, check_diag_1, check_diag_2, check_board, create_board

#board = create_board(3)
board = [['x','x','x'],['x','','x'],['o','o',' ']]
print(board)

def set_first_field (board, player):
    new_board = board
    i = 0
    j = 0
    set = False
    while i < len(new_board) and not set:
        while j < len(new_board[i]) and not set:
            if new_board [i][j] == ' ':
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
            if board [i][j] == '' or board [i][j] == ' ':
                position = (i,j)
                empty_fields.append(position) #!! with += the values are added seperately, not as tuples
    return empty_fields

#print(find_empty_fields(board))

def set_random_field(board, player):
    import random
    new_board = board
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



#def set_winner(board, player):
#    empties = find_empty_fields(board)


#print(set_first_field(board, 'x'))
print(set_random_field(board, 'x'))


b = [['x','x','x'],['x','x','o'],['x','o','o']]


def check_row (player, board, r):
    answer = True
    i = 0
    while i < len(board) and answer:
        if board[r][i] != player:
            answer = False
        i += 1
    return answer

def check_column (player, board, c):
    answer = True
    i = 0
    while i < len(board) and answer:
        if board [i][c] != player:
            answer = False
        i += 1
    return answer

def check_diag_1 (player, board): #a litte more efficient with the while loop (loop stops as soon as answer is clear)
    answer = True
    i = 0
    while i < len(board) and answer:
        if board[i][i] != player:
            answer = False
        i += 1
    return answer

def check_diag_2 (player, board):
    answer = True
    i = 0
    while i < len(board) and answer:
        if board[i][len(board)-1-i] != player:
            answer = False
        i += 1
    return answer

def check_board (board):
    x_won = False
    o_won = False
    if check_diag_1('x', board):
        x_won = True
    elif check_diag_2 ('x', board):
        x_won = True
    elif check_diag_1('o', board):
        o_won = True
    elif check_diag_2('o', board):
        o_won = True
    else:
        for i in range(len(board)):
            if check_row('x', board, i):
                x_won = True
            elif check_row('o', board, i):
                o_won = True
        if not x_won:
            for i in range(len(board)):
                if check_column('x', board, i):
                    x_won = True
                elif check_column('o', board, i):
                    o_won = True
    if x_won and o_won:
        result = 'The game was played to far, unclear who won'
    elif x_won:
        result = 'Player x has won'
    elif o_won:
        result = 'Player o has won'
    else:
        result = 'No player has won (yet)'
    return result



def create_board (length): #must be quadratic
    import random
    board = []
    row = []
    for r in range(length):
        for f in range(length):
            field = random.choice(['x', 'o', ' '])
            row += field
        board += [row]
        row = []
    return board

if __name__ == '__main__':

    board = create_board(3)
    print(board)
    print(check_board(board))

    #print(check_diag_1('x', b))
    #print(check_diag_2('o', b))

    #print(check_column('x', b, 0))
    #print(check_column('x', b, 1))
    #print(check_column('x', b, 2))

    #print(check_row('x', b, 0))
    #print(check_row('x', b, 1))
    #print(check_row('x', b, 2))
    #print(check_row('o', b, 2))



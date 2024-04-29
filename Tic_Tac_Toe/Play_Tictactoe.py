import random
from Computer_Player import find_empty_fields, set_random_field, set_winner, prevent_opponent
from Print_Board import tictactoe_board
from Check_Functions import check_board_bool, check_board

def set_field(board, player, row, column):
    if board[row][column] == '' or board[row][column] == ' ':
        board[row][column] = player
        placed = True
    else:
        print('This position is not free')
        placed = False
    return placed


def play_tictactoe():
    board = [['','',''],['','',''],['','','']]
    mode = input('Welcome to Tic Tac Toe! \n Do you want to play agains a second person sitting next to you or against the computer?\n Please enter human or computer:\n')
    while mode != 'computer' and mode != 'human':
        mode = input('This is not a valid keyword.\n Please enter human or computer without spaces or quotation marks!:\n')
    print('You will play agains a ' + mode)
    player = input('Choose your symbol: Either x or o\n')
    while player != 'x' and player != 'o':
        player = input('This is not a valid symbol.\n Please enter x or o (not zero) without spaces or quotation marks!:\n')
    print('Your symbol is ' + player)
    if player == 'x':
        opp = 'o'
        print('Your opponent has the symbol o')
    if player == 'o':
        opp = 'x'
        print('Your opponent has the symbol x')
    starter = input('Do you want to play first or second?\nEnter first, second or random:\n')
    while starter != 'first' and starter != 'second' and starter != 'random':
        starter = input('This is not a valid symbol.\n Please first, second or random without spaces or quotation marks!:\n')
    if starter == 'random':
        start = random.choice([True, False])
        if start:
            print('You will start!')
        else:
            print('Your opponent will start!')
    elif starter == 'first':
        start = True
        print('You will start!')
    elif starter == 'second':
        start = False
        print('Your opponent will start!')
    if mode == 'human':
    #in this case the player starts always
        while not check_board_bool(board, 'x') and not check_board_bool(board, 'o') and find_empty_fields(board) != []:
            placed = False
            while not placed and start:
                print('Its turn for ' + player)
                print('This is the board:')
                tictactoe_board(board)
                row_name = input('In which row do you want to place your stone?\n 1, 2 or 3?\n')
                column_name = input('In which column do you want to place your stone?\n a, b or c?\n')
                row = {'1': 2, '2': 1, '3': 0}.get(row_name, None)
                column = {'a': 0, 'b': 1, 'c': 2}.get(column_name, None)
                if row != None and column != None:
                    placed = set_field(board, player, row, column)
                else:
                    print ('You did not enter a correct field position, please try again')
            placed = False
            if not check_board_bool(board, player) and find_empty_fields(board) != []:
                while not placed:
                    print('Its turn for ' + opp)
                    print('This is the board:')
                    tictactoe_board(board)
                    row_name = input('In which row does ' + opp + ' want to place the stone?\n 1, 2 or 3?\n')
                    column_name = input('In which column does ' + opp + ' want to place the stone?\n a, b or c?\n')
                    row = {'1': 2, '2': 1, '3': 0}.get(row_name, None)
                    column = {'a': 0, 'b': 1, 'c': 2}.get(column_name, None)
                    if row != None and column != None:
                        placed = set_field(board, opp, row, column)
                    else:
                        print('You did not enter a correct field position, please try again')
            tictactoe_board(board)
            start = True
        print(check_board(board))
    if mode == 'computer':
        #print(board) #still without spaces
        while not check_board_bool(board, 'x') and not check_board_bool(board, 'o') and find_empty_fields(board) != []:
            placed = False
            while not placed and start:
                tictactoe_board(board) #changes to spaces in original board!!
                print('Your turn!')
                row_name = input('In which row do you want to place your stone?\n 1, 2 or 3?\n')
                column_name = input('In which column do you want to place your stone?\n a, b or c?\n')
                row = {'1': 2, '2': 1, '3': 0}.get(row_name, None)
                column = {'a': 0, 'b': 1, 'c': 2}.get(column_name, None)
                if row != None and column != None:
                    placed = set_field(board, player, row, column)
                else:
                    print ('You did not enter a correct field position, please try again')
            if not check_board_bool(board, player) and find_empty_fields(board) != []: #check whether board is not full!!
                newboard = set_winner(board, opp)
                if newboard == board:
                    newboard = prevent_opponent(board,opp)
                if newboard == board:
                    newboard = set_random_field(board, opp)
                board = newboard
                print('This is how the computer played:')
            else:
                print('You have won, Congratulations!')
            start = True
        tictactoe_board(board)
        if check_board_bool(board, opp):
            print('The computer has won, sorry!')
        elif not check_board_bool(board, player):
            print('The game is over, noone won')



play_tictactoe()

'''
b = [['','o','x'],['x','x','o'],['','x','']]
print(b)
print(set_field(b, 'x', 2, 1))
print(b)
'''
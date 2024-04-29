import copy


import copy
def tictactoe_board (board):
    list_of_lists = copy.deepcopy(board)
    rows = ['3','2','1']
    columns = ['a', 'b', 'c']
    print('     ', columns[0], ' |  ', columns[1], ' |  ', columns[2], ' ')
    print('-----------------------')
    for r in range(len(list_of_lists)):
        for c in range(len(list_of_lists[r])):
            if list_of_lists[r][c] == '':
                list_of_lists[r][c] = ' '
        print(rows[r]+' |  ',list_of_lists[r][0],' |  ',list_of_lists[r][1],' |  ',list_of_lists[r][2],' |')
        print('---------+------+------')
if __name__ == '__main__':
    b = [['','o','x'],['x','x','o'],['','x','']]
    tictactoe_board(b)

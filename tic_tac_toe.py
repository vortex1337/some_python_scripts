import os
d = {'7':0, '8':1, '9':2, '4':3, '5':4, '6':5, '1':6, '2':7, '3':8}
arr = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
def clear():
    os.system( 'clear' )
def print_board(board):
    print "    |     |    \n  {} |  {}  | {}  \n    |     |    \n--------------\n    |     |    \n  {} |  {}  | {}  \n    |     |    \n--------------\n    |     |    \n  {} |  {}  | {}  \n    |     |    ".format(*board)
def next_turn(board, marker):
    s = str(input())
    clear()
    arr[d[s]] = marker
    print_board(arr)
print_board(arr)
def win_check(arr):
    matrix = []
    j=0
    for i in range(3):
        matrix.append(arr[j:j+3])
        j+=3
    return matrix

while True:
    next_turn(arr,'X')
    print(arr)
    print(win_check(arr))

from SudoSolver import SudokuBoard
from time import time

now = time()
print('Opening the file...')
with open('sudoin.txt') as f:
    board = []
    for i in f:
        board.append([int(num) for num in i.strip()])

print('Processing the board...')
with open('sudoout.txt', 'w') as f:
    for i in SudokuBoard(board).solve():
        print(''.join([str(num) for num in i]), file=f)

print('Done!')
print('Took {} seconds long.', time() - now)

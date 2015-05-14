from SudoSolver import SudokuBoard
from time import time

now = time()
print('Opening the file...')
print('Found this sudoku inside...\n')
with open('sudoin.txt') as f:
    board = []
    for i in f:
        print(i.strip())
        board.append([int(num) for num in i.strip()])

print('\nSolving the sudoku...\n')
with open('sudoout.txt', 'w') as f:
    for i in SudokuBoard(board).solve():
        print(''.join([str(num) for num in i]))
        print(''.join([str(num) for num in i]), file=f)

print('\nDone!')
print('Took {} seconds long.'.format(time() - now))

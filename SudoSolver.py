import unittest
from copy import deepcopy


class SudokuBoard(object):

    """Simulates a sudoku board"""

    BOARD_SIZE = 9
    BOARD_INDEX = BOARD_SIZE - 1
    POSSIBLE_VALUES = range(1, 10)

    def __init__(self, board):
        self.board = board

    def solve(self):
        tempBoard = deepcopy(self.board)
        self.recurse(0, 0)
        self.board, tempBoard = deepcopy(tempBoard), deepcopy(self.board)
        return tempBoard

    def recurse(self, y, x):
        if (y == self.BOARD_INDEX and x == self.BOARD_INDEX):
            return True
        nextX = self.next_coord(x)
        nextY = self.next_coord(y)
        i = 0
        exit = False
        while (i < self.BOARD_SIZE and not exit):
            self.board[y][x] = self.POSSIBLE_VALUES[i]
            if self.is_valid(y, x):
                exit = self.recurse(nextY, nextX)
            i += 1
        return False

    @classmethod
    def next_coord(cls, coord):
        return (coord + 1) % cls.BOARD_SIZE

    def is_valid(self, y, x):
        if self.all_unique(i for i in self.board[y]) and self.all_unique(
                self.board[i][x] for i in range(0, self.BOARD_SIZE)):
            return True
        return False

    @staticmethod
    def all_unique(generator):
        occurences = {}
        for i in generator:
            if i != 0:
                if i in occurences:
                    return False
                occurences.add(i)
        return True


class TestBoard(unittest.TestCase):

    def test_is_valid(self):
        return True

if __name__ == '__main__':
    unittest.main(verbosity=2)

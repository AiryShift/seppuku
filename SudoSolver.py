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
        self.board[y][x] = 0
        return False

    @classmethod
    def next_coord(cls, coord):
        return (coord + 1) % cls.BOARD_SIZE

    def is_valid(self, y, x):
        row = (i for i in self.board[y])
        col = (self.board[i][x] for i in range(0, self.BOARD_SIZE))
        box = (i for i in 0)  # TODO
        for generator in (row, col, box):
            if not self.all_unique(generator):
                return False
        return True

    @staticmethod
    def all_unique(generator):
        occurences = set()
        for i in generator:
            if i != 0:
                if i in occurences:
                    return False
                occurences.add(i)
        return True


class TestBoard(unittest.TestCase):

    def test_is_valid(self):
        return True

    def test_all_unique(self):
        self.assertTrue(SudokuBoard.all_unique(i for i in [
            1, 4, 3, 2, 9, 0, 0]))
        self.assertFalse(SudokuBoard.all_unique(i for i in [
            0, 0, 0, 1, 1]))
        self.assertTrue(SudokuBoard.all_unique(i for i in [
            1, 2, 3, 0, 0, 0]))

if __name__ == '__main__':
    unittest.main(verbosity=2)

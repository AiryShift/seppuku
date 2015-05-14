import unittest
from copy import deepcopy


class SudokuBoard(object):

    """Simulates a sudoku board"""

    BOARD_SIZE = 9
    BOARD_INDEX = BOARD_SIZE - 1
    POSSIBLE_VALUES = range(1, BOARD_SIZE + 1)
    UNDETERMINED_VALUE = 0

    def __init__(self, board):
        self.board = board

    def solve(self):
        tempBoard = deepcopy(self.board)
        self.recurse(0, 0)
        self.board, tempBoard = deepcopy(tempBoard), deepcopy(self.board)
        return tempBoard

    def recurse(self, y, x):
        if (y == self.BOARD_INDEX and x == self.BOARD_INDEX):
            for i in self.POSSIBLE_VALUES:
                self.board[y][x] = i
                if self.is_valid(y, x):
                    return True
            self.board[y][x] = 0
            return False

        nextX = self.next_coord(x)
        nextY = y
        if nextX == 0:  # Step down a row
            nextY = self.next_coord(y)

        exit = False
        if self.board[y][x] == self.UNDETERMINED_VALUE:
            i = 0
            while (i < self.BOARD_SIZE and not exit):
                self.board[y][x] = self.POSSIBLE_VALUES[i]
                if self.is_valid(y, x):
                    exit = self.recurse(nextY, nextX)
                i += 1
            if not exit:
                self.board[y][x] = self.UNDETERMINED_VALUE
        else:
            exit = self.recurse(nextY, nextX)
        return exit

    def is_valid(self, y, x):
        row = (i for i in self.board[y])
        col = (self.board[i][x] for i in range(self.BOARD_SIZE))
        box = (self.board[i][j]
               for i in self.find_box(y) for j in self.find_box(x))
        for generator in (row, col, box):
            if not self.all_unique(generator):
                return False
        return True

    @staticmethod
    def find_box(coord):
        box = coord // 3
        if box == 0:
            return range(0, 3)
        elif box == 1:
            return range(3, 6)
        elif box == 2:
            return range(6, 9)

    @classmethod
    def all_unique(cls, generator):
        occurences = set()
        for value in generator:
            if value != cls.UNDETERMINED_VALUE:
                if value in occurences:
                    return False
                occurences.add(value)
        return True

    @classmethod
    def next_coord(cls, coord):
        return (coord + 1) % cls.BOARD_SIZE


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.board = SudokuBoard([
            [0, 1, 2, 3, 4, 5, 6, 7, 8],
            [0, 0, 0, 0, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 0, 0, 0, 0, 0, 0, 0, 5],
            [0, 0, 0, 0, 0, 0, 0, 0, 4],
            [0, 0, 0, 0, 0, 0, 1, 0, 3],
            [0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 1]])
        self.solveable_1 = SudokuBoard([
            [1, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 5],
            [0, 6, 9, 0, 0, 0, 0, 0, 2],
            [0, 0, 3, 0, 0, 0, 2, 0, 0],
            [4, 9, 8, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 7, 8, 0, 0, 0],
            [7, 0, 0, 0, 4, 0, 6, 0, 0],
            [0, 0, 6, 3, 0, 0, 9, 0, 0],
            [0, 5, 0, 0, 0, 0, 8, 0, 0]])

    def test_is_valid(self):
        self.assertFalse(self.board.is_valid(0, 8))
        self.assertFalse(self.board.is_valid(7, 7))
        self.assertFalse(self.board.is_valid(8, 8))
        self.assertTrue(self.board.is_valid(5, 8))

    def test_next_coord(self):
        self.assertEqual(6, SudokuBoard.next_coord(5))
        self.assertEqual(0, SudokuBoard.next_coord(8))

    def test_all_unique(self):
        self.assertTrue(SudokuBoard.all_unique(i for i in [
            1, 4, 3, 2, 9, 0, 0]))
        self.assertFalse(SudokuBoard.all_unique(i for i in [
            0, 0, 0, 1, 1]))
        self.assertTrue(SudokuBoard.all_unique(i for i in [
            1, 2, 3, 0, 0, 0]))

    def test_solve(self):
        self.assertEqual(self.solveable_1.solve(), [
            [1, 2, 4, 5, 8, 7, 3, 6, 9],
            [3, 8, 7, 9, 2, 6, 1, 4, 5],
            [5, 6, 9, 1, 3, 4, 7, 8, 2],
            [6, 7, 3, 4, 9, 5, 2, 1, 8],
            [4, 9, 8, 2, 1, 3, 5, 7, 6],
            [2, 1, 5, 6, 7, 8, 4, 9, 3],
            [7, 3, 2, 8, 4, 9, 6, 5, 1],
            [8, 4, 6, 3, 5, 1, 9, 2, 7],
            [9, 5, 1, 7, 6, 2, 8, 3, 4]])

if __name__ == '__main__':
    unittest.main(verbosity=2)
    print('All tests passed! You the best!')

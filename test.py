import unittest
import demo
import functions



class MyTestCase(unittest.TestCase):
    def checkWinner(self):
        board = [['x', '.', '.'],
                 ['o', '.', '.'],
                 ['x', 'o', 'o']]
        self.assertEqual('x', functions.getWinner(board))


if __name__ == '__main__':
    unittest.main()

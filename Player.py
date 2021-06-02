class Player:
    def __init__(self, value):
        self.value=value

    def getMove(self, board):
        print("Hello {}, pleas enter of your clever move (row, col)".format(self.value))
        res = input();
        row, col = res.split(',')
        return (int(row), int(col))
def gameOver(board):
    if getWinner(board) is not None:
        return True

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]=='.':
                return False
    return True

def isSameRowOrCol(board, i1, i2, i3):
    return i1==i2 and i2==i3 and i3!='.'


def getWinner(board):
    for i in range(3):
        if isSameRowOrCol(board, board[i][0], board[i][1], board[i][2]):
            return board[i][0]
        if isSameRowOrCol(board, board[0][i], board[1][i], board[2][i]):
            return board[0][i]
    if isSameRowOrCol(board, board[0][0], board[1][1], board[2][2]):
        return board[0][0]
    if isSameRowOrCol(board, board[0][2], board[1][1], board[2][0]):
        return board[0][2]

def isValid(board, nextMove):
    try:
        row, col=nextMove
        if board[row][col]=='.':
            return True
        return False
    except IndexError:
        return False

def play(board, nextMove, game):
    global currentPlayer
    row, col=nextMove
    board[row][col]=game.player().value
    game.nextPlayer()
    printBoard(board)

def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(" ", board[i][j], end=" ")
        print()
    print("------------")



# Python3 program to find the next optimal move for a player
player, opponent = 'x', 'o'

def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '_'):
                return True
    return False


#return 10 if in next step i win, -10 if opponnet win else return 0;
def evaluate(b):
    for row in range(3):
        if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
            if (b[row][0] == player):
                return 10
            elif (b[row][0] == opponent):
                return -10

    for col in range(3):
        if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):
            if (b[0][col] == player):
                return 10
            elif (b[0][col] == opponent):
                return -10

    if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):
        if (b[0][0] == player):
            return 10
        elif (b[0][0] == opponent):
            return -10

    if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):
        if (b[0][2] == player):
            return 10
        elif (b[0][2] == opponent):
            return -10

    return 0

# It considers all the possible ways the game can go and returns the value of the board
def minimax(board, depth, isMax):
    score = evaluate(board)

    if (score == 10):
        return score

    if (score == -10):
        return score

    if (isMovesLeft(board) == False):
        return 0

    # if its my move
    if (isMax):
        best = -1000

        for i in range(3):
            for j in range(3):
                if (board[i][j] == '.'):
                    board[i][j] = player
                    best = max(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '.'
        return best

    # If its opp move
    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if (board[i][j] == '.'):
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = '.'
        return best


# This will return the best possible move for the player
def findBestMove(board):
    bestVal = -1000
    bestMove = (-1, -1)

    # Traverse all cells, evaluate minimax function for
    # all empty cells. And return the cell with optimal
    # value.
    for i in range(3):
        for j in range(3):

            if (board[i][j] == '.'):
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '.'

                if (moveVal > bestVal):
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove


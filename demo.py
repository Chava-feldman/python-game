from Player import Player
from AIPlayer import AIPlayer
from Game import Game
import functions as f

board=[['.','.','.'],['.','.','.'], ['.','.','.']]
game=Game('x', 'o')


if __name__=="__main__":
    while not f.gameOver(board):
        nextMove=game.player().getMove(board)
        if f.isValid(board, nextMove):
            f.play(board, nextMove, game)
        else: print('ERROR')

    winner=f.getWinner(board)
    if winner is not None:
        print("Yay, ", winner, " is the winner")
    else: print("game over")


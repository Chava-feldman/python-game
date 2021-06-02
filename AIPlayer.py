import random
import AIAlgorithm
import Player

class AIPlayer(Player.Player):
    def __init__(self, value):
        super(AIPlayer, self).__init__(value)

    def getMove(self, board):

         return AIAlgorithm.findBestMove(board)


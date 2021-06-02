from Player import Player
from AIPlayer import AIPlayer

class Game:
    def __init__(self, v1, v2):
        self.players=[Player(v1), AIPlayer(v2)]
        self.currentPlayer=0

    def nextPlayer(self):
        self.currentPlayer=(self.currentPlayer+1)%len(self.players)

    def player(self):
        return self.players[self.currentPlayer]



# This is a tic tac tow agent that selects its moves randomly

import Player
import random

class Player_Random(Player):

    def __init__(self, n, t):
        super().__init__(n,t)

    def selectMove(self, b):
        allPrevMoves = b.xMoves+b.oMoves
        while True:
            move = random.randint(0,9)
            if move not in allPrevMoves:
                return move

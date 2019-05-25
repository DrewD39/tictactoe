# This program will handle coordination between players and the board

import Board
import Player

class coordinator(self):

    def __init__(self):
        self.board = Board()
        xPlayer = Player('xTest','x')
        oPlayer = Player('oTest','o')
        self.turn = 'x' # whose turn is it

    def play(self):
        while self.board.checkEnd() == "":
            self.board.show()

            if self.turn == 'x':
                xMove = xPlayer.selectMove(b)
                valid = self.board.makeMove('x', xMove)
                if valid:
                    self.turn = 'o'
                else:
                    print("Illegal move attempted. Select a different move")
            
            elif self.turn == 'o':
                oMove = oPlayer.selectMove(b)
                valid = self.board.makeMove('o', oMove)
                if valid:
                    self.turn = 'x'
                else:
                    print("Illegal move attempted. Select a different move")


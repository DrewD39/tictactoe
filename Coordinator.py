# This program will handle coordination between players and the board

import Board
import Player
import Player_Random

class Coordinator():

    def __init__(self, px, po):
        self.board = Board()
        xPlayer = px
        oPlayer = po
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


        self.board.show()



testCoord = Coordinator(Player_Random('xTest','x'),\
                        Player_Random('oTest','o'))

testCoord.play()

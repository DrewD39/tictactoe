# here layith the board of tic tac toe

class Board:
   
    def __init__(self):
        self.xMoves = []
        self.oMoves = []

    def show(self):
        print('\n')
        for i in range(9):
            if i in self.xMoves:
                print('X', end="")
            elif i in self.oMoves:
                print('O', end="")
            else:
                print(' ', end="")
            
            if (i+1) % 3 != 0:
                print(' | ', end="")
            else:
                print('\n---------\n', end="")


    # allows one player to make a single move on the board
    # returns true in the move was legal, false otherwise
    def makeMove(self, player, place):
        ## I suppose it is not pythonic to type and value check
        ##  in all these functions. Just let it propogate and
        ##  only do explicit checks at the point of entry
        #if player != "x" and player != "o":
        #    raise Exception("Move made by invalid player ({})"\
        #                    .format(player))
        #if place < 0 or place > 8:
        #    raise Exception("Illegal move location selected ({})"
        #                    \.format(place))

        if place in self.xMoves or place in self.oMoves:
            print("Illegal repeated move attempted")
            return False
        
        if player=="x":
            self.xMoves.append(place)
        elif player=="o":
            self.oMoves.append(place)
        return True


    # check if the game is over due to a victory or no moves remaining
    # return x if player x wins, o if player o wins, c if cat's game
    def checkEnd(self):

        # see if 3 Xs in a row
        if \
        all(q in self.xMoves for q in [0,1,2]) or\
        all(q in self.xMoves for q in [3,4,5]) or\
        all(q in self.xMoves for q in [6,7,8]) or\
        all(q in self.xMoves for q in [0,3,6]) or\
        all(q in self.xMoves for q in [1,4,7]) or\
        all(q in self.xMoves for q in [2,5,8]) or\
        all(q in self.xMoves for q in [0,4,8]) or\
        all(q in self.xMoves for q in [2,4,6]):
            return 'x'
        # see if 3 Os in a row
        elif \
        all(q in self.oMoves for q in [0,1,2]) or\
        all(q in self.oMoves for q in [3,4,5]) or\
        all(q in self.oMoves for q in [6,7,8]) or\
        all(q in self.oMoves for q in [0,3,6]) or\
        all(q in self.oMoves for q in [1,4,7]) or\
        all(q in self.oMoves for q in [2,5,8]) or\
        all(q in self.oMoves for q in [0,4,8]) or\
        all(q in self.oMoves for q in [2,4,6]):
            return 'o'
        # see if all spaces have been filled
        if len(xMoves)+len(oMoves)==9:
            return 'c'

        return ''

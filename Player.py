# This program holds the parent class for all types of players


class Player:

    def __init__(self, n, t):
        self.name = n
        self.human = False
        self.team = t # x or o
 

    def selectMove(self, b):
        print("Method needs to be redefined by subclass")


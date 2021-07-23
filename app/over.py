from ball import Ball
from randomiser import Randomiser

class Over:
    def __init__(self, batting_team):
        self.rand = Randomiser()
        self.batting_team = batting_team
        
    def play(self, noEnter = False):
        for i in range(1, 7):
            if noEnter == False:
                input("press 'enter' for next ball")
            ball = Ball()
            ball.print()

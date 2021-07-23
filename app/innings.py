from over import Over
from randomiser import Randomiser
import os
from team import Team
import random

class Innings:
    def __init__(self, bowling_team, batting_team):
        self.rand = Randomiser()
        self.bowling_team = bowling_team
        self.batting_team = batting_team

    def play(self, noEnter = False):
        for i in range(1, 21):
            if noEnter == False:
                input("press 'enter' for next over")
            os.system("cls")
            print("over " + str(i))
            print("bowler - " + random.choice(self.bowling_team.squad).name)
            print("batter - " + self.rand.get_player_name("M"))
            over = Over(self.batting_team)
            over.play(True)
from over import Over
from randomiser import Randomiser
import os

class Innings:
    def __init__(self):
        self.rand = Randomiser()

    def play(self, noEnter = False):
        for i in range(1, 21):
            if noEnter == False:
                input("press 'enter' for next over")
            os.system("cls")
            print("over " + str(i))
            print("bowler - " + self.rand.get_player_name("M"))
            print("batter - " + self.rand.get_player_name("M"))
            over = Over()
            over.play(True)
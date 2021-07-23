from randomiser import Randomiser
from player import Player

class Team:
    def __init__(self, team_name):
        self.rand = Randomiser()
        self.team_name = team_name
        self.squad = []
        for name in range(1,12):
            self.squad.append(Player())
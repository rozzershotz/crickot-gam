from randomiser import Randomiser

class Team:
    def __init__(self, team_name):
        self.rand = Randomiser()
        self.team_name = team_name
        self.squad = []
        for name in range(1,12):
            self.squad.append(self.rand.get_player_name("M"))
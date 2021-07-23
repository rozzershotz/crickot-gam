from randomiser import Randomiser

class Player:
    def __init__(self):
        self.rand = Randomiser()
        self.name = self.rand.get_player_name("M")
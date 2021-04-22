from randomiser import Randomiser

class Ball:
    def __init__(self):
        rand = Randomiser()
        self.type = rand.ball_type()
        if self.type == "W":
            self.dismissal = rand.dismissal_type()

    def print(self):
        print(self.type)
        if self.type == "W":
            print(self.dismissal)
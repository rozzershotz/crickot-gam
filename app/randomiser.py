from hashlib import new
import random

class Randomiser:
    def ball_type(self):
        types = "....111122446W"
        newtypes = list(types)
        edq = random.choice(newtypes)
        return edq
    def dismissal_type(self):
        tipes = ["bowled", "caught", "stumped", "run out", "caught and bowled", "hit wicket"]
        das = random.choice(tipes)
        return das
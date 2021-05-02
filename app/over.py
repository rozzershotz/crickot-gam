from ball import Ball

class Over:
    def play(self, noEnter = False):
        for i in range(1, 7):
            if noEnter == False:
                input("press 'enter' for next ball")
            ball = Ball()
            ball.print()

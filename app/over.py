from ball import Ball

class Over:
    def play(self):
        for i in range(1, 7):
            ball = Ball()
            input("press 'enter' for next ball")
            ball.print()

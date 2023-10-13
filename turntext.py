from turtle import Turtle


class TurnText(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.turn = "Your turn"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 100)
        self.write(self.turn, align="center", font=('Arial', 12, 'bold'))

    def l_point(self):
        self.turn = "Your turn"
        self.update_scoreboard()

    def r_point(self):
        self.turn = "Ai's turn"
        self.update_scoreboard()

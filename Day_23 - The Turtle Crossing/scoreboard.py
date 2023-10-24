from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.score = 1
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-200, y=250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)




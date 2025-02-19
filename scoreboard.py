from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 50, "normal"))
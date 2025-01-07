from turtle import Turtle

FONT = "Courier"
ALIGNMENT = "center"
SIZE = 24

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_player = 0
        self.r_player = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 265)
        self.show_scoreboard()


    def show_scoreboard(self):
        self.clear()
        self.write(f"{self.l_player} : {self.r_player}", align=ALIGNMENT, font=(FONT, SIZE, "normal"))

    def l_player_score(self):
        self.l_player += 1
        self.show_scoreboard()

    def r_player_score(self):
        self.r_player += 1
        self.show_scoreboard()
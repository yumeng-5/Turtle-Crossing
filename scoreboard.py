from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.level = "Level: " + str(self.score)
        self.game_over_text = "GAME OVER"
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-270, 260)
        self.write(self.level, align="left", font=("Courier", 18, "normal"))

    def level_up(self):
        self.score += 1
        self.level = "Level: " + str(self.score)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(self.game_over_text, align="center", font=("Courier", 20, "normal"))
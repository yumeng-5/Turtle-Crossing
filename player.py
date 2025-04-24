from turtle import Turtle

STARTING_POSITION = (0, -270)

class TurtlePlayer(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def up(self):
        new_y = self.ycor() + 15
        self.goto(x=0, y=new_y)

    def reset(self):
        self.goto(STARTING_POSITION)
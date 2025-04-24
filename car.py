from turtle import Turtle
import random

COLORS = ["red", "yellow", "green", "blue", "purple", "brown", "orange", "pink"]

class Car(Turtle):

    def __init__(self, rand_y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.y = rand_y
        self.goto(300, self.y)
        self.x_move = -15

    def move(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())



import random
from turtle import Turtle, Screen
from player import TurtlePlayer
from car import Car
from scoreboard import ScoreBoard
import time

FINISH_LINE_Y = 270

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing")
screen.tracer(0)

cars = []
player = TurtlePlayer()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.up, " Up")

game_is_on = True
counter = 0
move_speed = 0.1

while game_is_on:
    time.sleep(move_speed)
    screen.update()

    counter += 1
    if counter > 5:
        random_y = random.randint(-220, 230)
        car = Car(random_y)
        cars.append(car)
        counter = 0

    # delete the out of screen cars
    # Need improvement it won't clear the drawing
    if len(cars) > 8:
        cars.pop(0)
        cars[0].clear()

    # keep all cars running
    # if player gets too close to the car, the game ends
    for car in cars:
        car.move()
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detect when turtle reaches the finish line
    if player.ycor() > FINISH_LINE_Y:
        player.reset()
        move_speed *= 0.8
        scoreboard.level_up()


screen.exitonclick()

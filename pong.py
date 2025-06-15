from turtle import Screen, Turtle
import random

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("white")
        self.speed(0)
        self.refresh()
        self.y_move = 10
        self.x_move = 10

    def refresh(self):
        self.teleport(0,0)

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_board(self):
        self.x_move *= -1
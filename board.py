import turtle
from turtle import Screen, Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(0.5,3)
        self.setheading(UP)

    def up(self):
        self.goto(self.xcor(),self.ycor()+20)

    def down(self):
        self.goto(self.xcor(),self.ycor()-20)

    def set(self, x, y):
        self.setposition(x,y)
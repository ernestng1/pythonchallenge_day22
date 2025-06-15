from turtle import Screen, Turtle
ALIGNMENT = "center"
FONT = ("Arial", 30, "normal")
UP = 90

class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.score = 0
        self.color("white")
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

class Dash(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.speed("fastest")
        self.teleport(0,-300)
        self.setheading(UP)
        self.width(5)
        for i in range(0,20):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.hideturtle()
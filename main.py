from turtle import Screen, Turtle
from board import Board
from scoreboard import Scoreboard, Dash
from pong import Pong
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard_1 = Scoreboard(-60,250)
scoreboard_2 = Scoreboard(60,250)
dash = Dash()
pong = Pong()


board_1 = Board()
board_1.set(-250,0)
board_2 = Board()
board_2.set(250,0)

screen.listen()
screen.onkey(board_1.up, "w")
screen.onkey(board_1.down, "s")
screen.onkey(board_2.up, "i")
screen.onkey(board_2.down, "k")

game_on=True
while game_on:
    time.sleep(0.05)
    screen.update()
    pong.move()
    if pong.xcor() > 250:
        scoreboard_1.increase_score()
        pong.refresh()
        print("1")
    elif pong.xcor() < -250:
        scoreboard_2.increase_score()
        pong.refresh()
        print("2")
    elif pong.ycor() > 300 or pong.ycor() < -300:
        pong.bounce_wall()
        print("3")
    elif (pong.distance(board_1)< 50 and pong.xcor() < -240) or (pong.distance(board_2) < 50 and pong.xcor() > 240):
        pong.bounce_board()
        print(pong.xcor())
        print("4")

screen.exitonclick()
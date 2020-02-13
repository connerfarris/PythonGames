import turtle
import random

turtle.hideturtle()
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.begin_fill()
turtle.pencolor("blue")
turtle.dot(20)
turtle.forward(100)
turtle.pencolor("purple")
turtle.right(90)
turtle.forward(100)
turtle.pencolor("green")
turtle.right(90)
turtle.forward(100)
turtle.pencolor("yellow")
turtle.right(90)
turtle.forward(100)
turtle.fillcolor("pink")
turtle.end_fill()
turtle.penup()
turtle.goto(-200, 200)
turtle.pencolor("orange")
turtle.dot(200)


def clicked(x, y):
	turtle.pendown()
	turtle.goto(x, y)
	turtle.dot(50)

turtle.onscreenclick(clicked)

turtle.done()

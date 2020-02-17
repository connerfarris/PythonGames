from turtle import *

title("Tic Tac Toe!")
bgcolor("black")
setup(500, 500)
hideturtle()
# speed(10)


def square(size):
	forward(size)
	right(90)
	forward(size)
	right(90)
	forward(size)
	right(90)
	forward(size)
	right(90)


def squareAt(x, y, size):
	pencolor("black")
	up()
	goto(x, y)
	down()
	fillcolor("white")
	begin_fill()
	square(size)
	end_fill()


# def drawXorO()


def drawBoard(x, y):
	for a in range(0, 3):
		for b in range(0, 3):
			squareAt(x, y, 100)
			x = x + 100
		x = -150
		y = y - 100


drawBoard(-150, 150)

done()

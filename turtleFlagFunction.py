import turtle 
turtle.bgcolor('black')

def drawFillRectangle(x, y, length, width, color):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.color(color)
	turtle.begin_fill()
	turtle.forward(width)
	turtle.right(90)
	turtle.forward(length)
	turtle.right(90)
	turtle.forward(width)
	turtle.right(90)
	turtle.forward(length)
	turtle.right(90)
	turtle.end_fill()

def drawStar(x, y, color, length):
	turtle.penup()
	turtle.goto(x,y)
	turtle.setheading(0)
	turtle.pendown()
	turtle.begin_fill()
	turtle.color(color)
	for star in range(0, 5):
		turtle.forward(length)
		turtle.right(144)
	turtle.end_fill()

def drawCircle(x, y, color, radius):
	turtle.penup()
	turtle.goto(x, y)
	turtle.color(color)
	turtle.begin_fill()
	turtle.circle(radius)
	turtle.end_fill()


def drawMoon(x, y, color, radius):
	turtle.penup()
	turtle.goto(x, y)
	turtle.color(color)
	turtle.begin_fill()
	turtle.circle(radius)
	turtle.end_fill()


def pattern(clr1,clr2):
	turtle.width(2)
	turtle.color('black',clr1)
	turtle.begin_fill()
	turtle.circle(150,180)
	turtle.circle(300,180)
	turtle.left(180)
	turtle.circle(-150,180)
	turtle.end_fill()
	turtle.left(90)
	turtle.up()
	turtle.forward(300*0.35)
	turtle.right(90)
	turtle.down()
	turtle.color(clr1,clr2)
	turtle.begin_fill()
	turtle.circle(300*0.20)
	turtle.end_fill()
	turtle.left(90)
	turtle.up()
	turtle.backward(300*0.35)
	turtle.down()
	turtle.left(90)



# FLAG RECTAINGLES
drawFillRectangle(-230, 125, 280, 130, 'red')
drawFillRectangle(-100, 125, 280, 130, 'blue')
drawFillRectangle(32, 125, 280, 130, 'red')
# YINGYANG
pattern('yellow','red')
pattern('yellow','red')
#CIRCLES

drawCircle(-200, -100, 'yellow', 20)
drawMoon(-200, -72, 'yellow', 20)
drawStar(0, 30, 'yellow', 50)

mainloop()

turtle.hideturtle()
turtle.done()
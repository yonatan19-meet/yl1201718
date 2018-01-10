from turtle import *
import random
colormode(255)
import math

class Ball(Turtle):
	def __init__(self, radius, color, x, y, dx, dy):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.x = x
		self.y = y
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
	def move(circle1, circle):
		circle1.x += circle1.dx
		circle1.y += circle1.dy
		circle1.goto(circle1.x, circle1.y)
		circle.x += circle.dx
		circle.y += circle.dy
		circle.goto(circle.x, circle.y)
		

circle = Ball(10, (random.randint(0,255),random.randint(0,255), random.randint(0,255)), 0, 0, 5, 7)
circle1 = Ball(15, (random.randint(0,255),random.randint(0,255), random.randint(0,255)), 100, 100, 3, 4)
def check_col(circle1, circle):
	if (circle.radius + circle1.radius) > math.sqrt((math.pow((circle1.x - circle.x,2))) + math.pow((circle1.y - circle.y,2))):
		print("collision!!!")
		circle.dx *= -1 
		circle.dy *= -1
		circle1.dx *= -1
		circle1.dy *= -1

while 1>0:
	circle.move()
	circle1.move()

check_col()
mainloop()

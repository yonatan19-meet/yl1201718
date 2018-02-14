from turtle import *
import time
import random
import math
colormode(255)

class Ball(Turtle):
	def __init__(self, x,y,dx,dy):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		global r
		r = 10
		self.shapesize(r/10)
		red = random.randint(0,255)
		g = random.randint(0,255)
		b = random.randint(0,255)
		self.color(red,g,b)
	def move(self,screen_width, screen_hight):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		right_side_ball = new_x + r 
		left_side_ball = new_x - r
		bottom_ball = new_y - r
		upper_ball_side = new_y + r
		self.goto(new_x, new_y)
		if bottom_ball < -screen_hight or upper_ball_side > screen_hight:
			self.dy *= -1
		if left_side_ball < -screen_width or right_side_ball > screen_width:
			self.dx *= -1

SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2

Balls = []

def create_ball(event):
	for i in range(NUMBER_OF_BALLS):
		print("hello")
		x = 0
		y = -SCREEN_HEIGHT + 50
		# while dx == 0:
		# 	dx = random.uniform(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
		# while dy == 0:
		# 	dy = random.uniform(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
		m = (event.y - y) / (event.x - x)
		if event.x <= 0:
			dx = -1
		if event.x > 0:
			dx = +1
		dy = m*dx
		new_ball = Ball(x, y, dx, dy, r)
		print(new_ball)
		if new_ball is None:
			print("Ball is none")
		BALLS.append(new_ball)
Ball1 = Ball(0,-50,1,1) 
while True:
	Ball1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
mainloop()
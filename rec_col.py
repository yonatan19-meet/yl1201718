from turtle import *
import random
colormode(255)

class Rectangle(Turtle):
	def __init__(self, h, w, color, x, y, dx, dy):
		Turtle.__init__(self)
		self.pu()
		self.color(color)
		self.h = h
		self.w = w
		self.x = x
		self.y = y
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.goto(x ,self.y+h/2)
		self.goto(self.x+w/2, self.y+h/2)
		self.begin_poly()
		for i in range (2):
			self.left(90)
			self.forward(h)
			self.left(90)
			self.forward(w)
		self.end_poly()
		p = self.get_poly()
		register_shape("poly",p)
		self.pu()
		self.shape("poly")
	def move(self):
		self.x += self.dx
		self.y += self.dy
		self.goto(self.x, self.y)
		
		

a = Rectangle(100, 200, (random.randint(0,255),random.randint(0,255), random.randint(0,255)), 0, 0, 1, 2)
b = Rectangle(150, 200, (random.randint(0,255),random.randint(0,255), random.randint(0,255)), 100, 100, -2, 0.8)
def check_col(a,b):
	if  ((a.ycor()+a.h/2)>(b.ycor()-b.h/2) and
		(a.ycor()-a.h/2)<(b.ycor()+b.h/2) and
		(a.xcor()+a.w/2)>(b.xcor()-b.w/2) and
		(a.xcor()-a.w/2)<(b.xcor()+b.w/2)):
		print("collision!!!")
		a.dx *= -1 
		a.dy *= -1
		b.dx *= -1
		b.dy *= -1

while True:
	b.move()
	a.move()
	check_col(a,b)
mainloop()

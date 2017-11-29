from turtle import *
import random
colormode(255)

class poly(Turtle):
	def __init__(self, lines, size, color, speed, x, y):
		Turtle. __init__(self)
		self.lines = lines
		self.size = size
		self.color(color)
		self.speed(speed)
	#def make_poly(self, lines, size):
		self.x = x
		self.y = y
		self.begin_poly()
		self.pu()
		for i in range(lines):
			self.fd(10)
			self.left(360 / lines)
		self.end_poly()
		p = self.get_poly()
		register_shape("poly",p)
		self.pd()
		self.shape("poly")
		self.shapesize(self.size)
		self.pu()
		self.goto(x,y)
		self.pd()
		while 0<1:
			self.fd(100)
			self.left(360 / lines)
		self.end_poly()


tommy = poly(random.randint(4,10), random.randint(1, 10), (random.randint(0,255),random.randint(0,255), random.randint(0,255)), 1, 10, 10)

mainloop()
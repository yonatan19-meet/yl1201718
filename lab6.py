from turtle import *
import random
colormode(255)

class Square(Turtle):
	def __init__ (self, size, color):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(size)
		self.color(color)

my_square = Square(5,(random.randint(0,255),random.randint(0,255), random.randint(0,255)))
mainloop()
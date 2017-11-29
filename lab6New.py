from turtle import *
import random
colormode(255)

class Rec(Turtle):
	def __init__ (self, height, width, color):
		Turtle.__init__(self)
		self.height = height
		self.width = width
		self.color(color)
	def make_rec(self, height, width):
		self.goto(0, height)
		self.goto(width, height)
		self.goto(width, 0)
		self.goto(0,0)

my_square = Rec(random.randint(5,200), random.randint(5,200),(random.randint(0,255),random.randint(0,255), random.randint(0,255)))
my_square.make_rec(my_square.height, my_square.width)
mainloop()
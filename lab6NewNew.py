from turtle import *
import random
colormode(255)

class hex(Turtle):
	def __init__(self, size, color):
		Turtle. __init__(self)
		self.size = size
		self.color(color)
	def make_hex(self, size):
		self.begin_poly()
		self.pu()
		for i in range(6):
			self.fd(size)
			self.left(60)
		self.end_poly()
		hex = self.get_poly()
		register_shape("hex",hex)
		self.pd()
		self.shape("hex")

tommy = hex(50, (random.randint(0,255),random.randint(0,255), random.randint(0,255)))
tommy.make_hex(145)
mainloop()
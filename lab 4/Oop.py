num = 18
class Animal(object):
	"""docstring for ClassName"""
	def __init__(self, sound, name, age, favourite_colour):
		self.sound = sound
		self.name = name
		self.age = age
		self. favourite_colour = favourite_colour 
	def eat(self,food):
			print("Yummy!! " + self.name + " is eating " + food)
	def description(self):
			print(self.name + " is " + str(self.age) + " years old and loves the colour " + self.favourite_colour)
	def make_sound(self,sound):
			print(num*self.sound)
Butterfly = Animal("Glu Glu ", "Rainbow", 18, "All of them")
Butterfly.eat("Nutella")

Butterfly.description()
Butterfly.make_sound("sound")

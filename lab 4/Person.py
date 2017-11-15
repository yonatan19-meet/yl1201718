class Person(object):
	def __init__(self, name, age, gender, fav_dis_princess, three_items, fav_food):
		self.name = name
		self.age = age
		self.gender = gender
		self.fav_dis_princess = fav_dis_princess
		self.three_items = three_items
		self.fav_food = fav_food
	def EatBreakfast(self, fav_food):
		print(self.name + " is eating " + self.fav_food)


Claire = Person("Claire", "-15", "Girl", "Bell", "Ducktape, Knife, PeanutButter", "Salad")
Claire.EatBreakfast("fav_food")

class Song(object):
	"""docstring for ClassName"""
	def __init__(self, lyrics):
		self.lyrics = lyrics
	def sing_me_a_song(self):
			print(lyrics)

flower_song = Song(["Roses are red",
			"Violets are Blue"
			"I wrote this poem for you."])

flower_song.sing_me_a_song()
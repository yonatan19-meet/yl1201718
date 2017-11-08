import turtle

turtle.speed(1000)
n=360
a=0
colours_list = ["Blue", "Red", "Magenta", "Silver", "Gray", "Green", "Yellow", "Orange", "Purple"]

size = 40
for i in range(n):
	a=a+1
	b=(a%9)
	turtle.left(a)
	turtle.forward(6*size)
	turtle.left(45)
	turtle.forward(2*size)
	turtle.left(90)
	turtle.forward(size)
	turtle.home()
	turtle.color(colours_list[b])
turtle.mainloop()


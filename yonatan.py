from turtle import *
import time
import random
import math
colormode(255)

class Ball(Turtle):
	def __init__(self, x,y,dx,dy,r):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.r = r
		self.shape("circle")
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
		right_side_ball = new_x + self.r
		left_side_ball = new_x - self.r
		bottom_ball = new_y - self.r
		upper_ball_side = new_y + self.r
		self.goto(new_x, new_y)
		if bottom_ball < -screen_hight or upper_ball_side > screen_hight:
			self.dy *= -1
		if left_side_ball < -screen_width or right_side_ball > screen_width:
			self.dx *= -1



tracer(0)
ht()
RUNNING = True
SLEEP = 0.0077
SCREEN_WIDTH = getcanvas().winfo_width()
SCREEN_HEIGHT = getcanvas().winfo_height()

MY_BALL = Ball(0,0,0.5,-0.4,30)
NUMBER_OF_BALLS = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 40
MINIMUM_BALL_DX = -1
MAXIMUM_BALL_DX = 1
MINIMUM_BALL_DY = -1
MAXIMUM_BALL_DY = 1

BALLS = []

for i in range(NUMBER_OF_BALLS):
	print("hello")
	x = random.randint(int(- SCREEN_WIDTH/2 + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH/2 - MAXIMUM_BALL_RADIUS))
	y = random.randint(-SCREEN_HEIGHT/2 + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT/2 - MAXIMUM_BALL_RADIUS)
	dy = random.uniform(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	dx = random.uniform(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
	while dx == 0:
		dx = random.uniform(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
	while dy == 0:
		dy = random.uniform(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
	new_ball = Ball(x, y, dx, dy, r)
	print(new_ball)
	if new_ball is None:
		print("Ball is none")
	BALLS.append(new_ball)


def move_all_balls():
	print(len(BALLS))
	for index in range(len(BALLS)):
		BALLS[index].move(SCREEN_WIDTH/2 ,SCREEN_HEIGHT/2)

# #move_all_balls(BALLS)
# while True:
#   move_all_balls()

def check_col(ball_a, ball_b):
	if ball_a == ball_b:
		return False
	if (ball_a.r + ball_b.r) >= math.sqrt((math.pow((ball_a.xcor() - ball_b.xcor()),2)) + math.pow((ball_a.ycor() - ball_b.ycor()),2)):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if check_col(ball_a, ball_b) == True:
				ra = ball_a.r
				rb = ball_b.r
				x_cor_new = random.randint(int(- SCREEN_WIDTH / 2 + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH/2 - MAXIMUM_BALL_RADIUS))
				y_cor_new = random.randint(-SCREEN_HEIGHT/2 + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT/2 - MAXIMUM_BALL_RADIUS)
				dy_new = random.uniform(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				dx_new = random.uniform(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				r_new = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				while dx_new == 0:
					dx_new = random.uniform(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				while dy_new == 0:
					dy_new = random.uniform(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				red_new = random.randint(0,255)
				g_new = random.randint(0,255)
				b_new = random.randint(0,255)
				color = (red_new,g_new,b_new)
				if ra < rb:
					ball_a.dx = dx_new
					ball_a.dy = dy_new
					ball_a.r = r_new
					#ball_a = (x_cor_new, y_cor_new, dx_new, dy_new, r_new)
					ball_a.goto(x_cor_new, y_cor_new)
					ball_a.shapesize(r_new/10)
					new_rb = ball_b.r + 1
					ball_b.r = new_rb
					ball_b.shapesize(new_rb/10)
				else:
					ball_b.r = r_new
					ball_b.dx = dx_new
					ball_b.dy = dy_new
					#ball_b = (x_cor_new, y_cor_new, dx_new, dy_new, r_new)
					ball_b.goto(x_cor_new, y_cor_new)
					ball_b.shapesize(r_new/10)
					new_ra = ball_a.r + 1
					ball_a.r = new_ra
					ball_a.shapesize(new_ra/10)

def score():
	pu()
	goto(SCREEN_WIDTH*0.25 , SCREEN_HEIGHT*0.45)
	clear()
	write("Your Score: " + str(cur_score), move = False, align = "left", font = ("Ariel", 14, "normal"))

def Harder():
	global MAXIMUM_BALL_DX
	global MAXIMUM_BALL_DY
	global cur_score
	global MAXIMUM_BALL_RADIUS
	global NUMBER_OF_BALLS
	global new_ball
	if cur_score > 10:
		MAXIMUM_BALL_DY += 0.05
		MAXIMUM_BALL_DX += 0.05
		MAXIMUM_BALL_RADIUS += 1
		NUMBER_OF_BALLS += 0.1
	if 100 > cur_score > 60:
		x = random.randint(int(- SCREEN_WIDTH/2 + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH/2 - MAXIMUM_BALL_RADIUS))
		y = random.randint(-SCREEN_HEIGHT/2 + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT/2 - MAXIMUM_BALL_RADIUS)
		dy = random.uniform(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
		dx = random.uniform(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
		r = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
		while dx == 0:
			dx = random.uniform(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
		while dy == 0:
			dy = random.uniform(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
		new_ball = Ball(x, y, dx, dy, r)
		print(new_ball)
		if new_ball is None:
			print("Ball is none")
	BALLS.append(new_ball)
	if cur_score > 100:
		NUMBER_OF_BALLS = 8

cur_score = 0
def my_ball_collision():
	global cur_score
	for ball_x in BALLS:
		if check_col(MY_BALL,ball_x) == True:
			if MY_BALL.r < ball_x.r:
				return False
				write("You Lost!", align = "center", )
				sleep(3)
			if MY_BALL.r > ball_x.r:
				x_cor_new = random.randint(int(- SCREEN_WIDTH / 2 + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH/2 - MAXIMUM_BALL_RADIUS))
				y_cor_new = random.randint(-SCREEN_HEIGHT/2 + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT/2 - MAXIMUM_BALL_RADIUS)
				dy_new = random.uniform(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				while dy_new == 0:
					dy_new = random.uniform(MINIMUM_BALL_DY , MAXIMUM_BALL_DY)
				dx_new = random.uniform(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				while dx_new == 0:
						dx_new = random.uniform(MINIMUM_BALL_DX , MAXIMUM_BALL_DX)
				r_new = random.randint(MINIMUM_BALL_RADIUS , MAXIMUM_BALL_RADIUS)
				ball_x.goto(x_cor_new,y_cor_new)
				ball_x.dx = dx_new
				ball_x.dy = dy_new
				ball_x.r = r_new
				ball_x.shapesize(r_new/10)
				MY_BALL.r += 1
				MY_BALL.shapesize(MY_BALL.r/10)
				cur_score += 1
				score()
				Harder()
	return True

def movearound(event):
	MY_BALL.goto(event/.x - SCREEN_WIDTH/2 , SCREEN_HEIGHT/2 - event.y)
getcanvas().bind("<Motion>", movearound)
listen()





while RUNNING == True:
	if SCREEN_WIDTH != getcanvas().winfo_width():
		SCREEN_WIDTH = getcanvas().winfo_width()
	if SCREEN_HEIGHT != getcanvas().winfo_height():
		SCREEN_HEIGHT = getcanvas().winfo_height()
	move_all_balls()
	check_all_balls_collision()
	# my_ball_collision()
	# if my_ball_collision() == False:
	# 	RUNNING = False
	# if my_ball_collision() == True:
	# 	RUNNING = True
	RUNNING = my_ball_collision()
	getscreen().update()
	time.sleep(SLEEP)

mainloop()
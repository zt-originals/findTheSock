# Import pygame and initialize
import random
import pygame
pygame.init()
# Definitions and global variables
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("The Finder of Socks")
clock = pygame.time.Clock()
x = 50
y = 425
width = 50
height = 50
vel = 25
isJump = False
jumpCount = 10
# COLORS #
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
magenta = (255,0,255)
grey = (100,100,100)
colors = [white, red, green, blue, magenta]
# Classes, I've only started learning about classes so most of this is experimental, ha!
# Player class
class player(object):
	def __init__(self, x, y, width, height, color):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.isJump = False
		self.jumpCount = 10
		self.hitbox = (self.x, self.y, 50, 50)
		self.color = grey
	def draw(self,win):
		self.hitbox = (self.x, self.y, 50, 50)
		if keys[pygame.K_DOWN]:
			self.hitbox = (self.x - 12.5, self.y + 25, 75, 25)
		#draw mom to the screen
		pygame.draw.rect(win, grey, self.hitbox,0)
# Sock class (item to be collected)
class sock(object):
	def __init__(self, x, y, width, height, color):
		self.x = random.randint(25,350)
		self.y = y + 20
		self.width = width
		self.height = height
		self.vel = 5
		self.doesHave = False
		self.hitbox = (self.x, self.y, 20, 20)
		self.color = color
		self.jumpCount = 10
		self.isJump = False
	def draw(self,win):
		pygame.draw.rect(win, self.color, self.hitbox,0)
		if self.doesHave == True:
			self.hitbox = (mom.hitbox[0] - 25, mom.hitbox[1] - 15, 20, 20)
			
		if keys[pygame.K_LCTRL]:
			if self.isJump == False:
				self.doesHave = False
				if self.jumpCount >= -10:
					self.neg = 1
				if self.jumpCount < 0:
					self.neg = -1
					# this is a cool way to make jumps look more realistic with MATHS!!!
					self.y -= (self.jumpCount ** 2) * 0.25 * self.neg
					self.jumpCount -= 1
				else:
					self.isJump = False
					self.jumpCount = 10

			pygame.display.update()
# Refreshes our screen so player can see updated changes like position
def redrawGameWindow():
	global walkCount
	win.fill(black)
	mom.draw(win)
	sock.draw(sockA,win)
	sock.draw(sockB,win)
	sock.draw(sockC,win)
	sock.draw(sockD,win)
	pygame.display.update()
xDestinations = [(10, 115), (135, 240), (260, 365), (385, 490)]
xList = random.sample(xDestinations,4)
colorList = random.sample(colors,4)
sockA = sock(xList[0], 450, 20, 20, colorList[0])
sockB = sock(xList[1], 450, 20, 20, colorList[1])
sockC = sock(xList[2], 450, 20, 20, colorList[2])
sockD = sock(xList[3], 450, 20, 20, colorList[3])
sockList = [sockA, sockB, sockC, sockD]
mom = player(450, 450, 50, 50, grey)
run = True
# sockCount = 0
sockList = []
# Main Loop
while run:
	# Set a rate of time for our world
	clock.tick(30)
	# Moving without the sock
	if sockA.doesHave == False:
		if mom.hitbox[1] < sockA.hitbox[1] + sockA.hitbox[3] and mom.hitbox[1] + mom.hitbox[3] > sockA.hitbox[1]:
				if mom.hitbox[0] + mom.hitbox[2] > sockA.hitbox[0] and mom.hitbox[0] < sockA.hitbox[0] + sockA.hitbox[2]:
					sockA.doesHave = True
					sockA.draw(win)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	# movements and interactions
	keys = pygame.key.get_pressed()
	# if mom does not have the sock
	if sockA.doesHave == False:
		# then she moves when we use the controls
		if keys[pygame.K_LEFT] and mom.x > mom.vel:
			mom.x -= mom.vel
		elif keys[pygame.K_RIGHT] and mom.x < 500 - mom.width - mom.vel:
			mom.x += mom.vel
		# if mom is not jumping, she can jump
		if not(mom.isJump):
			if keys[pygame.K_SPACE]:
				mom.isJump = True
		else:
			if mom.jumpCount >= -10:
				mom.neg = 1
				if mom.jumpCount < 0:
					mom.neg = -1
				# this is a cool way to make jumps look more realistic with MATHS!!!
				mom.y -= (mom.jumpCount ** 2) * 0.25 * mom.neg
				mom.jumpCount -= 1
			else:
				mom.isJump = False
				mom.jumpCount = 10
	# if mom DOES have the sock
	elif sockA.doesHave == True:
		# mom carries the sock around
		if keys[pygame.K_LEFT] and mom.x > mom.vel:
			mom.x -= mom.vel
			sockA.x -= sockA.vel
		elif keys[pygame.K_RIGHT] and mom.x < 500 - mom.width - mom.vel:
			mom.x += mom.vel
			sockA.x += sockA.vel
		# elif keys[pygame.K_LCTRL]:
		# 	sockA.doesHave = False
		# 	sockA.neg = -1
		# 	sockA.jumpCount = 2
		# 	sockA.y -= (sockA.jumpCount ** 2) * 0.25 * sockA.neg
		# and she even jumps with the sock
		if not(mom.isJump):
			if keys[pygame.K_SPACE]:
				mom.isJump = True
		else:
			if mom.jumpCount >= -10:
				mom.neg = 1
				if mom.jumpCount < 0:
					mom.neg = -1
				mom.y -= (mom.jumpCount ** 2) * 0.25 * mom.neg
				mom.jumpCount -= 1
			else:
				mom.isJump = False
				mom.jumpCount = 10
	redrawGameWindow()
# I've just been playing with ASCII art hehe
print("""
*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*
*.*.==================*.*.==================*.*.
.*.*==================.*.*==================.*.*
*.*.*.*.*.*.*///////*.*.*.*.*.*.*||||.*.*.*.*.*.
.*.*.*///////*.*.*.*.*.*.*.*.*.*.||||*.*.*.*.*.*
*.*.==================*.*.*.*.*.*||||.*.*.*.*.*.
.*.*==================.*.*.*.*.*.||||*.*games*.*
*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*
	""")
# Shut her down!
pygame.quit()

# Import pygame and initialize
import random
import time
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
font1 = pygame.font.SysFont('comicsans', 100)
font2 = pygame.font.SysFont('comicsans', 25)
music = pygame.mixer.music.load('HappyJumping.mp3')
pygame.mixer.music.play(-1)
run = False
end_it = False
# COLORS #
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
magenta = (255,0,255)
cyan = (0,255,255)
yellow = (255,255,0)
grey = (100,100,100)
colors = [white, red, green, blue]
desiredColor = random.choice(colors)
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
		self.own = False
	def draw(self,win):
		self.hitbox = (self.x, self.y, 50, 50)
		keys = pygame.key.get_pressed()
		if keys[pygame.K_DOWN]:
			self.hitbox = (self.x - 12.5, self.y + 25, 75, 25)
		#draw mom to the screen
		pygame.draw.rect(win, grey, self.hitbox,0)
class child(object):
	def __init__(self, x, y, width, height, color):
		self.x = 475
		self.y = 5
		self.width = 40
		self.height = 40
		self.color = desiredColor
		self.hitbox = (self.x, self.y, self.width, self.height)
	def draw(self,win):
		pygame.draw.rect(win, self.color, self.hitbox,0)
# Sock class (item to be collected)
class sock(object):
	def __init__(self, x, y, width, height, color,doesHave):
		self.x = random.randint(25,350)
		self.y = 480
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
		keys = pygame.key.get_pressed()
		# if mom DOES have the sock
		if self.doesHave == True:
			if self.color == childA.color:
				font1 = pygame.font.SysFont('comicsans', 100)
				textA = font1.render('You Win!', 1, (255,0,0))
				win.blit(textA, (500/2 - (textA.get_width()/2),200))
				pygame.display.update()
				time.sleep(3)
				run = False
				end_it = True
				pygame.display.quit()
				pygame.quit()
			self.hitbox = (mom.hitbox[0] - 25, mom.hitbox[1] - 25, 20, 20)
			if keys[pygame.K_LCTRL]:
				if self.isJump == False:
					self.doesHave = False
					mom.own = False
					self.y = 480
					self.x = mom.x - 20
					self.hitbox = (self.x, self.y, 20, 20)
					self.neg = 1
					if mom.jumpCount >= -10:
						mom.neg = 1
					if mom.jumpCount < 0:
						mom.neg = -1
					self.x -= 15
					self.jumpCount -= -1
		# mom carries the sock around
			if keys[pygame.K_LEFT] and mom.x > mom.vel:
				mom.x -= mom.vel
				self.x -= self.vel
			elif keys[pygame.K_RIGHT] and mom.x < 500 - mom.width - mom.vel:
				mom.x += mom.vel
				self.x += self.vel
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
		elif self.doesHave == False:
			self.x = self.x
			self.y = 480
			if mom.hitbox[1] < self.hitbox[1] + self.hitbox[3] and mom.hitbox[1] + mom.hitbox[3] > self.hitbox[1]:
					if mom.hitbox[0] + mom.hitbox[2] > self.hitbox[0] and mom.hitbox[0] < self.hitbox[0] + self.hitbox[2]:
						if mom.own == False:
							self.doesHave = True
							mom.own = True
			if keys[pygame.K_LEFT] and mom.x > mom.vel:
				mom.x -= mom.vel
			elif keys[pygame.K_RIGHT] and mom.x < 500 - mom.width - mom.vel:
				mom.x += mom.vel
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
# Refreshes our screen so player can see updated changes like position
def redrawGameWindow():
	global walkCount
	global end_it
	global run
	# Start Screen
	if end_it == False:
		startScreen = win.fill(magenta)
		font1 = pygame.font.SysFont('comicsans', 18)
		textA = font1.render("Mom needs to find socks to match baby's outfit! Press RETURN to begin. ", 1, (255,255,255))
		win.blit(textA, (500/2 - (textA.get_width()/2),200))
		pygame.display.update()
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RETURN]:
			end_it = True
			run = True
	# Main Game
	elif run == True:
		win.fill(black)
		mom.draw(win)
		sock.draw(sockA,win)
		sock.draw(sockB,win)
		sock.draw(sockC,win)
		sock.draw(sockD,win)
		child.draw(childA,win)
		pygame.display.update()	
xDestinations = [(10, 115), (135, 240), (260, 365), (385, 490)]
xList = random.sample(xDestinations,4)
colorList = random.sample(colors,4)
sockA = sock(xList[0], 480, 20, 20, colorList[0],False)
sockB = sock(xList[1], 480, 20, 20, colorList[1],False)
sockC = sock(xList[2], 480, 20, 20, colorList[2],False)
sockD = sock(xList[3], 480, 20, 20, colorList[3],False)
#childA_hitbox = (475, 5, 20, 20)
childA = child(475,5,40,40,desiredColor)
sockList = [sockA, sockB, sockC, sockD]
mom = player(450, 450, 50, 50, grey)
run = True
# Main Loop
while run:
	# Set a rate of time for our world
	clock.tick(15)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
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
pygame.display.quit()
pygame.quit()

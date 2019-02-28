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

# Classes, I've only started learning about classes so most of this is experimental, ha!
# Player class
class player(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.isJump = False
		self.jumpCount = 10
		self.hitbox = (self.x, self.y, 50, 50)
	def draw(self,win):
		self.hitbox = (self.x, self.y, 50, 50)
		#draw mom to the screen
		pygame.draw.rect(win, (255,0,0), self.hitbox,2)

# Sock class (item to be collected)
class sock(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.vel = 5
		self.doesHave = False
		# A) boundaries of the sock
		self.hitbox = (random.randint(25,350), self.y, 20, 20)
		# B) random placement of sock when spawned
		self.hitboxB = (random.randint(25,350), self.y, 20, 20)
		self.hitboxC = (random.randint(25,350), self.y, 20, 20)
		# self.hitboxD = (random.randint(25,350), self.y, 20, 20)
	def draw(self,win):
		if self.doesHave == False:
			self.hitbox = (self.x, self.y, 20, 20)
			# B) - case in point
			pygame.draw.rect(win, (100,100,100), self.hitbox,0)
			pygame.draw.rect(win, (0,0,255), self.hitboxB,0)
			if self.hitboxB[1] < self.hitbox[1] + self.hitbox[3] and self.hitboxB[1] + self.hitboxB[3] > self.hitbox[1]:
				return True

			pygame.draw.rect(win, (255,0,255), self.hitboxC,0)
			if self.hitboxC[1] < self.hitboxB[1] + self.hitboxB[3] and self.hitboxC[1] + self.hitboxC[3] > self.hitboxB[1]:
				if self.hitboxC[1] < self.hitbox[1] + self.hitbox[3] and self.hitboxC[1] + self.hitboxC[3] > self.hitbox[1]:
					return True	

			# pygame.draw.rect(win, (0,0,255), self.hitboxC,2)
			# pygame.draw.rect(win, (0,0,255), self.hitboxD,2)
		elif self.doesHave == True:
			self.hitbox = ((mom.hitbox[0] + 5, mom.hitbox[1] + 5, 20, 20))
			self.hitboxB = ((sock.hitboxB[0], sock.hitboxB[1], 20, 20))
			# A) - case in point
			pygame.draw.rect(win, (100,100,100), self.hitbox,1)
			pygame.draw.rect(win, (0,0,255), self.hitboxB,0)

# Refreshes our screen so player can see updated changes like position
def redrawGameWindow():
	global walkCount
	win.fill((0,0,0))
	mom.draw(win)
	sock.draw(win)
	pygame.display.update()

# Lists?
mom = player(450, 450, 50, 50)
sock = sock(50, 450, 20, 20)
run = True
sockCount = 0
sockList = []

# Main Loop
while run:
	# Set a rate of time for our world
	clock.tick(30)
	# Moving without the sock
	if sock.doesHave == False:
		if mom.hitbox[1] < sock.hitbox[1] + sock.hitbox[3] and mom.hitbox[1] + mom.hitbox[3] > sock.hitbox[1]:
				if mom.hitbox[0] + mom.hitbox[2] > sock.hitbox[0] and mom.hitbox[0] < sock.hitbox[0] + sock.hitbox[2]:
					sock.doesHave = True
					sock.draw(win)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# movements and interactions
	keys = pygame.key.get_pressed()
	# if mom does not have the sock
	if sock.doesHave == False:
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
	elif sock.doesHave == True:
		# mom carries the sock around
		if keys[pygame.K_LEFT] and mom.x > mom.vel:
			mom.x -= mom.vel
			sock.x -= sock.vel
		elif keys[pygame.K_RIGHT] and mom.x < 500 - mom.width - mom.vel:
			mom.x += mom.vel
			sock.x += sock.vel
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
	*.*.*.*.*.*.*/////////*.*.*.*.*.*||||.*.*.*.*.*.
	.*.*/////////*.*.*.*.*.*.*.*.*.*.||||*.*.*.*.*.*
	*.*.==================*.*.*.*.*.*||||.*.*.*.*.*.
	.*.*==================.*.*.*.*.*.||||*.*games*.*
	*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.
	.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*
	""")
# Shut her down!
pygame.quit()

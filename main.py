import pygame
import os

os.system('cls')

pygame.init()

win = pygame.display.set_mode((600, 300))
pygame.display.set_caption("The cube")

FPS = 60
clock = pygame.time.Clock()

x_player = 10
y_player = 280
width_player = 10
height_player = 10
speed_player = 3

isJump = False
jampCount = 10

z = False

def drawWindow():
	pygame.display.update()

	win.fill((0,0,0))

	pygame.draw.rect(win, (255,255,255), (x_player, y_player, width_player, height_player))

		#Линии по краям
	pygame.draw.line(win, (255,255,255), (5, 5), (595, 5))
	pygame.draw.line(win, (255,255,255), (5, 5), (5, 295))
	pygame.draw.line(win, (255,255,255), (5, 295), (595, 295))
	pygame.draw.line(win, (255,255,255), (595, 295), (595, 5))

run = True
while run:
	#Контроль фпс
	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()


	keys = pygame.key.get_pressed()

	if keys[pygame.K_a] and x_player > 10:
		x_player -= speed_player
	if keys[pygame.K_d] and x_player < 600 - width_player - 10:
		x_player += speed_player
	if not(isJump):
		if keys[pygame.K_z]:
			z = True
			if keys[pygame.K_w] and y_player > 10:
				y_player -= speed_player
			if keys[pygame.K_s] and y_player < 300 - height_player - 10:
				y_player += speed_player
		if keys[pygame.K_SPACE]:
			isJump = True
		if z == False:
			y_player = 280
		if not(keys[pygame.K_z]):
			z = False


	else:
		if jampCount >= -10:
			if jampCount < 0:
				y_player += (jampCount ** 2) / 6
			else:
				y_player -= (jampCount ** 2) / 6
			jampCount -= 1
		else:
			isJump = False
			jampCount = 10



	drawWindow()

pygame.quit()


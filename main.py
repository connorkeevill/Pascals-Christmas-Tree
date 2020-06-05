import pygame
import sys
import colours
from pygame.locals import *
from tree.pascalTree import pascalTree
from snow.snowStorm import snowStorm

pygame.init()

windowWidth = 700
windowHeight = 600

FPS = 30
clock = pygame.time.Clock()

window = pygame.display.set_mode((windowWidth, windowHeight))

snowStorm = snowStorm()

tree = pascalTree(125, 4)

while True:
	window.fill(colours.black)

	snowStorm.fall()
	snowStorm.draw(window)

	tree.draw(window, 20)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.flip()
	clock.tick(FPS)


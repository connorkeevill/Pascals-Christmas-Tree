import pygame
import sys
from pygame.locals import *
from tree.pascalTree import pascalTree

pygame.init()

windowWidth = 400
windowHeight = 400

FPS = 3
clock = pygame.time.Clock()

window = pygame.display.set_mode((windowWidth, windowHeight))

tree = pascalTree(120, 2)

while True:

    tree.draw(window, 20)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)


import pygame
import sys
from pygame.locals import *
from tree.pascalTree import pascalTree
from tree.christmasTree import christmasTree

pygame.init()

windowWidth = 400
windowHeight = 400

FPS = 60
clock = pygame.time.Clock()

window = pygame.display.set_mode((windowWidth, windowHeight))

tree = pascalTree(20)

christmas = christmasTree(tree, window)

while True:
    christmas.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)


import pygame
import sys
from pygame.locals import *
from pascalTree import pascalTree
from christmasTree import christmasTree

pygame.init()

windowWidth = 400
windowHeight = 400

window = pygame.display.set_mode((windowWidth, windowHeight))

tree = pascalTree(20)

treeBranches = tree.getBranches()
christmas = christmasTree(tree, window)

while True:
    christmas.draw()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


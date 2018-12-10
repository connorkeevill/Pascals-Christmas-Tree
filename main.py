import pygame
from pygame.locals import *
from pascalTree import pascalTree

pygame.init()

windowWidth = 700
windowHeight = 700

window = pygame.display.set_mode((windowWidth, windowHeight))

tree = pascalTree(70)

treeBranches = tree.getTree()

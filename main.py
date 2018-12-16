import pygame
import sys
from pygame.locals import *
from tree.pascalTree import pascalTree

pygame.init()

windowWidth = 400
windowHeight = 400

FPS = 60
clock = pygame.time.Clock()

window = pygame.display.set_mode((windowWidth, windowHeight))

tree = pascalTree(20)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(FPS)


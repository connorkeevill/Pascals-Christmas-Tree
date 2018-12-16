import pygame
import sys
from pygame.locals import *
from tree.pascalTree import pascalTree

pygame.init()

windowWidth = 700
windowHeight = 600

FPS = 3
clock = pygame.time.Clock()

window = pygame.display.set_mode((windowWidth, windowHeight))

tree = pascalTree(125, 4)

while True:
    tree.draw(window, 20)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(FPS)


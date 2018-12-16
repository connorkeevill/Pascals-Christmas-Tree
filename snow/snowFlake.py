import colours
import pygame
import math

class snowFlake():
    def __init__(self, size, fallAxis):
        self.size = size

        self.fallAxis = fallAxis
        self.Xpos = fallAxis

        self.Yvelocity = 0
        self.Ypos = -size

        self.time = 0

    def draw(self, display):
        pygame.draw.circle(display, colours.white, (self.Xpos, self.Ypos), self.size)

    def fall(self):
        self.time += 1

        self.Xpos = int((10 * math.sin(self.time / 4)) + self.fallAxis)

        if self.Yvelocity < 5:
            self.Yvelocity += self.time

        self.Ypos += self.Yvelocity



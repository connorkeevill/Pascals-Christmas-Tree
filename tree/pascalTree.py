from tree.pascalLeaf import pascalLeaf
import pygame
import colours
import threading
import random
import time

class pascalTree:
    def __init__(self, height, leafSize):
        self.tree = self.buildTree(height)
        self.treeHeight = height

        self.leafSize = leafSize

        primeColourChanger = threading.Thread(target=self.flashPrimes)
        primeColourChanger.setDaemon(True)
        primeColourChanger.start()

    def buildTree(self, height):
        tree = []

        for layer in range(height):
            treeLayer = []

            for leaf in range(layer + 1):
                treeLayer.append(pascalLeaf(layer, leaf))

            tree.append(treeLayer)

        return tree

    def draw(self, display, height):
        Xoffset = self.leafSize // 2
        displayMid = display.get_width() // 2
        Xpos = displayMid

        Ypos = height

        for branch in self.tree:
            Xpos -= Xoffset
            Ypos += self.leafSize

            leafNumber = 0
            for leaf in branch:
                pygame.draw.rect(display, leaf.colour, (Xpos + self.leafSize * leafNumber, Ypos, self.leafSize, self.leafSize))
                leafNumber += 1

        baseWidth = 0.2 * (self.treeHeight * self.leafSize)
        pygame.draw.rect(display, colours.baseBrown, (displayMid - (baseWidth / 2), height + ((self.treeHeight + 1) * self.leafSize), baseWidth, baseWidth / 2))

    def flashPrimes(self):
        while True:
            for branch in self.tree:
                for leaf in branch:
                    if leaf.isPrime:
                        leaf.colour = random.choice(colours.baubleColours)
            time.sleep(1 / 4)
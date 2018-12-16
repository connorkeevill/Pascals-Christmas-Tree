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

        shadeChange = threading.Thread(target=self.changeTreeShading)
        shadeChange.setDaemon(True)
        shadeChange.start()

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

    def changeTreeShading(self):
        upperLimit = 1.8
        lowerLimit = 1.39

        increasing = True

        baseValue = 1.4
        adjustmentValue = 0.003

        while True:
            if baseValue < lowerLimit:
                increasing = True
            elif baseValue > upperLimit:
                increasing = False

            if increasing: baseValue += adjustmentValue
            else: baseValue -= adjustmentValue

            for branch in self.tree:
                for leaf in branch:
                    leaf.calculateColour(leaf.pascalValue, baseValue)

            time.sleep(1/60)
import pygame


class christmasTree():
    def __init__(self, pascalTree, display):
        self.pascalTree = pascalTree
        self.display = display

    def draw(self):
        dispMid = self.display.get_width() / 2

        branchCount = 1
        yOffset = -1

        for branch in self.pascalTree.getBranches():
            xOffset = -5 * branchCount
            branchCount += 1

            yOffset += 10

            leafCount = 0

            for leaf in branch.leaves:
                leafOffset = 10 * leafCount
                leafCount += 1
                pygame.draw.rect(self.display, (0, 255, 0), (dispMid + xOffset + leafOffset, 10 + yOffset, 10, 10))

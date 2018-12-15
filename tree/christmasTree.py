import pygame

# | christmasTree()
# |--------------------------------------------------
# | The object for the drawn tree. Has a pascalTree,
# | but also a method that draws it to the screen
# |--------------------------------------------
class christmasTree():
    def __init__(self, pascalTree, display):
        self.pascalTree = pascalTree
        self.display = display

        self.midOfDisplay = display.get_width() // 2

    def draw(self):
        offset = 0
        yPos = 20
        for branch in self.pascalTree.branches:
            offset += 5
            for leaf in range(len(branch.leaves)):
                branchLeaf = branch.leaves[leaf]
                pygame.draw.rect(self.display, branchLeaf.colour, (self.midOfDisplay - offset + branchLeaf.Xoffset, yPos + branchLeaf.Yoffset, branchLeaf.size, branchLeaf.size))


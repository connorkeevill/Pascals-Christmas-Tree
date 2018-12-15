from tree.pascalBranch import pascalBranch

class pascalTree:
    def __init__(self, height):
        self.branches = []
        self.buildTree(height)

    def buildTree(self, height):

        treeTop = pascalBranch()
        self.branches.append(treeTop)

        for branch in range(1, height):
            self.branches.append(pascalBranch(self.branches[branch - 1]))

    def getBranches(self):
        return self.branches


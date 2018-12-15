from tree.pascalLeaf import pascalLeaf

# | pascalBranch()
# |------------------------------------------------------
# | Class to represent each row or branch of the tree.
# |------------------------------------------------
class pascalBranch:
    def __init__(self, parentBranch=None):
        self.leaves = []
        self.branchNumber = 0
        self.leafSize = 10

        # | The first two if statements generate the first two branches
        if parentBranch is None:
            self.leaves = [pascalLeaf(0, 0, 1, self.leafSize)]
            self.branchNumber = 0
        elif len(parentBranch.leaves) == 1:
            self.leaves = [pascalLeaf(1, 0, 1, self.leafSize), pascalLeaf(1, 1, 1, self.leafSize)]
            self.branchNumber = 1
        else:
            self.generateBranch(parentBranch)
            self.branchNumber = parentBranch.branchNumber + 1


    def generateBranch(self, parentBranch):
        for count in range(len(parentBranch.leaves) + 1):
            if count == 0 or count == (len(parentBranch.leaves)):
                self.leaves.append(pascalLeaf(parentBranch.branchNumber, count, 1, self.leafSize))
            else:
                leafVal = parentBranch.leaves[count - 1].pascalValue + parentBranch.leaves[count].pascalValue
                leaf = pascalLeaf(parentBranch.branchNumber + 1, count, leafVal, self.leafSize)
                self.leaves.append(leaf)

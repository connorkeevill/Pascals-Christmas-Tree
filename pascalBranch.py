

class pascalBranch:
    def __init__(self, parent=None):
        self.leaves = []

        if parent is None:
            self.leaves = [1]
        elif parent.leaves == [1]:
            self.leaves = [1, 1]
        else:
            self.generateLayer(parent)

    def generateLayer(self, parent):
        for item in range(len(parent.leaves) + 1):
            if item == 0 or item == len(parent.leaves):
                self.leaves.append(1)
            else:
                leaf = parent.leaves[item - 1] + parent.leaves[item]
                self.leaves.append(leaf)
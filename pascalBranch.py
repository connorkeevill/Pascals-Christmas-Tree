

class pascalBranch:
    def __init__(self, parentBranch=None):
        self.leaves = []

        # | The first two if statements generate the first two branches
        if parentBranch is None:
            self.leaves = [1]
        elif parentBranch.leaves == [1]:
            self.leaves = [1, 1]
        else:
            self.generateBranch(parentBranch)

    def generateBranch(self, parentBranch):
        for number in range(len(parentBranch.leaves) + 1):
            # | If we are looking at the first or last item of the parent branch
            if number == 0 or number == len(parentBranch.leaves):
                self.leaves.append(1)
            else:
                leaf = parentBranch.leaves[number - 1] + parentBranch.leaves[number]
                self.leaves.append(leaf)
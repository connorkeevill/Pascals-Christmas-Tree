from tree.pascalLeaf import pascalLeaf

class pascalTree:
    def __init__(self, height):
        self.tree = self.buildTree(height)

    def buildTree(self, height):
        tree = []

        for layer in range(height):
            treeLayer = []

            for leaf in range(layer + 1):
                treeLayer.append(pascalLeaf(layer, leaf))

            tree.append(treeLayer)

        return tree


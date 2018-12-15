
# | pascalLeaf()
# |--------------------------------------------
# | The object that will be used to represent
# | each node of a Pascal Christmas tree.
# |----------------------------------
class pascalLeaf():
    def __init__(self, branchNumber, leafNumber, pascalValue, size):
        self.branchNumber = branchNumber
        self.leafNumber = leafNumber
        self.pascalValue = pascalValue
        self.size = size

        self.Yoffset = size * branchNumber
        self.Xoffset = size * leafNumber


        shadeValue = 0

        if pascalValue > 1:
            shadeValue = pascalValue // branchNumber

        if shadeValue > 225:
            shadeValue = 225

        green = 255 - shadeValue
        self.colour = (0, green, 0)

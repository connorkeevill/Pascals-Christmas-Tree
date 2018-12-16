import math

# | pascalLeaf()
# |--------------------------------------------
# | The object that will be used to represent
# | each node of a Pascal Christmas tree.
# |----------------------------------
class pascalLeaf():
    def __init__(self, branchNumber, leafNumber):
        self.pascalValue = self.nCr(branchNumber, leafNumber)

        shadeValue = 0

        if self.pascalValue > 1:
            shadeValue = self.pascalValue // branchNumber

        if shadeValue > 225:
            shadeValue = 225

        green = 255 - shadeValue
        self.colour = (0, green, 0)

    # | nCr()
    # |-----------------------------------------------------------
    # | Calculates the value of a pascal's triangle node with
    # | the formula for the binomial coefficient 'nCr'.
    # |-------------------------------------------
    def nCr(self, n, r):
        value = math.factorial(n) / (math.factorial(r) * (math.factorial(n - r)))
        return value

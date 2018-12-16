import math

# | pascalLeaf()
# |--------------------------------------------
# | The object that will be used to represent
# | each node of a Pascal Christmas tree.
# |----------------------------------
class pascalLeaf():
    def __init__(self, branchNumber, leafNumber):
        self.pascalValue = self.nCr(branchNumber, leafNumber)

        self.colour = self.calculateColour(self.pascalValue, branchNumber, leafNumber)

    # | nCr()
    # |-----------------------------------------------------------
    # | Calculates the value of a pascal's triangle node with
    # | the formula for the binomial coefficient 'nCr'.
    # |-------------------------------------------
    def nCr(self, n, r):
        value = math.factorial(n) / (math.factorial(r) * (math.factorial(n - r)))
        return value

    def calculateColour(self, leafValue, leafBranch, leafNumber):

        colourOffset = int(math.log(leafValue, 1.4))
        print(colourOffset)

        green = 255 - colourOffset

        return (0, green, 0)

import math
import helpers
import random
import colours

# | pascalLeaf()
# |--------------------------------------------
# | The object that will be used to represent
# | each node of a Pascal Christmas tree.
# |----------------------------------
class pascalLeaf():
    def __init__(self, branchNumber, leafNumber, size):
        self.pascalValue = self.nCr(branchNumber, leafNumber)

        self.isPrime = helpers.is_Prime(self.pascalValue)

        self.colour = 0
        self.Xpos = (leafNumber * size) - (branchNumber * (size / 2))
        self.Ypos = (branchNumber * size)

        self.calculateColour(self.pascalValue, 1.4)

    # | nCr()
    # |-----------------------------------------------------------
    # | Calculates the value of a pascal's triangle node with
    # | the formula for the binomial coefficient 'nCr'.
    # |-------------------------------------------
    def nCr(self, n, r):
        value = math.factorial(n) / (math.factorial(r) * (math.factorial(n - r)))
        return value

    def calculateColour(self, leafValue, logarithmBase):

        if self.isPrime:
            return random.choice(colours.baubleColours)

        colourOffset = int(math.log(leafValue, logarithmBase))

        green = 255 - colourOffset

        self.colour = (0, green, 0)

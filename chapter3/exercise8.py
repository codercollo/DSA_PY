# The following function is based on the age-old analogy used to describe
# the power of compounding interest:
# Imagine you have a chessboard and put a single grain of rice on one
# square. On the second square, you put 2 grains of rice, since that is
# double the amount of rice on the previous square. On the third square,
# you put 4 grains. On the fourth square, you put 8 grains, and on the fifth
# square, you put 16 grains, and so on.
# report erratum • discuss
# Wrapping Up • 45
# The following function calculates which square you’ll need to place a
# certain number of rice grains. For example, for 16 grains, the function
# will return 5, since you will place the 16 grains on the fifth square.
# Use Big O Notation to describe the time complexity of this function, which
# is below:


# function chessboardSpace(numberOfGrains) {
#   let chessboardSpaces = 1;
#   let placedGrains = 1;

#   while (placedGrains < numberOfGrains) {
#        placedGrains *= 2;
#        chessboardSpaces += 1;
#    }
#    return chessboardSpaces;
# }
#
#
# This is a log time O(log n) time complexity because the for the 
# number of grains in a square doubles and halving the grain in a square gives back the square position/number

# 3. Calculate the chessboard square for rice grains
# Answer: O(log N) — Logarithmic Time
# Explanation:
# - The while loop doubles placedGrains on every iteration.
# - The values grow exponentially: 1, 2, 4, 8, 16, 32...
# - Each additional iteration handles twice as many grains as before.
# - The number of iterations increases by one whenever the input doubles.
# Conclusion: Logarithmic time complexity, O(log N).
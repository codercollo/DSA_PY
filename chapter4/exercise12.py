# 2. If we have an O(N2) algorithm that processes an array and
# find that it takes 256 steps, what is the size of the array?

# For an O(N2) algorithm the number of steps grows
# proportionally to the square of the input size (N)


# For an algorithm doing a quadratic time the steps taken are 
# a square of the N elements in the array. 
import math

def array_size(steps):

  size = math.sqrt(steps)
  print(f"The size of the array:{size}")

array_size(256)
  

  
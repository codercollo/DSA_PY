# 3. Use Big O Notation to describe the time complexity of the following func-
# tion. It finds the greatest product of any pair of two numbers within a
# given array:

def greatestProduct(array):
    greatestProductSoFar = array[0] * array[1]
    steps = 0

    for i, iVal in enumerate(array):
       steps += 1
       for j, jVal in enumerate(array):
            steps += 1
            if i != j and iVal * jVal > greatestProductSoFar:
                greatestProductSoFar = iVal * jVal
    print(steps)            
    return greatestProductSoFar

print(greatestProduct([1,2,4,5,3]))

# Time Complexity: O(N2) - Quadratic Time
# This function uses two nested loops to examine pairs
# of numbers . The outer loop iterates through the array, while the inner loop
# compares each number against every other number.
#
# For every iteration of the outer loop (N) the inner loop
# runs N times, resulting in N * N = N2 iterations
# 
# We check each pair of numbers, multiply them and update
# greatestProductSoFar whenever we find a larger product
#
# Therefore the time complexity is O(n2) because the number 
# of operations grows quadratically as the input array increases


# This is a quadratic time where the steps taken are a square of the input 
# the for loops are two thus squaring the the steps because we have to find the 
# first values and index and second values and index the compare each and multiply 
# them to find the greatest product  
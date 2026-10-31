# 5. The next function iterates over an array of numbers, and for each number
# whose index is even, it prints the sum of that number plus every number
# in the array. What is this function’s efficiency in terms of Big O Notation?
# def every_other(array)
#   array.each_with_index do |number, index|
#     if index.even?
#       array.each do |other_number|
#         puts number + other_number
#       end
#    end
#  end
# end

# Ans: This is also a linear time O(N) because the N input 
# is proportional to the steps done , the loop iterates 
# over the elements then the step to find the even index and 
# step to sum  it and every other number plus then step to print
# thus N + 3 efficiency

# Ans: The time complexity is O(N²), also known as quadratic time.
#
# This is because the function contains nested loops.
#
# The outer loop iterates through the entire array (N iterations).
# For every even index, the inner loop iterates through the
# entire array again (N iterations).
#
# Since approximately half of the indices are even, the total
# operations are:
#
# N * (N/2) = N²/2
#
# Big O notation ignores constant coefficients, so this
# simplifies to O(N²).
#
# Therefore, the function has quadratic time complexity.
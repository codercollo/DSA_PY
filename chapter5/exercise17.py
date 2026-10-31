# 3. Use Big O Notation to describe the time complexity of the following func-
# tion, which returns the sum of all numbers of an array after the numbers
# have been doubled:

# def double_then_sum(array)
#    doubled_array = []
# array.each do |number|
#    doubled_array << number *= 2
# end
# sum = 0
#
# doubled_array.each do |number|
#    sum += number
# end
#
# return sum
# en

# Ans: This is a quadratic time complexity O(N2) because of the 
# fact that there are nested loops in the function, so the steps 
# are dependent on the two iteration loops to pass through the array
# first to double the numbers then a second iteration to sum the numbers 
# of the array then return step  : N^2 + 1 === O(N)


# Ans: This is  O(N) linear time. This is because the function
# iterates through the array twice, the first loop doubles each number
# (N), while the second loop calculates their sum(N)
#
# Total steps = N + N + 1 = 2N + 1
# Big O notation ignores constant coefficients and lower-order terms
# leaving O(n)
#
# NB: Two consecutive loops result in O(N), not O(N^2).
# Quadratic tiem O(N^2) typically occurs when we have nested loops.

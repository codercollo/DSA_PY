# 4. Use Big O Notation to describe the time complexity of the following func-
# tion, which accepts an array of strings and prints each string in multiple
# cases:
# def multiple_cases(array)
#   array.each do |string|
#     puts string.upcase
#     puts string.downcase
#     puts string.capitalize
# end
# end

# Ans: This is a linear time O(N) because the input 
# the function takes is proportial to the steps 
# to run the operations.
#
# The loop iterates over the array once while the 
# convertions of cases is one step for each type of case
# thus N + 3 this becomes O(N)
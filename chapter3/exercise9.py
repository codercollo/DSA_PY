# 4. The following function accepts an array of strings and returns a new array
# that only contains the strings that start with the character "a". Use Big O
# Notation to describe the time complexity of the function:


# function selectAStrings(array) {
#     let newArray = [];
  
#     for(let i = 0; i < array.length; i++) {
#           if (array[i].startsWith("a")) {
#               newArray.push(array[i]);
#         }
#     }
#       return newArray;
# }
#
# This is a linear time O(n) time complexity 
# because the steps to push the "a" to the new array
# increase with the elements in the original array provided
#
#4. Select strings starting with "a"
# Answer: O(N) — Linear Time
# Explanation:
# - The for loop examines every element in the array.
# - Each string is checked using startsWith("a").
# - Matching strings are added to the new array.
# - As the input array grows, the number of iterations grows proportionally.
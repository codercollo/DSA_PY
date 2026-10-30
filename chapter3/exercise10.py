# 5. The following function calculates the median from an ordered array.
# Describe its time complexity in terms of Big O Notation:


# function median(array) {
#   const middle = Math.floor(array.length / 2);

#    // If array has even amount of numbers:
# if (array.length % 2 === 0) {
    
#     return (array[middle - 1] + array[middle]) / 2;
#   } else { 
    
#     // If array has odd amount of numbers:
#     return array[middle];
# }
# }
# This is a constant time O(1) time complexity 
# because irrespective of the array elements two
# steps are carried out to get the median 
#
# 5. Calculate the median of an ordered array
# Answer: O(1) — Constant Time
# Explanation:
# - The function calculates the middle index directly.
# - It checks whether the array has an even or odd number of elements.
# - It accesses either one or two elements using their indexes.
# - It does not iterate through the array.
# The following function finds the greatest single number 
# within an array, but has an efficiency of O(N2).
# Rewrite the function so that it becomes a speedy O(N):


# O(N2) - Quadratic Time Complexity 
# Logic: 
# Loop through the array and assume the current number (i) is the greatest.
# Use a nested loop to compare i against every number (j) in the array.
# If another number is greater that i , i cannot be te greatest
# If i is still the greatest after all comparisons, return i
# 
# For every number in the array, we potentially compare it
# against every other number. This creates a nested loop (N * N)
# As the array grows, the number of comparisons grows quadractically.  
def greatestNumber(array):
  steps = 0
  for i in array:
    
    isIValTheGreatest = True

    for j in array:
      steps += 1
      if j > i:
        isIValTheGreatest = False

    if isIValTheGreatest:
      print("Steps: ", steps)
      return i    
   
print("The greatest number using O(n2): ",greatestNumber([1, 2, 6, 3, 4]))  


# O(N) Linear Time Complexity
# Logic:
# Assume the first number in the array is the greatest.
# Loop through the array once, comparing each number with greatest.
# If a larger number is found, update greatest
# After checking all numbers, return the greatest number.
#
# Time Complexity O(N)
# We traverse the array only once. Each number is checked 
# once against the current greatest number. Work grows linearly
# with the size of the array
def greatest_number(array) :
   greatest = array[0]
   steps = 0

   for number in array:
     steps += 1
     if number > greatest:
       greatest = number
   print("Steps: ", steps)
   return greatest

print("The greatest number using O(n): ", greatest_number([1, 2, 6, 3, 4]))    






6. # Use Big O Notation to describe the time complexity of the 
# following function that determines whether a given year is a leap year.


# function isLeapYear(year) {
#   return (year % 100 === 0 ) ? (year % 400 === 0) : (year % 4 === 0)
# } 
# 
# Time complexity of constant time O(1) because the steps to calculate the leap
# year is done once irreguardless of the modulo arithmetic operation  .

# Determine whether a year is a leap year
# Answer: O(1) — Constant Time
# Explanation:
# - The function performs a fixed number of arithmetic operations and comparisons.
# - It does not contain loops or recursion.
# - The number of operations remains the same regardless of the year passed.
# Conclusion: Constant time complexity, O(1).
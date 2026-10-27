# Normally the search operation in an array looks for the first
# instance of a given value. But sometimes we may want to look
# for every instance of a given value. For example, say we want 
# to count how many times the value (occurrence)"apple" is found inside an array
# How many steps would it take to find all the "apples" Give answer in 
# terms of N

def count_apples(fruits):
  count = 0
  steps = 0

  for fruit in fruits:
    steps += 1

    if fruit == "apple":
      count += 1

  print("Apples found:", count)
  print("Steps taken:", steps)

fruits = ["apples", "bananas", "apple", "orange", "apple"]
count_apples(fruits)     


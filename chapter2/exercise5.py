# What is the maximum number of steps it would take to 
# perform a binary search on an array of size 100,000

def binary_search(target):
  array_size = 100000
  ordered_array = list(range(array_size))
  steps = 0

  first_value = 0
  last_value = len(ordered_array)-1

  while first_value <= last_value:
    mid_index = (first_value + last_value) // 2
    mid_value = ordered_array[mid_index]

    steps += 1

    if target == mid_value:
      print("Found:", target)
      print("Steps:", steps) 
      return
    elif target < mid_value:
      last_value = mid_index -1

    else:
      first_value = mid_index + 1

    print("Not found")
    print("Steps:", steps)     

# Search for 47, which exists in the array
binary_search(47)

# Search for a number outside the array to test the maximum steps
# it would take to perform a binary search on an array of size 100,000
binary_search(100000)
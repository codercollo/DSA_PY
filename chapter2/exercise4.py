# How many steps would it take to perform a binary search 
# for the number 8 in the ordered array   [2, 4, 6, 8, 10, 12, 13]

def binary_search(target):

  ordered_array = [2, 4, 6, 8, 10, 12, 13]
  steps = 0

  first_value = 0
  last_value = len(ordered_array) - 1

  while first_value <= last_value:
    mid_index = (first_value + last_value) // 2
    mid_value =  ordered_array[mid_index]

    steps += 1

    if target == mid_value:
      print("Found:", target)
      print("Steps:", steps)
      return

    elif target < mid_value:
      last_value = mid_value - 1
    else:
      first_value = mid_index + 1

    print("Not found")
    print("Steps:", steps)     



binary_search(8)


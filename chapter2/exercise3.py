# How many steps would it take to perform a linear search for the 
# number 8 in the ordered array  [2, 4, 6, 8, 10, 12, 13]

def linear_search(target):
  ordered_array = [2, 4, 6, 8, 10, 12, 13]
  steps = 0

 # Iterate through the Elements only
  for number in ordered_array:
    steps += 1

    if number == 8 :
      print("Found:", number)
      print("Steps:", steps)
      return

  print("Not found")
  print("Steps:", steps)

   
linear_search(8)



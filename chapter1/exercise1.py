# For an array containing 100 elements, provide the number of steps the 
# following operations would take:
# Reading
# Searching for a value not contianed within the array
# Insertion at the beginning of the array
# Insertion at the end of the array
# Deletion at the beginning of the arrat
# Deletion at the end of the array

def array_operations():
  numbers = list(range(100))

   # Reading
  value = numbers[50]
  print("a. Reading:", value)

   # Searching for a value not in the array
  found = 200 in numbers
  print("b. Searching:", found)

   # Insertion at the beginning
  numbers.insert(0, -1)
  print("c. Insertion at beginning", numbers[0])

   # Insertion at the end
  numbers.append(100) 
  print("d. Insertion at end", numbers[-1])

  # Deletion at the beginning
  del numbers[0]
  print("e. Deletion at beginning:", numbers[0])

  # Deletion at the end
  numbers.pop()
  print("f. Deletion at end:", numbers[-1])


array_operations()  

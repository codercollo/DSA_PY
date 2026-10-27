# For an array-based set containing 100 elements,
# provide the number of steps the following operations would take:
# Reading
# Searching for a value at the contained within the array
# Insertion of a new value at the beginning of the set
# Insertion of a new value at the end of the set
# Deletion at the beginning of the set
# Deletion at the end of the set

def array_set_operations():
  numbers = list(range(100))

  # Reading
  value = numbers[50]
  print("a. Reading:", value, "| Steps: 1")

  # Searching for a value not contained in the set
  target = 200
  steps = 0
  for number in numbers:
    steps += 1
    if number == target:
      break

  print("b. Searching:", target, "|Steps:", steps)

  # Insertion of a new value at the beginning
  new_value = 200
  steps = 0

  for number in numbers:
    steps += 1
    if number == new_value:
      break


  if new_value not in numbers:
     numbers.insert(0, new_value)
     steps += 100 # Shift existing elements
     steps += 1 # Insert the new value  

  print("c. Insert at beginning | Steps:", steps)

  # d. Insertion of a new value at the end
  new_value = 201
  steps = 0

  for number in numbers:
    steps += 1
    if number == new_value:
      break

  if new_value not in numbers:
    numbers.append(new_value)
    steps += 1 # Insert the new value

  print("d. Insert at end | Steps:", steps)

  # e. Deletion at the beginning
  del numbers[0]
  print("e. Delete at beginning | Steps: 100" )

  # f. Deletion at the end
  numbers.pop()
  print("f Delete at end | Steps: 1")       

array_set_operations()
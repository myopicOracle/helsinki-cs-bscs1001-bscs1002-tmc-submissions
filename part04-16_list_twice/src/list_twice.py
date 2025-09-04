# Write your solution here

# Sample output

# New item: 3
# The list now: [3]
# The list in order: [3]
# New item: 1
# The list now: [3, 1]
# The list in order: [1, 3]
# New item: 9
# The list now: [3, 1, 9]
# The list in order: [1, 3, 9]
# New item: 5
# The list now: [3, 1, 9, 5]
# The list in order: [1, 3, 5, 9]
# New item: 0
# Bye!

# def sorted(unsorted_list : list) -> list:
#   print("Entered 'sorted()' function")
#   unsorted_list.sort()
#   print("Sorted-in-place list inside function: ", unsorted_list)
#   return unsorted_list

unordered_list = []

while True:
  # print("Entered 'while' loop")
  new_item = int(input("New item: "))
  # print(f"new_item is {new_item} with type {type(new_item)}")
  if new_item == 0:
    print("Bye!")
    break
  unordered_list.append(new_item)
  print(f"The list now: {unordered_list}")
  ordered_list = sorted(unordered_list)
  print(f"The list in order: {ordered_list}")
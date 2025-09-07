# Please write a function named remove_smallest(numbers: list), which takes a list of integers as its argument.

# The functions should find and remove the smallest item in the list. You may assume there is a single smallest item in the list.

# The function should not have a return value - it should directly modify the list it receives as a parameter.

# ========================

# Write your solution here

def remove_smallest(numbers: list):
  smallest_number = sorted(numbers)[0]
  print("smallest_number: ", smallest_number)
  numbers.remove(smallest_number)

# numbers = [2, 4, 6, 1, 3, 5]
# print("BEFORE calling function: ", numbers)
# remove_smallest(numbers)
# print("AFTER calling function: ", numbers)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)
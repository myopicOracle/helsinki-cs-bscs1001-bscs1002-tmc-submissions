# Please write a function named double_items(numbers: list), which takes a list of integers as its argument.

# The function should return a new list, which contains all values from the original list doubled. The function should not change the original list.

# ========================

# Write your solution here

def double_items(numbers: list) -> list:
  new_list = []

  for i in range(len(numbers)):
    new_list.append(numbers[i] * 2)

  return new_list


# TMC Test block

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)
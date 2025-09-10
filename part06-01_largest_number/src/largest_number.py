# The file numbers.txt contains integer numbers, one number per line. The contents could look like this:

# 2
# 45
# 108
# 3
# -10
# 1100
# ...etc...

# Please write a function named largest, which reads the file and returns the largest number in the file.

# Notice that the function does not take any arguments. The file you are working with is always named numbers.txt.

# ========================

# def to_list() -> list:
#   with open("numbers.txt") as new_file:
#     unsorted_list = []
#     for line in new_file:
#       unsorted_list.append(int(line))
#     print("unsorted_list: ", unsorted_list)
#     sorted_list = sorted(unsorted_list)
#     print("sorted_list: ", sorted_list)
#     return sorted_list

# print("to_list(): ", to_list())


def largest() -> int:
  with open("numbers.txt") as new_file:
    current_largest = 0
    for line in new_file:
      if int(line) > current_largest:
        current_largest = int(line)
    # print(current_largest)
    return current_largest

# print("largest(): ", largest())


# ========================

if __name__ == "__email__":
  pass
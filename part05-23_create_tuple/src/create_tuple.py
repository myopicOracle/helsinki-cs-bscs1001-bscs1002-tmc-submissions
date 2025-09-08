# Please write a function named create_tuple(x: int, y: int, z: int), which takes three integers as its arguments, and creates and returns a tuple based on the following criteria:

#     The first element in the tuple is the smallest of the arguments
#     The second element in the tuple is the greatest of the arguments
#     The third element in the tuple is the sum of the arguments

# ========================

def create_tuple(x: int, y: int, z: int) -> tuple:
  sorted_list = sorted([x, y, z])

  first_element = sorted_list[0]
  second_element = sorted_list[1]
  third_element = sorted_list[2]
  sum_of_elements = first_element + second_element + third_element

  my_tuple = (first_element, third_element, sum_of_elements)

  return my_tuple

# ========================

if __name__ == "__main__":
  print(create_tuple(5, 3, -1))
# The file matrix.txt contains a matrix in the format specified in the example below:

# 1,0,2,8,2,1,3,2,5,2,2,2
# 9,2,4,5,2,4,2,4,1,10,4,2
# ...etc...

# Please write two functions, named matrix_sum and matrix_max. Both go through the matrix in the file, and then return the sum of the elements or the element with the greatest value, as the names of the functions imply.

# Please also write the function row_sums, which returns a list containing the sum of each row in the matrix. For example, calling row_sums when the matrix in the file is defined as

# 1,2,3
# 2,3,4

# the function should return the list [6, 9].

# Hint: you can also include other helper functions in your program. It is very worthwhile to spend a moment considering which functionalities are shared by the three functions you are asked to write. Notice that the three functions named above do not take any arguments, but any helper functions you write may take arguments. The file you are working with is always named matrix.txt.

# ========================

# matrix sum/max could be achieved with a flattened matrix (1d list). row sums would require matrix (2d list). all three functions would require reading then extracting file contents into handler var. 

# Helper function

def read_file(file_name: str) -> list:
  matrix = []
  flat_list = []

  with open(file_name) as new_file:
    for line in new_file:
      line = line.replace("\n", "")
      split_line = line.split(",")
      # print("split_line: ", split_line) # console logger

      row = []
      for item in split_line:
        row.append(int(item))
        flat_list.append(int(item))

      matrix.append(row)

  # print("matrix: ", matrix) # console logger
  # print("flat_list: ", flat_list) # console logger
  return matrix, flat_list

# Main functions

def matrix_sum() -> int:
  flat_list = read_file("matrix.txt")[1]
  # print("flat_list: ", flat_list) # console logger
  return sum(flat_list)


def matrix_max() -> int:
  flat_list = read_file("matrix.txt")[1]
  # print("flat_list: ", flat_list) # console logger
  return max(flat_list)

def row_sums() -> list:
  matrix = read_file("matrix.txt")[0]
  # print("matrix: ", matrix) # console logger

  summed = []
  for row in matrix:
    summed.append(sum(row))

  return summed

# Test calls

# print(matrix_sum())
# print(matrix_max())
# print(row_sums())

# ========================

if __name__ == "__email__":
  matrix_sum()
  matrix_max()
  row_sums()
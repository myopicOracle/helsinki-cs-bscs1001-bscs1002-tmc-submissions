# Please write a function named transpose(matrix: list), which takes a two-dimensional integer array, i.e., a matrix, as its argument. The function should transpose the matrix. Transposing means essentially flipping the matrix over its diagonal: columns become rows, and rows become columns.

# You may assume the matrix is a square matrix, so it will have an equal number of rows and columns.

# ========================

# Write your solution here

def transpose(matrix: list):
  matrix_copy = []
  for row in matrix:
    matrix_copy.append(row[:])

  for row_no, row in enumerate(matrix):
    for column_no, item in enumerate(row):
      matrix[row_no][column_no] = matrix_copy[column_no][row_no]

  print(matrix_copy)
  print(matrix)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# transpose(matrix)


if __name__ == "__main__":
  pass
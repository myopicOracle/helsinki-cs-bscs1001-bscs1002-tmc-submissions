# This is the very last sudoku task. This time we will create a slightly different version of the function for adding new numbers to the grid.

# The function copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) takes a two-dimensional array representing a sudoku grid, two integers referring to the row and column indexes of a single square, and a single digit between 1 and 9, as its arguments. The function should return a copy of the original grid with the new digit added in the correct location. The function should not change the original grid received as a parameter.

# ========================

# Write your solution here

def print_sudoku(sudoku: list):
  for i, row in enumerate(sudoku):
    if i in [3, 6]:
      print()
    for j, square in enumerate(row):
      if j in [3, 6]:
        print(" ", end="")
      if square == 0:
        print("_ ", end="")
      else:
        print(f"{square} ", end="")
    print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
  sudoku_copy = []
  for row in sudoku:
    sudoku_copy.append(row[:])
  sudoku_copy[row_no][column_no] = number
  return sudoku_copy

# Test code

# sudoku  = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

# grid_copy = copy_and_add(sudoku, 0, 0, 2)
# print("Original:")
# print_sudoku(sudoku)
# print()
# print("Copy:")
# print_sudoku(grid_copy)

if __name__ == "__main__":
  pass
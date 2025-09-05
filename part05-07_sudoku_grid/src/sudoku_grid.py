# Please write a function named sudoku_grid_correct(sudoku: list), which takes a two-dimensional array representing a sudoku grid as its argument. The function should use the functions from the three previous exercises to determine whether the complete sudoku grid is filled in correctly. Copy the functions from the exercises above into your Python code file for this exercise.

# The function should check each of the nine rows, columns and 3 by 3 blocks in the grid. If all contain each of the numbers 1 to 9 at most once, the function returns True. If a single one is filled in incorrectly, the function returns False.

# The image of a sudoku grid above these exercises has the nine blocks within the grid indicated with thicker borders. These are the blocks the function should check, and they begin at the indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6).

# ==========================

# Write your solution here

# Check row_correct
def row_correct(sudoku: list, row_no: int) -> bool:

  non_zero = []
  for item in sudoku[row_no]:
    if item != 0:
      non_zero.append(item)

  if len(non_zero) != len(set(non_zero)):
    return False
  else:
    return True

# Check column_correct
def column_correct(sudoku: list, column_no: int) -> bool:

  constructed_column = []
  for row in sudoku:
    constructed_column.append(row[column_no])

  non_zero = []
  for item in constructed_column:
    if item != 0:
      non_zero.append(item)

  if len(non_zero) != len(set(non_zero)):
    return False
  else:
    return True

# Check block_correct
def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:

  constructed_block = []
  starting_row = row_no
  for i in range(3):
    sub_list = sudoku[starting_row][column_no : column_no + 3]
    for j in sub_list:
      constructed_block.append(j)
    starting_row += 1

  non_zero = []
  for item in constructed_block:
    if item != 0:
      non_zero.append(item)

  if len(non_zero) != len(set(non_zero)):
    return False
  else:
    return True

# Main function
def sudoku_grid_correct(sudoku: list) -> bool:
  check_row = False
  check_column = False
  check_block = False

  # Check 9 rows
  for row in range(len(sudoku)):
    check_row = row_correct(sudoku, row)
    if not check_row:
      return False

  # Check 9 columns
  for column in range(len(sudoku)):
    check_column = column_correct(sudoku, column)
    if not check_column:
      return False

  # Check 9 blocks
  for row in range(0, 9, 3):
    print("row number in block check: ", row)
    for column in range(0, 9, 3):
      print("column number in block check: ", column)
      check_block = block_correct(sudoku, row, column)
      if not check_block:
        return False

  print("check_row is: ", check_row)
  print("check_column is: ", check_column)
  print("check_block is: ", check_block)

  if check_row and check_column and check_block:
    return True
  else:
    return False

# Run pre-tests
# sudoku1 = [
#   [9, 0, 0, 0, 8, 0, 3, 0, 0],
#   [2, 0, 0, 2, 5, 0, 7, 0, 0],
#   [0, 2, 0, 3, 0, 0, 0, 0, 4],
#   [2, 9, 4, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 7, 3, 0, 5, 6, 0],
#   [7, 0, 5, 0, 6, 0, 4, 0, 0],
#   [0, 0, 7, 8, 0, 3, 9, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0, 0, 3],
#   [3, 0, 0, 0, 0, 0, 0, 0, 2]
# ]
# print(sudoku_grid_correct(sudoku1))

# sudoku2 = [
#   [2, 6, 7, 8, 3, 9, 5, 0, 4],
#   [9, 0, 3, 5, 1, 0, 6, 0, 0],
#   [0, 5, 1, 6, 0, 0, 8, 3, 9],
#   [5, 1, 9, 0, 4, 6, 3, 2, 8],
#   [8, 0, 2, 1, 0, 5, 7, 0, 6],
#   [6, 7, 4, 3, 2, 0, 0, 0, 5],
#   [0, 0, 0, 4, 5, 7, 2, 6, 3],
#   [3, 2, 0, 0, 8, 0, 0, 5, 7],
#   [7, 4, 5, 0, 0, 3, 9, 0, 1]
# ]
# print(sudoku_grid_correct(sudoku2))

# sudoku3 = [
#   [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
#   [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
#   [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
#   [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
#   [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
#   [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
#   [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
#   [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
#   [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
# ]
# sudoku_grid_correct(sudoku3)

# Test block
if __name__ == "__main__":
  print(sudoku_grid_correct(sudoku))
  
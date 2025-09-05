# Please write a function named block_correct(sudoku: list, row_no: int, column_no: int), which takes a two-dimensional array representing a sudoku grid, and two integers referring to the row and column indexes of a single square, as its arguments. Rows and columns are indexed from 0.

# The function should return True or False depending on whether the 3 by 3 block to the right and down from the given indexes is filled in correctly. That is, whether the block contains each of the numbers 1 to 9 at most once.

# Notice that this function does not strictly follow the rules of sudoku. In a real game of sudoku there are only 9 blocks to check, and these are located at indexes (0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3) and (6, 6). Such restrictions on indexes should not be implemented here.

# ==========================

# Write your solution here

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:

  constructed_block = []
  starting_row = row_no
  for i in range(3):
    sub_list = sudoku[starting_row][column_no : column_no + 3]
    for j in sub_list:
      constructed_block.append(j)
    starting_row += 1

  # print(f"Block is: {constructed_block}, row number is {row_no}, column number is {column_no}.")

  non_zero = []
  for item in constructed_block:
    if item != 0:
      non_zero.append(item)
  # print("non_zero: ", non_zero)
  # print("len(non_zero): ", len(non_zero))
  # print("set(non_zero): ", set(non_zero))
  # print("len(set(non_zero)): ", len(set(non_zero)))

  if len(non_zero) != len(set(non_zero)):
    return False
  else:
    return True

# sudoku = [
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

# print(block_correct(sudoku, 0, 0))
# print(block_correct(sudoku, 1, 2))

# # Test block
if __name__ == "__main__":
  print(block_correct(sudoku, 0, 0))
  print(block_correct(sudoku, 1, 2))

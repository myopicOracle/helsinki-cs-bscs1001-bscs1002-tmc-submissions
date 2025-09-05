# Please write a function named row_correct(sudoku: list, row_no: int), which takes a two-dimensional array representing a sudoku grid, and an integer referring to a single row, as its arguments. Rows are indexed from 0.

# The function should return True or False, depending on whether the row is filled in correctly, that is, whether it contains each of the numbers 1 to 9 at most once.

# ==========================

# Write your solution here

def row_correct(sudoku: list, row_no: int) -> bool:
  # print(f"Row is: {sudoku[row_no]}, row number is {row_no}.")

  non_zero = []
  for item in sudoku[row_no]:
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

# for i in range(9):
#   print(f"Currently on row {i}")
#   print(row_correct(sudoku, i))
#   print("==================+")

# Test block
if __name__ == "__main__":
  print(row_correct(sudoku, 0))
  print(row_correct(sudoku, 1))
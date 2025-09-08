# This final exercise in this part is a relatively demanding problem solving task. It can be solved in many different ways. Even though this current section in the material covers tuples, tuples are not necessarily the best way to go about solving this.

# Please write a program which prints out a square of letters as specified in the examples below. You may assume there will be at most 26 layers.

# Sample output

#   Layers: 3

#     CCCCC
#     CBBBC
#     CBABC
#     CBBBC
#     CCCCC

# Sample output

#   Layers: 4

#     DDDDDDD
#     DCCCCCD
#     DCBBBCD
#     DCBABCD
#     DCBBBCD
#     DCCCCCD
#     DDDDDDD

# ========================

# Scoping

# *Key Insight: instead of figuring out how to write logic to print each row, print layers outwards-in, so that the inner layers overwrite the outer layers!

# Should create a dict of 26 keys (1-26), each mapping to one letter
#   Layer 1 (dict[1]) = "A", Layer 2 (dict[2]) = "B", and so on

# Printing is done line-by-line
#   So the program logic should be row-wise and not concentric circles, even though the obvious pattern is concentric

# Turn blocks into matrices
#   Should probably turn the blocks into 2D list matrices first

# Size is always odd
#   This means there's always a middle value in each row
#   Predictable pattern because first and last char of row is same, middle value and everything between predictable

# ========================

layer_keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

layer_values = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alphabet_dict = {}
for i in range(26):
  alphabet_dict[layer_keys[i]] = layer_values[i]
# print(alphabet_dict)

# ========================

# BBB
# BAB
# BBB

# CCCCC
# CBBBC
# CBABC
# CBBBC
# CCCCC

# DDDDDDD
# DCCCCCD
# DCBBBCD
# DCBABCD
# DCBBBCD
# DCCCCCD
# DDDDDDD

layers_2_size = len("BBB")
# print(layers_2_size) # 3x3

layers_3_size = len("CCCCC")
# print(layers_3_size) # 5x5

layers_4_size = len("DDDDDDD")
# print(layers_4_size) # 7x7

# Relationship between layer and size
#   number_of_layers = int
#   size = ( number_of_layers * 2 ) - 1

# ========================

# 222
# 212
# 222

# 33333
# 32223
# 32123
# 32223
# 33333

# 4444444  
# 4333334  
# 4322234  
# 4321234  
# 4322234  
# 4333334  
# 4444444

# Use reverse stepping
#   Converting block of letters to integers shows how range(start, end, step) can be used to create matrix of integers

# ========================

# get user input for number of layers
number_of_layers = int(input("Layers: "))

# relate size to layers
size = ( number_of_layers * 2 ) - 1

# create empty matrix 
my_matrix = []
for i in range(size):
  row = []
  for j in range(size):
    row.append("_")
  my_matrix.append(row)

# print(my_matrix) # debugging statement
    
# fill in layers from outwards in
for layer in range(number_of_layers, 0, -1):
  letter = alphabet_dict[layer]
  start = number_of_layers - layer
  end = size - start
  for i in range(start, end):
    for j in range(start, end):
      my_matrix[i][j] = letter

# print(my_matrix) # debugging statement

# convert matrix to printed block
for row in my_matrix:
  for letter in row:
    print(letter, end="")
  print()


# ========================

if __name__ == "__main__":
  pass

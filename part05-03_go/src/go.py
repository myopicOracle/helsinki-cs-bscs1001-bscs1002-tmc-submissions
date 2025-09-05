# In a game of Go two players take turns to place black and white stones on a game board. The winner is the player who manages to encircle a bigger area on the board with their own game pieces.

# Please write a function named who_won(game_board: list), which takes a two-dimensional array as its argument. The array consists of integer values, which represent the following situations:

# 0: empty square
# 1: player 1 game piece
# 2: player 2 game piece
# The scoring rules of Go can be quite complex, but in this exercise it is enough to compare the number of pieces each player has on the game board. Also, the size of the game board is not limited.

# The function should return the value 1 if player 1 won, and the value 2 if player 2 won. If both players have the same number of pieces on the board, the function should return the value 0.

# ==========================

# Write your solution here

def who_won(game_board: list) -> int:
  player_1 = 0
  player_2 = 0 
  for row in game_board:
    player_1 += row.count(1)
    print(f"player 1's pieces on board is now: {player_1}")
    player_2 += row.count(2)
    print(f"player 2's pieces on board is now: {player_2}")
  if player_1 > player_2:
    return 1
  elif player_2 > player_1:
    return 2
  else:
    return 0

# gameboard = [
#   [2, 0, 1, 2, 0, 1, 1, 0, 2, 1, 0, 2, 0, 1, 2, 0, 1, 0],
#   [1, 2, 0, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0, 0, 2, 1, 0, 2],
#   [0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1, 0],
#   [2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 0, 2, 1, 0, 2, 1],
#   [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 0, 2, 1, 0, 2],
#   [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 0, 2, 1, 0],
#   [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 0, 2, 1],
#   [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 0, 2],
#   [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1, 0],
#   [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2, 1],
#   [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0, 2],
#   [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 0],
#   [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1],
#   [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0],
#   [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2],
#   [2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1],
#   [1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0],
#   [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
# ]

# print(who_won(gameboard))

# Test block
if __name__ == "__main__":
  print(who_won(gameboard))
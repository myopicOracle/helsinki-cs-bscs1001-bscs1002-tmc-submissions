# Please write a function named times_ten(start_index: int, end_index: int), which creates and returns a new dictionary. The keys of the dictionary should be the numbers between start_index and end_index inclusive

# The value mapped to each key should be the key times ten.

# ========================

def times_ten(start_index: int, end_index: int) -> dict:

  new_dictionary = {}

  for i in range(start_index, end_index + 1):
    new_dictionary[i] = i * 10

  return new_dictionary

# d = times_ten(3, 6)
# print(d)

# ========================
if __name__ == "__main__":
  pass

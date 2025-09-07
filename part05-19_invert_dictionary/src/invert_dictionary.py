# Please write a function named invert(dictionary: dict), which takes a dictionary as its argument. The dictionary should be inverted in place so that values become keys and keys become values.

# ========================

def invert(dictionary: dict) -> None:
  
  dict_copy = {}
  for key, value in dictionary.items():
    dict_copy[value] = key

  dictionary.clear()
  for key in dict_copy:
    dictionary[key] = dict_copy[key]
  
# s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
# print("Original dictionary: ", s)
# invert(s)
# print("Inverted in-place: ", s)

# ========================

if __name__ == "__main__":
  pass

# Please write a function named histogram, which takes a string as its argument. The function should print out a histogram representing the number of times each letter occurs in the string. Each occurrence of a letter should be represented by a star on the specific line for that letter.

# ========================

def output_histogram(dict_input: dict):
  for key, value in dict_input.items():
    occurence = "*" * value
    print(f"{key} {occurence}")

def histogram(str_input: str):
  my_dictionary = {}
  for char in str_input:
    # print(f"At character '{char}' in string '{str_input}'.")
    if char not in my_dictionary:
      my_dictionary[char] = 0
    my_dictionary[char] += 1
    # print(f"Dictionary is now: {my_dictionary}.")
  output_histogram(my_dictionary)

# histogram("abba")
# histogram("statistically")


# ========================

if __name__ == "__main__":
  pass

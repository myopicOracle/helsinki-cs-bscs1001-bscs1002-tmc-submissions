# Write your solution here

# Please write a function named most_common_character, which takes a string argument. The function returns the character which has the most occurrences within the string. If there are many characters with equally many occurrences, the one which appears first in the string should be returned.

# An example of expected behaviour:

# first_string = "abcdbde"
# print(most_common_character(first_string))

# second_string = "exemplaryelementary"
# print(most_common_character(second_string))
# Sample output
# b
# e

def most_common_character(my_string: str):
  # str_to_list = list(my_string)
  # print(str_to_list)
  # unique_chars = list(set(str_to_list))
  # print(unique_chars)
  helper_var = 0
  most_common = ""
  for i in my_string:
    print(f"Char: {i}, Count of Char: {my_string.count(i)}")
    if my_string.count(i) > helper_var:
      helper_var = my_string.count(i)
      most_common = i
  return most_common


# print(most_common_character("abcdbde"))

if __name__ == "__main__":
  most_common_character("abcdbde")
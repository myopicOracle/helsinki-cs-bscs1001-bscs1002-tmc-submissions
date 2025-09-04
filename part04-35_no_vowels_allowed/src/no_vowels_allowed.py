# Write your solution here

# Please write a function named no_vowels, which takes a string argument. The function returns a new string, which should be the same as the original but with all vowels removed.

# You can assume the string will contain only characters from the lowercase English alphabet a...z.

# An example of expected behaviour:

# my_string = "this is an example"
# print(no_vowels(my_string))
# Sample output
# ths s n xmpl

def no_vowels(my_string : str):
  vowels = ["a", "e", "i", "o", "u"]
  for i in vowels:
    my_string = my_string.replace(i, "")
  return my_string

# print(no_vowels("this is an example"))

if __name__ == "__main__":
  no_vowels("this is an example")
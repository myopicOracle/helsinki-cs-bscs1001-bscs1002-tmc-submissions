# Please write a function named longest(strings: list), which takes a list of strings as its argument. The function finds and returns the longest string in the list. You may assume there is always a single longest string in the list.

# An example of expected behaviour:

# if __name__ == "__main__":
#     strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
#     print(longest(strings))
# Sample output
# howdydoody

# ==========================

# Write your solution here

def longest(list_of_strings: list) -> str:

  current_longest = 1
  return_value = ""
  for i in list_of_strings:
    if len(i) > current_longest: 
      # print(f"The current item in loop is \"{i}\", it's length is {len(i)}.")
      current_longest = len(i)
      # print("current_longest: ", current_longest)
      return_value = i
      # print("return_value: ", return_value)
  
  return return_value

# strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
# print(longest(strings))


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
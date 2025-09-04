# Write your solution here

# Please write a function named everything_reversed, which takes a list of strings as its argument. The function returns a new list with all of the items on the original list reversed. Also the order of items should be reversed on the new list.

# An example of how the function should work:

# my_list = ["Hi", "there", "example", "one more"]
# new_list = everything_reversed(my_list)
# print(new_list)
# Sample output
# ['erom eno', 'elpmaxe', 'ereht', 'iH']

def everything_reversed(my_list : list):
  new_list = []
  reversed_list = my_list[::-1]
  for i in reversed_list:
    new_list.append(i[::-1])
  return new_list

# print(everything_reversed(["Hi", "there", "example", "one more"]))

if __name__ == "__main__":
  everything_reversed(["Hi", "there", "example", "one more"])
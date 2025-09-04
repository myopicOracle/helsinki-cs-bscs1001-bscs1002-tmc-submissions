# Write your solution here

# Please use the isupper method to write a function named no_shouting, which takes a list of strings as an argument. The function returns a new list, containing only those items from the original which do not consist of solely uppercase characters.

# An example of expected behaviour:

# my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
# pruned_list = no_shouting(my_list)
# print(pruned_list)
# Sample output
# ['def', 'lower', 'another lower', 'Capitalized']

def no_shouting(list_of_strings : list):
  new_list = []
  for i in list_of_strings:
    if i.isupper() == False:
      new_list.append(i)
  return new_list

# print(no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]))

if __name__ == "__main__":
  no_shouting(["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"])
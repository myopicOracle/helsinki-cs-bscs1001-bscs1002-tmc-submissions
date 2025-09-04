# Write your solution here

# Given a list of integers, let's decide that two consecutive items in the list are neighbours if their difference is 1. So, items 1 and 2 would be neighbours, and so would items 56 and 55.

# Please write a function named longest_series_of_neighbours, which looks for the longest series of neighbours within the list, and returns its length.

# For example, in the list [1, 2, 5, 4, 3, 4] the longest list of neighbours would be [5, 4, 3, 4], with a length of 4.

# An example function call:

# my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
# print(longest_series_of_neighbours(my_list))
# Sample output
# 4

# def longest_series_of_neighbours(my_list: list):
#   longest_count = 0
#   for i in range(len(my_list)-1):
#     sub_list = my_list[index:-1]
#     for j in sub_list:
#       condition = (sub_list[j] - sub_list[j+1]) == 1 or (sub_list[j] - sub_list[j+1]) == -1
#       longest_count += 1
#   return longest_count

def longest_series_of_neighbours(my_list: list):
  index = 0
  max_longest = 1
  while index < (len(my_list) - 1):
      current_longest = 1
      while index < (len(my_list) - 1) and ((my_list[index] - my_list[index+1]) == 1 or (my_list[index] - my_list[index+1]) == -1):
          current_longest += 1
          index += 1
      if current_longest > max_longest:
          max_longest = current_longest
      index += 1
  return max_longest
    
# print(longest_series_of_neighbours([1, 2, 5, 7, 6, 5, 6, 7, 6, 5, 6, 3, 4, 1, 0]))

if __name__ == "__main__":
    longest_series_of_neighbours([1, 2, 5, 7, 6, 5, 6, 7, 6, 5, 6, 3, 4, 1, 0])


# Write your solution here

# my_list = [3, 2, 2, 1, 3, 3, 1]
# print(distinct_numbers(my_list)) # [1, 2, 3]

# test_list = [3, 2, 2, 1, 3, 3, 1]
# test_list = [-1, -2, -1, -2, -3, -3, -3, 0, 0]

def distinct_numbers(some_list : list) -> list: 
  # print(some_list)
  # unique_set = set(some_list)
  # print(unique_set)
  # unique_list = list(unique_set)
  # print(unique_list)
  # unique_list.sort()
  # return unique_list

  return (sorted(list(set(some_list))))

# print(distinct_numbers(test_list))



# Test
if __name__ == "__main__":
  distinct_numbers([3, 2, 2, 1, 3, 3, 1])
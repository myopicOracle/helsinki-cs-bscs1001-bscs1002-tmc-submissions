# Write your solution here

# my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

# result = length_of_longest(my_list)
# print(result)

# ===========================

def length_of_longest(my_list : list) -> int:
  helper_var = 0
  for i in my_list:
    # print(f"Item: {i}, item length: {len(i)} longest: {helper_var}")
    # print("BEG longest: ", helper_var)
    if len(i) > helper_var:
      helper_var = len(i)
    # print("END longest: ", helper_var)
  # print("Final longest: ", helper_var)
  return helper_var

# print(length_of_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))

# ===========================

# Test
if __name__ == "__main__":
  length_of_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])

# Write your solution here

def length_of_longest(my_list : list) -> int:
  helper_var = 0
  for i in my_list:
    if len(i) > helper_var:
      helper_var = len(i)
  return helper_var

def all_the_longest(my_list : list) -> list:
  result = []
  longest = length_of_longest(my_list)
  for i in my_list:
    if len(i) == longest:
      result.append(i)
  return result

# print(all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))

# ===========================
# Model Solution

# def all_the_longest(names: list):
#     result = []
 
#     for name in names:
#         if result == [] or len(name) > len(result[0]):
#             result = [name]
#         elif len(name) == len(result[0]):
#             result.append(name)
 
#     return result

# ===========================

# Test
if __name__ == "__main__":
  all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])
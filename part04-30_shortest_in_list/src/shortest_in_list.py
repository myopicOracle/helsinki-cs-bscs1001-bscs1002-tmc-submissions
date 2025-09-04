# Write your solution here

def shortest(my_list : list) -> int:
  # helper_var = 0
  # for i in range(len(my_list)):
  #   if len(my_list[i]) < len(my_list[helper_var]):
  #     helper_var = i
  # return my_list[helper_var]

  helper_var = "su·per·ca·li·fra·gil·is·tic·ex·pi·a·li·do·cious"
  for i in my_list:
    if len(i) < len(helper_var):
      helper_var = i
  return helper_var

# print(shortest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))

# ===========================
# Model Solution:
# def shortest(names: list):
#     result = ""
 
#     for nimi in names:
#         if result == "" or len(nimi) < len(result):
#             result = nimi
 
#     return result

# ===========================

# Test
if __name__ == "__main__":
  shortest(["adele", "mark", "dorothy", "tim", "hedy", "richard"])

# This exercise is about creating a program which allows the user to search for recipes based on their names, preparation times, or ingredients used. The program should read the recipes from a file submitted by the user.

# Each recipe consists of three or more lines. The first line has the name of the recipe, the second line contains an integer number representing the preparation time in minutes, and the remaining line or lines contain the ingredients used, one on each line. The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file. So, there can be more than one recipe in a single file, like in the example below.

#   ... (See txt files for recipes)

# Hint: it might be best to first read through all the lines in the file and pop them into a list, which is then easier to manipulate in the way described in the exercise.

# Part 1. Search for recipes based on the name of the recipe

#   Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose name contains the given search string. The names of these recipes are then returned in a list.

#   An example of the function in action:

#   found_recipes = search_by_name("recipes1.txt", "cake")

#   for recipe in found_recipes:
#       print(recipe)

#   Sample output

#   Pancakes
#   Cake pops

#   As you can see in the example above, the case of the letters is irrelevant. The search term cake returns both Pancakes and Cake pops, even though the latter is capitalized.

#   NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.

# Part 2. Search for recipes based on the preparation time

#   Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments. The function should go through the file and select all recipes whose preparation time is at most the number given.

#   The names of these recipes are again returned in a list, but the preparation time should be appended to each name. Please have a look at the example below.

#   found_recipes = search_by_time("recipes1.txt", 20)

#   for recipe in found_recipes:
#       print(recipe)

#   Sample output

#   Pancakes, preparation time 15 min

# Part 3. Search for recipes based on the ingredients

#   A word of caution: this third part of the exercise is considerably more demanding than the previous two. If you feel like you aren't making headway, it may be worth your while to move on, complete the other exercises in this part of the material, and then come back to this exercise if you have time later. Remember, you can submit and receive points for the first two parts of this exercise even if you haven't completed the third part.

#   Please write a function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose ingredients contain the given search string.

#   The names of these recipes are returned in a list just like in the second part, with the preparation time appended. Please have a look at the example below.

#   found_recipes = search_by_ingredient("recipes1.txt", "eggs")

#   for recipe in found_recipes:
#       print(recipe)

#   Sample output

#   Pancakes, preparation time 15 min
#   Meatballs, preparation time 45 min
#   Cake pops, preparation time 60 min

# ========================
# Part 1

# file_name = "recipes1.txt" # harcoded var for testing

def get_recipe_matrix(file_name: str) -> list:
  recipe_list = []

  with open(file_name) as new_file:
    single_recipe = []
    for line in new_file:
      line = line.strip()
      single_recipe.append(line)
      if line == '':
        single_recipe.pop()
        recipe_list.append(single_recipe)
        single_recipe = []
        continue
    recipe_list.append(single_recipe)

  # print(recipe_list) # debugger
  return recipe_list

# print(get_recipe_matrix(file_name)) # debugger


def search_by_name(file_name: str, word: str) -> list:
  all_recipes = get_recipe_matrix(file_name)
  filtered_recipes = []

  for recipe in all_recipes:
    if word in recipe[0].lower():
      filtered_recipes.append(recipe[0])
  
  # print(filtered_recipes) # debugger
  return filtered_recipes

# print(search_by_name(file_name, "cake")) # debugger


# ========================
# Part 2

def search_by_time(file_name: str, prep_time: int) -> list:
  all_recipes = get_recipe_matrix(file_name)
  filtered_recipes = []

  for recipe in all_recipes:
    if int(recipe[1]) <= prep_time:
      name = recipe[0]
      time = recipe[1]
      filtered_recipes.append(f"{name}, preparation time {time} min")

  # print(filtered_recipes) # debugger
  return filtered_recipes

# print(search_by_time(file_name, 20)) # debugger


# ========================
# Part 3

def search_by_ingredient(file_name: str, ingredient: str) -> list:
  all_recipes = get_recipe_matrix(file_name)
  filtered_recipes = []

  for recipe in all_recipes:
    if ingredient in recipe[2:]:
      name = recipe[0]
      time = recipe[1]
      filtered_recipes.append(f"{name}, preparation time {time} min")
  
  # print(filtered_recipes) # debugger
  return filtered_recipes

# print(search_by_ingredient(file_name, "eggs")) # debugger


# ========================

if __name__ == "__email__":
  # search_by_name(file_name, "cake")
  # search_by_time(file_name, 15)
  # search_by_ingredient(file_name, "eggs")
  pass
# Please write a function named new_person(name: str, age: int), which creates and returns a tuple containing the data in the arguments. The first element should be the name and the second the age.

# If the values stored in the parameter variables are not valid, the function should throw a ValueError exception.

# Invalid parameters in this case include:

#     name is an empty string
#     name contains less than two words
#     name is longer than 40 characters
#     age is a negative number
#     age is greater than 150

# ========================

def new_person(name: str, age: int) -> tuple:

  # name is an empty string
  condition_1 = name == ""

  # name contains less than two words
  condition_2 = " " not in name

  # name is longer than 40 characters 
  condition_3 = len(name) > 40

  # age is a negative number
  condition_4 = age < 0

  # age is greater than 150
  condition_5 = age > 150

  name_errors = []
  if condition_1:
    name_errors.append("Name cannot be empty.")
  if condition_2:
    name_errors.append("Name must contain at least 2 words.")
  if condition_3:
    name_errors.append("Name cannot be longer then 40 characters.")

  age_errors = []
  if condition_4:
    age_errors.append("Age cannot be a negative integer.")
  if condition_5:
    age_errors.append("Age cannot be greater than 150.")

  if condition_1 or condition_2 or condition_3:
    raise ValueError(f"'Name' input value errors found: {" ".join(name_errors)}")
  
  if condition_4 or condition_5:
    raise ValueError(f"'Age' input value errors found: {" ".join(age_errors)}")
  
  return name, age


# print(new_person("Horatio Summers", 27)) # testing
# print(new_person("", 27)) # testing
# print(new_person("Horatio", 27)) # testing
# print(new_person("Horatio Orelius Ludwig von Duchenstein el Capo de Summers", 27)) # testing
# print(new_person("Horatio Summers", -1)) # testing
# print(new_person("Horatio Summers", 999)) # testing


# ========================

if __name__ == "__main__":
  pass

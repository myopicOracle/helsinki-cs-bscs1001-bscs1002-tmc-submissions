# Please write a function named add_movie(database: list, name: str, director: str, year: int, runtime: int), which adds a new movie object into a movie database.

# The database is a list, and each movie object in the list is a dictionary. The dictionary should contain the following keys.

#     name
#     director
#     year
#     runtime

# The values attached to these keys are given as arguments to the function.

# ========================

def add_movie(database: list, name: str, director: str, year: int, runtime: int) -> None:
  new_dict = {}
  # print("New dictionary before: ", new_dict)

  new_dict["name"] = name
  new_dict["director"] = director
  new_dict["year"] = year
  new_dict["runtime"] = runtime
  # print("New dictionary after: ", new_dict)

  # print("Database before function call: ", database)
  database.append(new_dict)
  # print("Database after function call: ", database)

# database = []
# add_movie(database, "Gone with the Python", "Victor Pything", 2017, 116)
# add_movie(database, "Pythons on a Plane", "Renny Pytholin", 2001, 94)
# print(database)

# ========================

if __name__ == "__main__":
  pass

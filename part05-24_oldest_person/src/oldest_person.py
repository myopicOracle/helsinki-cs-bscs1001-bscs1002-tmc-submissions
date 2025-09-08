# Please write a function named oldest_person(people: list), which takes a list of tuples as its argument. In each tuple, the first element is the name of a person, and the second element is their year of birth. The function should find the oldest person on the list and return their name.

# ========================

def oldest_person(people: list) -> str:
  name_of_oldest = ""
  current_oldest = 2025

  for person in people:
    if person[1] < current_oldest:
      current_oldest = person[1]
      name_of_oldest = person[0]
  
  return name_of_oldest

# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]

# print(oldest_person(people))

# ========================

if __name__ == "__main__":
  pass
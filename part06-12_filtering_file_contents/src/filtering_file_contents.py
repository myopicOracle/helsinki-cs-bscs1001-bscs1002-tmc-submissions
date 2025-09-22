# The file solutions.csv contains some solutions to mathematics problems:

# Arto;2+5;7
# Pekka;3-2;1
# Erkki;9+3;11
# Arto;8-3;4
# Pekka;5+5;10
# ...jne...

# As you can see above, on each line the format is name_of_student;problem;result. All the operations are either addition or subtraction, and each has exactly two operands.

# Please write a function named filter_solutions() which

#     Reads the contents of the file solutions.csv
#     writes those lines which have a correct result into the file correct.csv
#     writes those lines which have an incorrect result into the file incorrect.csv

# NB: the function should have the exact same result, no matter how many times it is called. That is, it shouldn't matter if the function is called once or multiple times in a row.

# ========================

def filter_solutions() -> None:
  all_solutions = []
  correct_solutions = []
  incorrect_solutions = []

  with open("solutions.csv") as new_file:
    for line in new_file:
      line = line.strip()
      parts = line.split(";")
      all_solutions.append(parts)
  
  # print(all_solutions)

  for solution in all_solutions:
    solution_string = solution[1]
    answer_string = solution[2]
    # print("solution_string: ", solution_string) # debugger

    if "+" in solution_string:
      parts = solution_string.split("+")
      # print("student solution: ", parts, "| student answer: ", answer_string) # debugger
      condition = (int(parts[0]) + int(parts[1])) == int(answer_string)
      # print("condition: ", condition) # debugger
      if condition:
        correct_solutions.append(solution)
      else:
        incorrect_solutions.append(solution)
      
    elif "-" in solution_string:
      parts = solution_string.split("-")
      # print("student solution: ", parts, "| student answer: ", answer_string) # debugger
      condition = (int(parts[0]) - int(parts[1])) == int(answer_string)
      # print("condition: ", condition) # debugger
      if condition:
        correct_solutions.append(solution)
      else:
        incorrect_solutions.append(solution)

  # print(correct_solutions) # debugger
  # print(incorrect_solutions) # debugger

  with open("correct.csv", "w") as new_file:
    for solution in correct_solutions:
      line = ""
      for part in solution:
        line += f"{part};"
      line = line[:-1]
      new_file.write(line+"\n")

  with open("incorrect.csv", "w") as new_file:
    for solution in incorrect_solutions:
      line = ""
      for part in solution:
        line += f"{part};"
      line = line[:-1]
      new_file.write(line+"\n")
  

# filter_solutions() # testing


# ========================

if __name__ == "__main__":
  pass

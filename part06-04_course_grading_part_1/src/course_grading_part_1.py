# This program works with two CSV files. One of them contains information about some students on a course:

#   id;first;last
#   12345678;peter;pythons
#   12345687;jean;javanese
#   12345699;alice;adder

# The other contains the number of exercises each student has completed each week:

#   id;e1;e2;e3;e4;e5;e6;e7
#   12345678;4;1;1;4;5;2;4
#   12345687;3;5;3;1;5;4;6
#   12345699;10;2;2;7;10;2;2

# As you can see above, both CSV files also have a header row, which tells you what each column contains.

# Please write a program which asks the user for the names of these two files, reads the files, and then prints out the total number of exercises completed by each student. If the files have the contents in the examples above, the program should print out the following:

# Sample output

#   Student information: students1.csv
#   Exercises completed: exercises1.csv
#   pekka peloton 21
#   jaana javanainen 27
#   liisa virtanen 35

# ========================

student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")

# hardcoded for testing
# student_file = "students2.csv"
# exercise_file = "exercises2.csv"

students = {}
with open(student_file) as new_file:
  for line in new_file:
    line = line.split(";")
    if line[0] == "id":
      continue
    else: 
      student_key = line[0].strip()
      name = f"{line[1].strip()} {line[2].strip()}"
      students[student_key] = name
  # print(students) # debugger

exercises = {}
with open(exercise_file) as new_file:
  for line in new_file:
    line = line.replace("\n", "")
    line = line.split(";")
    if line[0] == "id":
      continue
    else: 
      student_key = line[0].strip()
      name = students[student_key]
      completed_exercises = 0
      for item in line[1:]:
        completed_exercises += int(item)
      exercises[student_key] = (name, completed_exercises)
  # print(exercises) # debugger

for key, value in exercises.items():
  print(f"{value[0]} {value[1]}")


# ========================

if __name__ == "__email__":
  pass
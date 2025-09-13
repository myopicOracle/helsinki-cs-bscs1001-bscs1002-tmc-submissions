# This exercise will continue from the previous one. Now we shall print out some statistics based on the CSV files.
# Sample output

# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv

# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3

# Each row contains the information for a single student. The number of exercises completed, the number of exercise points awarded, the number of exam points awarded, the total number of points awarded, and the grade are all displayed in tidy columns. The width of the column for the name should be 30 characters, while the other columns should be 10 characters wide.

# You might find the f-strings covered in part 4 useful here.

# F-strings differentiate between strings and numbers when it comes to justifying columns:

# word = "python"
# print(f"{word:10}continues")
# print(f"{word:>10}continues")

# Sample output

# python    continues
#     pythoncontinues

# As you can see above, by default strings are justified to the left edge of the area specified for them. The > symbol can be used to justify to the right edge.

# With number values the logic is reversed:

# number = 42
# print(f"{number:10}continues")
# print(f"{number:<10}continues")

# Sample output

#         42continues
# 42        continues

# With numbers the default behaviour is to justify to the right edge. The symbol < can be used to justify to the left edge.

# ========================

def extract_file(file_name: str) -> list:
  output_list = []
  with open(file_name) as new_file:
    for line in new_file:
      line = line.replace("\n", "")
      parts = line.split(";")
      if parts[0] == "id":
        continue
      else: 
        output_list.append(parts)
  # print("File name: ", file_name, "\nExtracted file contents:", output_list) # debugger
  return output_list


def map_names(file_name: str) -> dict:
  students = {}
  content_list = extract_file(file_name)

  for row in content_list:
    student_key = row[0]
    name = f"{row[1]} {row[2]}"
    students[student_key] = name

  # print("students: ", students) # debugger
  return students


def map_exercises(file_name: str) -> dict:
  exercises = {}
  content_list = extract_file(file_name)

  for row in content_list:
    student_key = row[0]
    exercise_points = sum([int(points) for points in row[1:]])
    # print(exercise_points) # debugger
    exercises[student_key] = exercise_points
  
  # print("exercises: ", exercises) # debugger
  return exercises


def map_exams(file_name: str) -> dict:
  exams = {}
  content_list = extract_file(file_name)

  for row in content_list:
    student_key = row[0]
    exam_scores = sum([int(scores) for scores in row[1:]])
    # print(exam_scores) # debugger
    exams[student_key] = exam_scores

  # print("exams: ", exams) # debugger
  return exams


def get_grades(student_file: str, exercise_file: str, exam_file: str) -> list:

  names_dict = map_names(student_file)
  # print("names_dict: ", names_dict) # debugger
  exercises_dict = map_exercises(exercise_file)
  # print("exercises_dict: ", exercises_dict) # debugger
  exams_dict = map_exams(exam_file)
  # print("exams_dict: ", exams_dict) # debugger

  grades = []

  for key, value in names_dict.items():

    # scale exercise points earned
    number_completed = int(exercises_dict[key])
    percentage_completed = ( number_completed / 40 ) * 100 # convert raw points to %
    # print("percentage_completed: ", percentage_completed) # debugger
    exercise_points = int(percentage_completed // 10) # round down to nearest % tier per instructions
    # print("exercise_points: ", exercise_points) # debugger
    
    # calculate total points earned
    exam_points = int(exams_dict[key])
    total_points = int(exam_points + exercise_points)

    # calculate grade
    if total_points >= 28:
      grade = 5
    elif total_points >= 24:
      grade = 4
    elif total_points >= 21:
      grade = 3
    elif total_points >= 18:
      grade = 2
    elif total_points >= 15:
      grade = 1
    else:
      grade = 0

    # store name & grade to dict
    name = value
    grades.append( (name, number_completed, exercise_points, exam_points, total_points, grade) )

  # print("grades - list of tuples: ", grades) # debugger
  return grades

  
def main() -> None:
  
  # get file names from user input
  student_file = input("Student information: ")
  exercise_file = input("Exercises completed: ")
  exam_file = input("Exam points: ")

  # # hardcoded for testing
  # student_file = "students1.csv"
  # exercise_file = "exercises1.csv"
  # exam_file = "exam_points1.csv"
  # student_file = "students2.csv"
  # exercise_file = "exercises2.csv"
  # exam_file = "exam_points2.csv"

  student_stats = get_grades(student_file, exercise_file, exam_file)
  # print("student_stats: ", student_stats) # debugger

  print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")
  for student in student_stats:
    name, number_completed, exercise_points, exam_points, total_points, grade = student
    print(f"{name:30}{str(number_completed):10}{str(exercise_points):10}{str(exam_points):10}{str(total_points):10}{str(grade):10}")

main()

# ========================

if __name__ == "__email__":
  pass

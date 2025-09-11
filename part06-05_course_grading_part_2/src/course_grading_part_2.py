# Let's expand the program created in the previous exercise. Now also the exam points awarded to each student are contained in a CSV file. The contents of the file follow this format:

#   id;e1;e2;e3
#   12345678;4;1;4
#   12345687;3;5;3
#   12345699;10;2;2

# In the above example the student whose student number is 12345678 was awarded 4+1+4 points in the exam, which equals a total of 9 points.

# The program should again ask the user for the names of the files. Then the program should process the files and print out a grade for each student.

# Rubric: exam points + exercise points	-> grade

#   0-14	-> 0 (fail)
#   15-17	-> 1
#   18-20	-> 2
#   21-23	-> 3
#   24-27	-> 4
#   28-  	-> 5

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


def get_grades(student_file: str, exercise_file: str, exam_file: str) -> dict:

  names_dict = map_names(student_file)
  # print("names_dict: ", names_dict) # debugger
  exercises_dict = map_exercises(exercise_file)
  # print("exercises_dict: ", exercises_dict) # debugger
  exams_dict = map_exams(exam_file)
  # print("exams_dict: ", exams_dict) # debugger

  grades = {}

  for key, value in names_dict.items():

    # scale exercise points earned
    percentage_completed = ( exercises_dict[key] / 40 ) * 100 # convert raw points to %
    # print("percentage_completed: ", percentage_completed) # debugger
    exercise_points = percentage_completed // 10 # round down to nearest % tier per instructions
    # print("exercise_points: ", exercise_points) # debugger
    
    # calculate total points earned
    exam_points = exams_dict[key]
    total_points = exam_points + exercise_points

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
    grades[key] = (name, grade)

  # print("grades: ", grades) # debugger
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

  for student in student_stats.values():
    name = student[0]
    grade = student[1]
    print(f"{name} {grade}")

main()

# ========================

if __name__ == "__email__":
  pass
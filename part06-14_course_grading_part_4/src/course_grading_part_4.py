# Let's revisit the course grading project from the previous section.

# As we left if last time, the program read and processed files containing student information, completed exercises and exam results. We'll add a file containing information about the course. An example of the format of the file:
# Sample data

# name: Introduction to Programming
# study credits: 5

# The program should then create two files. There should be a file called results.txt with the following contents:
# Sample data

# Introduction to Programming, 5 credits
# ======================================
# name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
# pekka peloton                 21        5         9         14        0
# jaana javanainen              27        6         11        17        1
# liisa virtanen                35        8         14        22        3

# The statistics section is identical to the results printed out in part 3 of the project. The only addition here is the header section.

# Additionally, there should be a file called results.csv with the following format:
# Sample data

# 12345678;pekka peloton;0
# 12345687;jaana javanainen;1
# 12345699;liisa virtanen;3

# When the program is executed, it should look like this:
# Sample output

# Student information: students1.csv
# Exercises completed: exercises1.csv
# Exam points: exam_points1.csv
# Course information: course1.txt
# Results written to files results.txt and results.csv

# That is, the program only asks for the names of the input files. All output should be written to the files. The user will only see a message confirming this.

# ========================

def read_student_files(file_name: str) -> list:
  output_list = []

  with open(file_name) as new_file:
    for line in new_file:
      line = line.replace("\n", "")
      parts = line.split(";")
      if parts[0] == "id":
        continue
      else: 
        output_list.append(parts)

  return output_list


def read_course_files(file_name: str) -> tuple:
  output_list = []

  with open(file_name) as new_file:
    for line in new_file:
      parts = line.split(":")
      output_list.append(parts[1].strip())

  return output_list[0], output_list[1]


def map_names(file_name: str) -> dict:
  students = {}
  content_list = read_student_files(file_name)

  for row in content_list:
    student_key = row[0]
    name = f"{row[1]} {row[2]}"
    students[student_key] = name

  return students


def map_exercises(file_name: str) -> dict:
  exercises = {}
  content_list = read_student_files(file_name)

  for row in content_list:
    student_key = row[0]
    exercise_points = sum([int(points) for points in row[1:]])
    exercises[student_key] = exercise_points
  
  return exercises


def map_exams(file_name: str) -> dict:
  exams = {}
  content_list = read_student_files(file_name)

  for row in content_list:
    student_key = row[0]
    exam_scores = sum([int(scores) for scores in row[1:]])
    exams[student_key] = exam_scores

  return exams


def get_grades(student_file: str, exercise_file: str, exam_file: str) -> list:

  names_dict = map_names(student_file)
  exercises_dict = map_exercises(exercise_file)
  exams_dict = map_exams(exam_file)

  grades = []

  for key, value in names_dict.items():

    # scale exercise points earned
    number_completed = int(exercises_dict[key])
    percentage_completed = ( number_completed / 40 ) * 100 # convert raw points to %
    exercise_points = int(percentage_completed // 10) # round down to nearest % tier per instructions
    
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
    student_id = key
    grades.append( (name, student_id, number_completed, exercise_points, exam_points, total_points, grade) )

  return grades

  
def save_results() -> None:
  # hardcoded for testing
  # student_file = "students1.csv" # testing
  # exercise_file = "exercises1.csv" # testing
  # exam_file = "exam_points1.csv" # testing
  # course_file = "course1.txt" # testing

  # get file names from user input
  student_file = input("Student information: ")
  exercise_file = input("Exercises completed: ")
  exam_file = input("Exam points: ")
  course_file = input("Course information: ")

  course_name, course_credits = read_course_files(course_file)
  student_stats = get_grades(student_file, exercise_file, exam_file)

  with open("results.txt", "w") as new_file:
    new_file.write(f"{course_name}, {course_credits} credits\n======================================\n")
    new_file.write(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}\n")
    for student in student_stats:
      name, student_id, number_completed, exercise_points, exam_points, total_points, grade = student
      new_file.write(f"{name:30}{str(number_completed):10}{str(exercise_points):10}{str(exam_points):10}{str(total_points):10}{str(grade):10}\n")

  with open("results.csv", "w") as new_file:
    for student in student_stats:
      name = student[0]
      student_id = student[1]
      grade = student[6]
      new_file.write(f"{student_id};{name};{grade}\n")

  print("Results written to files results.txt and results.csv")


# save_results() # testing


# ========================

if __name__ == "__main__":
  pass

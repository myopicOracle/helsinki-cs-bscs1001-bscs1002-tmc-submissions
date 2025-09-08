# In this series of exercises you will create a simple student database. Before diving in, please spend a moment reading through the instructions and thinking about what sort of data structures are necessary for organising the data stored by your program.

# Part 1. Adding students

#   First write a function named add_student, which adds a new student to the database. Also write a preliminary version of the function print_student, which prints out the information of a single student.

# Part 2. Adding completed courses

#   Please write a function named add_course, which adds a completed course to the information of a specific student in the database. The course data is a tuple consisting of the name of the course and the grade:

# Part 3. Repeating courses

#   Courses with grade 0 should be ignored when adding course information. Additionally, if the course is already in the database in that specific student's information, the grade recorded in the database should never be lowered if the course is repeated.

# Part 4. Summary of database

#   Please write a function named summary, which prints out a summary based on all the information stored in the database.

# NB: Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests .

# ========================

# Scoping:
#   database -> dictionary of lists, key = student name, value = course list
#   courses -> list of tuples
#   tuple -> string course name, integer grade

# student_database = {
#   "Name": [
#     ("Course One", 3),
#     ("Course Two", 5),
#   ],
# }

# ========================

# Part 1. Adding Students

# def add_student(database: dict, student: str) -> None:
#   database[student] = []
#   # print(database) # debugging statement

# def print_student(database: dict, student: str) -> None:

#   if student not in database:
#     print(f"{student}: no such person in the database")

#   else:
#     print(f"{student}: ")

#     if not database[student]:
#       print(" no completed courses")
#     else:
#       print(f"{database[student]}")

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# print_student(students, "Peter")
# print_student(students, "Eliza")
# print_student(students, "Jack")

# ========================

# Part 2. Adding completed courses

# def add_student(database: dict, student: str) -> None:
#   database[student] = []
#   # print(database) # debugging statement

# def add_course(database: dict, student: str, course: tuple) -> None:
#   database[student].append(course)
#   # print(database) # debugging statement

# def print_student(database: dict, student: str) -> None:

#   if student not in database:
#     print(f"{student}: no such person in the database")

#   else:
#     print(f"{student}: ")
#     number_of_courses = len(database[student])
#     sum_of_grades = 0

#     if number_of_courses == 0:
#       print(" no completed courses")

#     else:
#       print(f" {number_of_courses} completed courses")
#       for course in database[student]:
#         print(f"  {course[0]} {course[1]}")
#         sum_of_grades += course[1]
#       print(f" average grade {sum_of_grades / number_of_courses}")
      
# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# print_student(students, "Peter")

# ========================

# Part 3. Repeating courses

# def add_student(database: dict, student: str) -> None:
#   database[student] = []
#   # print(database) # debugging statement

# def add_course(database: dict, student: str, course: tuple) -> None:
#   database[student].append(course)
#   # print(database) # debugging statement

# def print_student(database: dict, student: str) -> str:

#   if student not in database:
#     print(f"{student}: no such person in the database")

#   else:
#     # print(f"Initial course list: '{database[student]}'") # debugging statement

#     # filter out failed and duplicate courses (keeping highest grade)
#     helper_dictionary = {}
#     for course in database[student]:
#       if course[1] == 0:
#         continue
#       if (course[0] not in helper_dictionary) or (course[1] > helper_dictionary[course[0]]):
#         helper_dictionary[course[0]] = course[1]
#     # print(helper_dictionary) # debugging statement

#     # reconstruct filtered course list from dictionary
#     adjusted_course_list = []
#     for key, value in helper_dictionary.items():
#       course_tuple = (str(key), int(value))
#       adjusted_course_list.append(course_tuple)

#     # begin main print logic
#     number_of_courses = len(adjusted_course_list)
#     sum_of_grades = 0

#     print(f"{student}: ")
#     if number_of_courses == 0:
#       print(" no completed courses")

#     else:
#       print(f" {number_of_courses} completed courses")
#       for course in adjusted_course_list:
#         print(f"  {course[0]} {course[1]}")
#         sum_of_grades += course[1]
#       print(f" average grade {sum_of_grades / number_of_courses}")

# students = {}
# add_student(students, "Peter")
# add_course(students, "Peter", ("Introduction to Programming", 3))
# add_course(students, "Peter", ("Advanced Course in Programming", 2))
# add_course(students, "Peter", ("Data Structures and Algorithms", 0))
# add_course(students, "Peter", ("Introduction to Programming", 2))
# print_student(students, "Peter")

# ========================

# Part 4. Summary of database

def add_student(database: dict, student: str) -> None:
  database[student] = []

def add_course(database: dict, student: str, course: tuple) -> None:
  database[student].append(course)


def print_student(database: dict, student: str) -> str:

  if student not in database:
    print(f"{student}: no such person in the database")

  else:
    # print(f"Initial course list: '{database[student]}'") # debugging statement

    # filter out failed and duplicate courses (keeping highest grade)
    helper_dictionary = {}
    for course in database[student]:
      if course[1] == 0:
        continue
      if (course[0] not in helper_dictionary) or (course[1] > helper_dictionary[course[0]]):
        helper_dictionary[course[0]] = course[1]
    # print(helper_dictionary) # debugging statement

    # reconstruct filtered course list from dictionary
    adjusted_course_list = []
    for key, value in helper_dictionary.items():
      course_tuple = (str(key), int(value))
      adjusted_course_list.append(course_tuple)

    # begin main print logic
    number_of_courses = len(adjusted_course_list)
    sum_of_grades = 0

    print(f"{student}: ")
    if number_of_courses == 0:
      print(" no completed courses")

    else:
      print(f" {number_of_courses} completed courses: ")
      for course in adjusted_course_list:
        print(f"  {course[0]} {course[1]}")
        sum_of_grades += course[1]
      print(f" average grade {sum_of_grades / number_of_courses}")


def create_statistic(database: dict, student: str) -> str:
  helper_dictionary = {}
  for course in database[student]:
    if course[1] == 0:
      continue
    if (course[0] not in helper_dictionary) or (course[1] > helper_dictionary[course[0]]):
      helper_dictionary[course[0]] = course[1]
  # print(helper_dictionary) # debugging statement

  # reconstruct filtered course list from dictionary
  adjusted_course_list = []
  for key, value in helper_dictionary.items():
    course_tuple = (str(key), int(value))
    adjusted_course_list.append(course_tuple)

  # main logic returns a tuple with student name, and best GPA
  sum_of_grades = 0
  for course in adjusted_course_list:
    sum_of_grades += course[1]
  
  number_of_courses = len(adjusted_course_list)
  gpa_of_best = sum_of_grades / number_of_courses

  return student, number_of_courses, gpa_of_best


def summary(database: dict) -> str:
  number_of_students = len(database)
  most_courses = 0
  highest_gpa = 0
  student_with_most_courses = ""
  student_with_highest_gpa = ""

  for student in database:
    student_name, courses_completed, gpa = create_statistic(database, student)
    if courses_completed > most_courses:
      most_courses = courses_completed
      student_with_most_courses = student_name
    if gpa > highest_gpa:
      highest_gpa = gpa
      student_with_highest_gpa = student_name

  print(f"""students {number_of_students} \nmost courses completed {most_courses} {student_with_most_courses} \nbest average grade {highest_gpa} {student_with_highest_gpa}""")

# students = {}
# add_student(students, "Peter")
# add_student(students, "Eliza")
# add_course(students, "Peter", ("Data Structures and Algorithms", 1))
# add_course(students, "Peter", ("Introduction to Programming", 1))
# add_course(students, "Peter", ("Advanced Course in Programming", 1))
# add_course(students, "Eliza", ("Introduction to Programming", 5))
# add_course(students, "Eliza", ("Introduction to Computer Science", 4))
# summary(students)

# ========================

if __name__ == "__main__":
  pass

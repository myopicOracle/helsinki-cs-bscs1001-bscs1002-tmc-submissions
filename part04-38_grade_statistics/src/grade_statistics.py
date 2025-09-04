# Write your solution here

# Programming exercise: Grade statistics
# https://programming-25.mooc.fi/part-4/6-strings-and-lists

# ## Sample output
# Statistics:
# Points average: 14.5
# Pass percentage: 75.0
# Grade distribution:
#   5:
#   4:
#   3: *
#   2:
#   1: **
#   0: *

# Function to get user inputs for all courses
def get_points() -> list:
  all_courses_input = []
  while True:
    user_input = input("Exam points and exercises completed: ")
    if user_input == "":
      break
    exam_points = int(user_input.split(" ")[0])
    # print("exam_points: ", exam_points)
    exercise_points = int(user_input.split(" ")[1])
    # print("exercise_points: ", exercise_points)
    all_courses_input.append([exam_points, exercise_points])
  # print("all_courses_input: ", all_courses_input)
  return all_courses_input

# Function to calculate total points for 1 course
def evaluate_points(course: list) -> float:
  exam_points = course[0]
  # print("exam_points: ", exam_points)
  exercise_points = course[1] // 10
  # print("exercise_points: ", exercise_points)
  course_points = exam_points + exercise_points
  # print("course_points: ", course_points)
  return course_points

# Function to map points to grade for 1 course
def evaluate_grade(course: list) -> int:
  course_points = evaluate_points(course)
  exam_points = course[0]
  # print("exam_points: ", exam_points)
  if exam_points < 10:
    return 0
  else:
    if course_points >= 28:
      return 5
    elif course_points >= 24:
      return 4
    elif course_points >= 21:
      return 3
    elif course_points >= 18:
      return 2
    elif course_points >= 15:
      return 1
    else:
      return 0

# Function to output student's points average (float) and grade distribution (list)
def analyze_statistics() -> list:
  # Get points data for all courses
  all_courses_input = get_points()

  # Set up helper vars
  total_points = 0
  grade_distribution = []

  # Iterate through course data to get total points and grade distribution
  for course in all_courses_input:
    total_points += evaluate_points(course)
    # print("Interim total_points: ", total_points)
    grade_distribution.append(evaluate_grade(course))
    # print("Interim grade_distribution: ", grade_distribution)
  # print("Final total_points: ", total_points)
  # print("Final grade_distribution: ", grade_distribution)

  # Calculate avg points and % courses passed
  points_avg = round(total_points / len(all_courses_input), 1)
  total_courses = len(all_courses_input)
  failed_courses = grade_distribution.count(0)
  pass_percentage = round((((total_courses - failed_courses) / total_courses) * 100 ), 1)

  # Create student record
  student_record = [points_avg, grade_distribution, pass_percentage]
  return student_record


# Main function
def main():
  student_record = analyze_statistics()

  earned_5 = "*" * student_record[1].count(5)
  earned_4 = "*" * student_record[1].count(4)
  earned_3 = "*" * student_record[1].count(3)
  earned_2 = "*" * student_record[1].count(2)
  earned_1 = "*" * student_record[1].count(1)
  earned_0 = "*" * student_record[1].count(0)

  print(f"""
Statistics:
Points average: {student_record[0]}
Pass percentage: {student_record[2]}
Grade distribution:
  5: {earned_5} 
  4: {earned_4} 
  3: {earned_3} 
  2: {earned_2} 
  1: {earned_1} 
  0: {earned_0} 
""")


# ## Test functions
# get_points()
# get_grades()
# test_data = [[15, 87], [10, 55], [11, 40], [4, 17]]
# evaluate_points(test_data[0])
# print(evaluate_grade(test_data[0]))
# evaluate_points(test_data[2])
# print(evaluate_grade(test_data[2]))
main()

# ## TMC Test Block
# if __name__ == "__main__":

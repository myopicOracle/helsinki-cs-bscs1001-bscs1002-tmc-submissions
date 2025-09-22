# The file lottery_numbers.csv containts winning lottery numbers in the following format:
# Sample data

# week 1;5,7,11,13,23,24,30
# week 2;9,13,14,24,34,35,37
# ...etc...

# Each line should contain a header week x, followed by seven integer numbers which are all between 1 and 39 inclusive.

# The file has been corrupted. Lines in the file may contain the following kinds of errors (these exact lines may not be present in the file, but errors in a similar format will be):

# The week number is incorrect:
# Sample data

# week zzc;1,5,13,22,24,25,26

# One or more numbers are not correct:
# Sample data

# week 22;1,**,5,6,13,2b,34

# Too few numbers:
# Sample data

# week 13;4,6,17,19,24,33

# The numbers are too small or large:
# Sample data

# week 39;5,9,15,35,39,41,105

# The same number appears twice:
# Sample data

# week 41;5,12,3,35,12,14,36

# Please write a function named filter_incorrect(), which creates a file called correct_numbers.csv. The file should contain only those lines from the original file which are in the correct format.

# ========================
# comment out "#debugger" and "#testing" before submission to TMC

def read_file(file_name: str) -> list:
  file_data = []

  with open(file_name) as new_file:
    for line in new_file:
      cleaned_line = line.strip()
      file_data.append(cleaned_line)

  return file_data


def save_file(file_name: str, data: list) -> None:
  with open(file_name, "w") as new_file:
    for i, item in enumerate(data):
      if i < len(data) - 1:
        new_file.write(item + "\n")
      else:
        new_file.write(item)


def validation_conditions(weeks: str, numbers: str) -> tuple:
  weeks_list = weeks.split(" ")
  numbers_list = numbers.split(",")  

  # The week number is incorrect
  condition_1 = weeks_list[1].isdigit()

  # One or more numbers are not correct
  condition_2 = all(x.isdigit() for x in numbers_list)

  # Too few numbers
  condition_3 = len(numbers_list) == 7

  # The numbers are too small or large
  condition_4 = condition_2 and all( 1 <= int(x) <= 39 for x in numbers_list)

  # The same number appears twice
  condition_5 = condition_2 and len(numbers_list) == len(set(numbers_list))

  return condition_1, condition_2, condition_3, condition_4, condition_5


def filter_incorrect() -> None:
  correct_data = []

  file_data = read_file("lottery_numbers.csv")
  # print(file_data) # debugger

  for item in file_data:
    parts = item.split(";")
    weeks = parts[0]
    numbers = parts[1]
    condition_1, condition_2, condition_3, condition_4, condition_5 = validation_conditions(weeks, numbers)

    if condition_1 and condition_2 and condition_3 and condition_4 and condition_5:
      correct_data.append(item)

  # print(correct_data) # debugger

  save_file("correct_numbers.csv", correct_data)


# filter_incorrect() # testing


# ========================

if __name__ == "__main__":
  pass
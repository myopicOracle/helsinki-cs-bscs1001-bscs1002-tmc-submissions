# Please write a program which functions as a dictionary. The user can type in new entries or look for existing entries.

# The program should work as follows:
# Sample output

# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: auto
# The word in English: car
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: roska
# The word in English: garbage
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 1
# The word in Finnish: laukku
# The word in English: bag
# Dictionary entry added
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: bag
# roska - garbage
# laukku - bag
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: car
# auto - car
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 2
# Search term: laukku
# laukku - bag
# 1 - Add word, 2 - Search, 3 - Quit
# Function: 3
# Bye!

# The dictionary entries should be written to a file called dictionary.txt. The program should first read the contents of the file. New entries are written to the end of the file whenever they are added to the dictionary.

# The format of the data stored in the dictionary is up to you.

# NB: the automatic tests for this exercise may change the contents of the file. If you want to keep its contents, first make a copy of the file under a different name.

# ========================

def add_word() -> None:
  finnish_word = input("The word in Finnish: ")
  english_word = input("The word in English: ")

  with open("dictionary.txt", "a") as new_file:
    entry = f"{finnish_word};{english_word}\n"
    new_file.write(entry)

  print("Dictionary entry added")


def search_dictionary() -> None:
  search_term = input("Search term: ")
  matched_results = []

  with open("dictionary.txt") as new_file:
    for line in new_file:
      line = line.strip()
      # print("line: ", line) # debugger
      parts = line.split(";")
      # print("parts: ", parts) # debugger
      if search_term in parts[0] or search_term in parts[1]:
        matched_results.append(f"{parts[0]} - {parts[1]}")
        # print(matched_results) # debugger
      else:
        continue

  if matched_results:
    for result in matched_results:
      print(result)


while True:
  print("1 - Add word, 2 - Search, 3 - Quit")
  user_command = int(input("Function: "))
  if user_command == 1:
    add_word()
  elif user_command == 2:
    search_dictionary()
  elif user_command == 3:
    print("Bye!")
    break
  else:
    print("Please enter a valid command: 1 - Add word, 2 - Search, 3 - Quit.")


# ========================

if __name__ == "__main__":
  pass

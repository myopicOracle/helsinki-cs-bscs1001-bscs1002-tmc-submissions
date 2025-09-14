# Please write a program which works as a simply diary. The diary entries should be saved in the file diary.txt. When the program is executed, it should first read any entries already in the file.

# The program should work as follows:
# Sample output

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: Today I ate porridge
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 1
# Diary entry: I went to the sauna in the evening
# Diary saved

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

# When the program is executed for the second time, this should happen:
# Sample output

# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 2
# Entries:
# Today I ate porridge
# I went to the sauna in the evening
# 1 - add an entry, 2 - read entries, 0 - quit
# Function: 0
# Bye now!

# ========================

while True:
  print("1 - add an entry, 2 - read entries, 0 - quit")
  user_command = int(input("Function: "))
  if user_command == 1:
    with open("diary.txt", "a") as new_file:
      user_input = input("Diary entry: ")
      new_file.write(f"{user_input}\n")
    print("Diary saved")
  elif user_command == 2: 
    print("Entries:")
    with open("diary.txt") as new_file:
      for line in new_file:
        line = line.strip()
        print(line)
  elif user_command == 0: 
    print("Bye now!")
    break


# ========================

if __name__ == "__main__":
  pass

# Please write an improved version of the phone book application. Each entry should now accommodate multiple phone numbers. The application should work otherwise exactly as above, but this time all numbers attached to a name should be printed.

# Sample output

# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 040-5466745
# ok!
# command (1 search, 2 add, 3 quit): 2
# name: emily
# number: 045-1212344
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# command (1 search, 2 add, 3 quit): 1
# name: mary
# no number
# command (1 search, 2 add, 3 quit): 2
# name: peter
# number: 09-22223333
# ok!
# command (1 search, 2 add, 3 quit): 1
# name: peter
# 040-5466745
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...

# ========================

my_dictionary = {}

while True:
  user_input = int(input("command (1 search, 2 add, 3 quit): "))

  # Search for existing entry
  if user_input == 1:
    name = input("name: ")
    if name not in my_dictionary:
      print("no number")
    else:
      for number in my_dictionary[name]:
        print(number)

  # Add new entry
  elif user_input == 2:
    name = input("name: ")
    new_number = input("number: ")
    if name in my_dictionary:
      my_dictionary[name].append(new_number)
      print("ok!")
    else:
      number = []
      number.append(new_number)
      my_dictionary[name] = number
      print("ok!")

  # Quit program
  elif user_input == 3:
    print("quitting...")
    break # loop only breaks if user specifies quit command '3'

  # Handle command input error
  else:
    print("Beep... boop... You have entered an invalid command! Please enter 1 to search, 2 to add, 3 to quit.")

# print(f"Final phonebook is: {my_dictionary}")

# ========================

if __name__ == "__main__":
  pass

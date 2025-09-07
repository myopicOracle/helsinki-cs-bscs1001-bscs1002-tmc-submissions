# Please write a phone book application. It should work as follows:

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
# 09-22223333
# command (1 search, 2 add, 3 quit): 3
# quitting...

# As you can see above, each name can be attached to a single number only. If a new entry with the same name is added, the number attached to the old entry is replaced with the new number.

# ========================

my_dictionary = {}

while True:
  user_input = int(input("command (1 search, 2 add, 3 quit): "))
  if user_input == 1:
    name = input("name: ")
    if name not in my_dictionary:
      print("no number")
    else:
      print(my_dictionary[name])
  elif user_input == 2:
    name = input("name: ")
    number = input("number: ")
    my_dictionary[name] = number
    print("ok!")
  elif user_input == 3:
    print("quitting...")
    break # loop only breaks if user specifies quit command '3'
  else:
    print("Beep... boop... You have entered an invalid command! Please enter 1 to search, 2 to add, 3 to quit.")

# print(f"Final phonebook is: {my_dictionary}")


# ========================

if __name__ == "__main__":
  pass

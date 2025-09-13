# Please write a program which asks the user to type in some text. Your program should then perform a spell check, and print out feedback to the user, so that all misspelled words have stars around them. Please see the two examples below:

# Sample output

#   Write text: We use ptython to make a spell checker
#   We use *ptython* to make a spell checker

# Sample output

#   Write text: This is acually a good and usefull program
#   This is *acually* good and *usefull* program

# The case of the letters should be irrelevant to the functioning of your program.
# The exercise template includes the file wordlist.txt, which contains all the words the spell checker should accept as correct.

# NB: this exercise doesn't ask you to write any functions, so you should not place any code within an if __name__ == "__main__" block.

# ========================

input_string = input("Write text: ")
# input_string = "We use ptython to make a spell checker" # hardcoded for testing
list_of_accepted_words = []

with open("wordlist.txt") as new_file:
  for line in new_file:
    word = line.strip()
    list_of_accepted_words.append(word)
  # print(len(list_of_accepted_words)) # debugger
  # print(list_of_accepted_words[:10]) # debugger

string_to_list = input_string.split(" ")
# print(string_to_list) # debugger

for index, word in enumerate(string_to_list):
  if word.lower() not in list_of_accepted_words:
    string_to_list[index] = f"*{word}*"
  else:
    continue

# print(string_to_list) # debugger
checked_string = " ".join(string_to_list)

print(checked_string)

# ========================

if __name__ == "__email__":
  pass

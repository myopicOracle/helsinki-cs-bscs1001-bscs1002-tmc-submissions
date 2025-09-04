# Write your solution here

# Sample output

# Word: once
# Word: upon
# Word: a
# Word: time
# Word: upon
# You typed in 4 different words

# item = 3

# if item not in [0,1,2]:
#   print("true")
# else:
#   print("false")

my_list = []
counter = 0

while True:
  word = ""
  word = input("Word: ")
  if word in my_list:
    print(f"You typed in {counter} different words")
    break
  my_list.append(word)
  counter += 1
  # print(my_list)

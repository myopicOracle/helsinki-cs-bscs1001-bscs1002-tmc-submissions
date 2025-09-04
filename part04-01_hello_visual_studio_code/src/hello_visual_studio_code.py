# Write your solution here
while True:

  string = input("Editor: ")

  editor = string.lower()

  if editor == "visual studio code":
    print("an excellent choice!")
    break

  elif editor == "notepad" or editor == "word":
    print("awful")

  else:
    print("not good")
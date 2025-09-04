# Write your solution here

string = input("Please type in a string: ")

limit = len(string)
index = -1

for step in range(0,limit):
    print(string[index])
    index -= 1
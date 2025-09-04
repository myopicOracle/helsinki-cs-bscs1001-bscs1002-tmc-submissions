# Write your solution here

string_1 = input("Please type in string 1: ")
string_2 = input("Please type in string 2: ")

if len(string_1) == len(string_2):
    print("The strings are equally long")
elif len(string_1) > len(string_2):
    print(f"{string_1} is longer")
else:
    print(f"{string_2} is longer")
# Write your solution here

string = input("Please type in a string: ")

alpha = string[1]
omega = string[-2]

if alpha == omega: 
    print(f"The second and the second to last characters are {alpha}")
else: 
    print("The second and the second to last characters are different")
    
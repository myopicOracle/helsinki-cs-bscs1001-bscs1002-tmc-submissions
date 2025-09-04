from math import sqrt
# Write your solution here

user = int(input("Please type in a number: "))

while user != 0:

    if user < 0:
        print("Invalid number")
    else: 
        print(f"{sqrt(user)}")
    
    user = int(input("Please type in a number: "))

print("Exiting...")